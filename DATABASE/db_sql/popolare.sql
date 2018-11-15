insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('feroce', 100, 30, 50, 20);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('pascolatore', 30, 20, 70, 40);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('difensore', 50, 40, 90, 70);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('individuale', 70, 80, 20, 90);
insert into comportamento(nome, aggressività, branco, sedentarietà, riproduzione) values ('nomade', 10, 90, 40, 10);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('wolf', 1, 'a', 3, 2, 7, 'c', -20, 20, 5, 50);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('cow', 2, 'a', 6, 1, 3, 'e', 0, 35, 10, 70);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('bear', 3, 'a', 9, 7, 2, 'c', -20, 30, 10, 60);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('panther', 4, 'a', 5, 4, 8, 'c', 15, 40, 5, 55);
insert into creature(nome, comp, tipo, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax) values ('rabbit', 5, 'a', 2, 1, 9, 'e', -15, 30, 20, 60);
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('grass', 90, 'v', 4, 0, 30, 30, 80 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('oak', 30, 'v', 40, 0, 30, 20, 50 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('berry_bush', 10, 'v', 7, -20, 30, 15, 70 );
insert into creature(nome, riprod, tipo, resistenza, tmin, tmax, umin, umax) values ('fir', 50, 'v', 20, -30, 15, 10, 60 );

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

insert into terreno(nome,tmin,tmax,umin,umax) values('acqua',1,99,30,100);
insert into terreno(nome,tmin,tmax,umin,umax) values('deserto',-20,50,4,30);
insert into terreno(nome,tmin,tmax,umin,umax) values('ghiaccio',-30,0,30,100);
insert into terreno(nome,tmin,tmax,umin,umax) values('erba',10,30,30,50);




