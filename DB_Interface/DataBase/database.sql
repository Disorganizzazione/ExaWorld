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
    dsimili      percent not null, --FIIIIIIIILLLLLLLLLLL!!! >:(
    sedentarietà percent not null,
    riproduzione percent not null
);


create table creature(
    id integer primary key default NEXTVAL('cod_creat'),
    nome varchar(50) not null,
    comp integer references comportamento on delete cascade,
    tipo tipod default 'v',
    danno integer default null,
    sesso boolean default null,
    dieta dietad default null
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

create table habitat(
    creatura integer references creature on delete cascade,
    tmin integer not null,
    tmax integer not null,
    umin integer not null,
    umax integer not null,
    primary key(creatura)
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
\copy comportamento (nome, aggressività, dsimili, sedentarietà, riproduzione) from comportamento.txt;
\copy creature (nome, comp, tipo,danno,sesso,dieta)from creature.txt; --il join qua dà problemi

--viste
create view animali as select id, nome, comp, danno, sesso, dieta from creature where tipo = 'a';
create view piante as select id, nome, comp from creature where tipo='v' ;

create view carnivori as select * from animali where dieta='c';
create view erbivori as select * from animali where dieta='e';
create view onnivori as select * from animali where dieta='o';

--trigger
create function posto()returns trigger as $body$
declare
    t1 integer not null := random()*100;
    t2 integer not null := t1 + (10+random()*20);
    u1 integer not null := random()*100;
    u2 integer not null := u1 + (10+random()*20);
    temp integer;
begin
    insert into habitat(creatura, tmin, tmax, umin, umax) values (new.id, t1, t2, u1, u2);
    return null;
end
$body$
language plpgsql;

create trigger certezza after insert on creature for each row execute procedure posto();

