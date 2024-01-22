-- SQL > Structured Query Language


-- DDL
-- Data Definition Language (lenguaje de definicion de datos)

CREATE DATABASE IF NOT EXISTS pruebas;

use pruebas;

CREATE TABLE personas (
	id int primary key auto_increment,
    nombre text null,
    apellido varchar(50),
    fecha_nacimiento date,
    nacionalidad varchar(100) default 'PERUANO'
);

-- DML
-- Data Manipulation language (Lenguaje de manipulacion de datos)

-- agregar informacion a la tabla
insert into personas (id, nombre, apellido, fecha_nacimiento) values 
					 (default, 'Eduardo','de Rivero','1992-08-01');
                     
-- si no declaro las columnas que voy a insertar me veo en la obligacion de colocar valores a todas las columnas y siguiendo el mismo orden
-- que use al momento de crear la tabla
insert into personas values (default, 'Juana', 'Martinez', '2004-02-10', 'URUGUAYO');

insert into personas (nombre, apellido, fecha_nacimiento,nacionalidad) values 
					 ('Bryan','Urquizo','1995-02-14', 'PERUANO'),
                     ('Maria','Retamozo','1989-06-14', 'SALVADOREÑA');
                     
select id,nombre from personas; 
select * from personas;

select * from personas where nombre = 'Eduardo';
select * from personas where nacionalidad = 'Peruano' and id=3;

select * from personas where nombre like '%a%';
select * from personas where nombre like '__u%';

-- devolver todas la personas cuyo nombre tenga la letra 'r' o en su apellido tenga la letra 'a'
select * from personas where nombre like '%r%' or apellido like '%a%';

select * from personas where id in (1,2,3);
select * from personas where id = 1 or id = 2 or id = 3;

select * from personas 
limit 2 -- 2 elementos por pagina
offset 2; -- offsert sirve para indicar cuantos se tiene que saltar

-- Actualizaciones
update personas 
set nombre = 'Rodrigo', apellido = 'Flores'
where id = 1;

select * from personas where id = 1;

delete from personas where id = 4;

select * from personas;

-- Direcciones 













