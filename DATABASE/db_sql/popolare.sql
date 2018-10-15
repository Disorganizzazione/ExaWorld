insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('feroce', 100, 30, 50, 20);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('pascolatore', 30, 20, 70, 40);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('difensore', 50, 40, 90, 70);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('individuale', 70, 80, 20, 90);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('nomade', 10, 90, 40, 10);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('lupo', 1, 'a', 3, 2, 7, 'c', -20, 20, 3, 5);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('mucca', 2, 'a', 6, 1, 3, 'e', 30, 40, 2, 4);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('orso', 3, 'a', 9, 7, 2, 'c', -10, 30, 1, 3);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('pantera', 4, 'a', 5, 4, 8, 'c', 20, 40, 5, 7);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('coniglio', 5, 'a', 2, 1, 9, 'e', -5, 20, 2, 6);
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('erba', 90, 'v', 4, 5, 30, 4, 9 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('quercia', 30, 'v', 40, 10, 25, 2, 5 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('sparaci', 10, 'v', 7, 20, 30, 5, 9 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('abete', 50, 'v', 20, -5, 15, 1, 3 );

insert into carnivoro(predatore, preda) values(1,5);
insert into carnivoro(predatore, preda) values(3,1);
insert into carnivoro(predatore, preda) values(1,2);
insert into carnivoro(predatore, preda) values(1,3);
insert into carnivoro(predatore, preda) values(3,5);
insert into carnivoro(predatore, preda) values(3,4);
insert into carnivoro(predatore, preda) values(4,1);
insert into carnivoro(predatore, preda) values(4,5);
insert into carnivoro(predatore, preda) values(4,2);

insert into erbivoro(animale, vegetale) values(2,1);
insert into erbivoro(animale, vegetale) values(2,3);
insert into erbivoro(animale, vegetale) values(5,1);
insert into erbivoro(animale, vegetale) values(5,3);
insert into erbivoro(animale, vegetale) values(5,2);

<<<<<<< HEAD
=======
insert into terreno(nome,tmin,tmax,umin,umax) values('acqua',1,99,30,100);
insert into terreno(nome,tmin,tmax,umin,umax) values('deserto',-20,50,4,30);
insert into terreno(nome,tmin,tmax,umin,umax) values('ghiaccio',-30,0,30,100);
insert into terreno(nome,tmin,tmax,umin,umax) values('erba',10,30,30,50);



>>>>>>> 2c788fc1a6681cf09c26588a5f3b46bd909a3221

