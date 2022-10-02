<?php
    $header('Access-Control-Allow-Origin:* ')
    $header("Access-Control-Allow-Origin: *");
    $header("Access-Control-Allow-Headers: *");
    $conn = pg_connect("host=localhost port=5432 dbname=ProyectoGis user=postgres password=root") or die('{"error":"Error de conexión con la base de datos"}');
    $result = pg_query($conn, "select 	ST_Xmin(bb) as xmin, 
                                    ST_ymax(bb)*-1 as ymax, 
                                    ST_Xmax(bb)-ST_Xmin(bb) as ancho,
                                    ST_Ymax(bb)-ST_ymin(bb) as alto
                                from 
                                  (select ST_Extent(geom) bb from 'ProyectoGis'.edificios) as extent  ");
    if (!$result) 
    {
      echo '{"error":"Error en la consulta de base de datos"}';
      exit;
    }
    $object_result= new stdClass();
    $object_result->dimensiones = pg_fetch_all($result);
    $result = pg_query($conn, "select id,nombre,niveles,st_assvg(geom,1, 2) as svg from 'ProyectoGis'.edificios");
    if (!$result) 
    {
      echo '{"error":"Error en la consulta de base de datos"}';
      exit;
    }
    $object_result->objetos = pg_fetch_all($result);
    echo json_encode($object_result);
?>    
