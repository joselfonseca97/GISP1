import os
import psycopg2
from psycopg2.extras import RealDictCursor

#DataBase info
db= os.getenv('PG_DATABASE')
db_user=os.getenv('PG_USER')
db_pass=os.getenv('PG_PASSWORD')
db_host=os.getenv('PG_HOST')
db_port=os.getenv('PG_PORT')

def getEdificioData(idEdificio):
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('select ST_Xmin(bb) as xmin, ST_ymax(bb)*-1 as ymax, ST_Xmax(bb)-ST_Xmin(bb) as ancho,ST_Ymax(bb)-ST_ymin(bb) as alto from (select ST_Extent(geom) bb from proyectoGis.geometrias where idEdificio=%s) as extent',(idEdificio,))
        list= cur.fetchall()
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select nombre,niveles,area,st_assvg(geom,1, 2) as svg from proyectoGis.edificios where id=%s",(idEdificio,))
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select nombre,area,capacidad,tipoterreno,st_assvg(geom,1,2)as svg from proyectogis.zonasseguras where zonasseguras.idedificio=%s",(idEdificio,))
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,st_assvg(geom,1,2) as svg from proyectogis.rutasevacuacion where idEdificio=%s",(idEdificio,))
        list.append(cur.fetchall())
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

#Consulta que carga todas las capas
def getMedidas():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select ST_Xmin(bb) as xmin, ST_ymax(bb)*-1 as ymax, ST_Xmax(bb)-ST_Xmin(bb) as ancho,ST_Ymax(bb)-ST_ymin(bb) as alto from (select ST_Extent(geom) bb from proyectoGis.zonas_verdes) as extent")
        list= cur.fetchall()
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,nombre,tipo,st_assvg(geom,1,2) as svg from proyectoGis.vialidad")
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,descipcion,st_assvg(geom,1, 2) as svg from proyectoGis.aceras")
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,tipo,st_assvg(geom,1,2) as svg from proyectoGis.zonas_verdes")
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,tipoTerreno,nombre,st_assvg(geom,1,2) as svg from proyectoGis.zonasSeguras")
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,st_assvg(geom,1, 2) as svg from proyectoGis.rutasevacuacion")
        list.append(cur.fetchall())
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,nombre,niveles,st_assvg(geom,1, 2) as svg from proyectoGis.edificios")
        list.append(cur.fetchall())
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200
