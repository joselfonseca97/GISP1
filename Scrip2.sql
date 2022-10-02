/*Nombre de la base de datos ProyectoGis*/

CREATE TABLE "ProyectoGis".rutasEvacuacion(
	id serial primary key not null,
	geom geometry(MULTILINESTRING,5367) null
);
alter table "ProyectoGis".rutasEvacuacion add column idEdificio int null
alter table "ProyectoGis".rutasEvacuacion add constraint FK_idEdificio FOREIGN KEY (idedificio)references "ProyectoGis".edificios(id);


CREATE TABLE "ProyectoGis".zonasSeguras(
	id serial primary key not null,
	geom geometry(MultiPolygon,5367) null
);
alter table "ProyectoGis".zonasSeguras alter column tipoTerreno TYPE varchar(25) NULL
alter table "ProyectoGis".zonasSeguras add column idedificio int null
alter table "ProyectoGis".zonasseguras add constraint FK_idEdificio FOREIGN KEY (idedificio)references "ProyectoGis".edificios(id);
alter table "ProyectoGis".zonasSeguras add column nombre varchar(25) null

update "ProyectoGis".zonasseguras  set idedificio=16 where id=1;
update "ProyectoGis".zonasseguras set idedificio=29 where id=2;
update "ProyectoGis".zonasseguras set idedificio=6 where id=3;
update "ProyectoGis".zonasseguras set idedificio=148 where id=4;
update "ProyectoGis".zonasseguras set idedificio=8 where id=8;
update "ProyectoGis".zonasseguras set tipoterreno='Zona verde'



update "ProyectoGis".rutasevacuacion set idedificio=16 where id=6;
update "ProyectoGis".rutasevacuacion set idedificio=16 where id=7;
update "ProyectoGis".rutasevacuacion set idedificio=6 where id=2;
update "ProyectoGis".rutasevacuacion set idedificio=6 where id=3;
update "ProyectoGis".rutasevacuacion set idedificio=148 where id=1;
update "ProyectoGis".rutasevacuacion set idedificio=29 where id=4;
update "ProyectoGis".rutasevacuacion set idedificio=29 where id=5;
update "ProyectoGis".rutasevacuacion set idedificio=8 where id=8;


select * from "ProyectoGis".zonasseguras as A
select * from "ProyectoGis".edificios as B
select * from "ProyectoGis".rutasevacuacion as C