from importlib.util import resolve_name
from wsgiref.util import request_uri
from flask import jsonify, make_response
from asyncio import constants
import os
import requests
from sqlite3 import DatabaseError
import psycopg2
from psycopg2.extras import RealDictCursor
import json

#DataBase info
db= os.getenv('PG_DATABASE')
db_user=os.getenv('PG_USER')
db_pass=os.getenv('PG_PASSWORD')
db_host=os.getenv('PG_HOST')
db_port=os.getenv('PG_PORT')

def getEdificios():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,nombre,niveles,st_assvg(geom,1, 2) as svg from proyectoGis.edificios")
        list= cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getAceras():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,descipcion,st_assvg(geom,1, 2) as svg from proyectoGis.aceras")
        list= cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getZonasVerdes():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,tipo,st_assvg(geom,1,2) as svg from proyectoGis.zonas_verdes")
        list= cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getZonasSeguras():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,tipoTerreno,nombre,st_assvg(geom,1,2) from proyectoGis.zonasSeguras")
        list= cur.fetchall()
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,st_assvg(geom,1, 2) as svg from proyectoGis.rutasevacuacion")
        list.append(cur.fetchall())
        print(list)
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getRutasEvacuacion():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,st_assvg(geom,1, 2) as svg from proyectoGis.rutasevacuacion")
        list= cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getVialidad():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,nombre,tipo,st_assvg(geom,1,2) as svg from proyectoGis.vialidad")
        list= cur.fetchall()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200

def getMedidas():
    list=[]
    try:
        conn= psycopg2.connect(database=db,user=db_user,password=db_pass,host=db_host,port=db_port) 
        print("")
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select ST_Xmin(bb) as xmin, ST_ymax(bb)*-1 as ymax, ST_Xmax(bb)-ST_Xmin(bb) as ancho,ST_Ymax(bb)-ST_ymin(bb) as alto from (select ST_Extent(geom) bb from proyectoGis.zonas_verdes) as extent")
        list= cur.fetchall()
        cur= conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("select id,nombre,niveles,st_assvg(geom,1, 2) as svg from proyectoGis.edificios")
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
        cur.execute("select id,nombre,tipo,st_assvg(geom,1,2) as svg from proyectoGis.vialidad")
        list.append(cur.fetchall())
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        return 401
    finally:
        conn.close()
        return list, 200
