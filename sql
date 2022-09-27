/*Nombre de la base de datos ProyectoGis*/

CREATE TABLE rutasEvacuacion(
	id serial primary key not null,
	geom geometry(MULTILINESTRING,5367) null
);
alter table rutasEvacuacion add column idEdificio int null
alter table rutasEvacuacion add constraint FK_idEdificio FOREIGN KEY (idedificio)references edificios(id);


CREATE TABLE zonasSeguras(
	id serial primary key not null,
	geom geometry(MultiPolygon,5367) null
);
alter table zonasSeguras add column tipoTerreno int null
alter table zonasseguras add constraint FK_idEdificio FOREIGN KEY (idedificio)references edificios(id);

update zonasseguras set nombre='Zona PROTEC' where id=3;
update zonasseguras set nombre='Zona Labs Compu' where id=1;
update zonasseguras set nombre='Zona Comedor' where id=4;
update zonasseguras set nombre='Zona Edificios Produccion' where id=6;
update zonasseguras set nombre='Zona CTEC' where id=5;
update zonasseguras set idedificio=16 where id=1
update zonasseguras set idedificio=29 where id=3
update zonasseguras set idedificio=6 where id=4
update zonasseguras set idedificio=8 where id=6
update zonasseguras set idedificio=148 where id=5
update zonasseguras set tipoterreno='Zona verde'


select * from zonasseguras
select * from rutasevacuacion