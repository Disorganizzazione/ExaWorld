drop database if exists exaworld ;
create database exaworld;
\c exaworld;

create schema World;
set search_path to World ;

create domain tipod as char check(value='v' or value='a');
create domain dietad as char check(value='e'or value='c' or value='o');
create domain percent as integer check(value<=100 and value>=0);

create SEQUENCE cod_terr;
create SEQUENCE cod_comp;
create SEQUENCE cod_creat;

create table comportamento(
    id           integer primary key default NEXTVAL('cod_comp'),
    nome         varchar(100) not null,
    aggressività percent not null,
    dsimili percent not null,  
    sedentarietà percent not null,
    riproduzione percent not null
);


create table creature(
    id integer primary key default NEXTVAL('cod_creat'),
    nome varchar(50) not null,
    comp integer default null references comportamento on delete cascade,
    riprod percent default null,
    tipo tipod default 'v',
    resistenza integer not null,
    forza integer default null,
    velocita integer default null,
    dieta dietad default null,
    tmin integer not null,
    tmax integer not null,
    umin integer not null,
    umax integer not null
);

create table erbivoro(
    animale integer references creature on delete cascade,
    vegetale integer references creature on delete cascade,
    primary key (animale,vegetale)
);

create table carnivoro(
    predatore integer references creature on delete cascade,
    preda integer references creature on delete cascade,
    primary key (predatore,preda)
);

create table terreno(
    codice integer primary key default NEXTVAL('cod_terr'),
    nome varchar(50) not null,
    tmin integer not null,
    tmax integer not null,
    umin integer not null,
    umax integer not null
);

--popolazione
\i popolare.sql;

--viste
create view animali as select id, nome, comp, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax from creature where tipo = 'a';
create view piante as select id, nome, resistenza, riprod, tmin, tmax, umin, umax from creature where tipo= 'v' ;
create view carnivori as select * from animali where dieta='c';
create view erbivori as select * from animali where dieta='e';
create view onnivori as select * from animali where dieta='o';


