########################AULA_01##############################
Introdução a liguagem SQL
DDL - Linguagem de definição de dados - Estrutura
Criando tabelas
Sintaxe:
    create table nome_tabela
    (nome_coluna tipo_dados(tamanho) [regra],
    
    nome_colunaN tipo_dados(tamanho) [regra]);
    
    
    
Tipo de dados: char(n), campo alfanumérico de tamanho fixo(String)
               varchar(n), campo alfanumérico variável 
               number(x,y), campo numérico inteiro ou real
               date, campo tipo data
               
               
               
n = tamanho
x = parte inteira
y = parte real, casas decimais

constraint = nomear

Regras/Constraints
Pk - primary key, campo único, preenchimento obrigatório, relacionamento
Fk - foreign key, relacionamento lado n da cardinalidade, recebe dados
    previamente cadastrados na PK
Nn - not null, campo de preenchimento obrigatório
Uk - unique, campo com restrição a dados repetidos
Ck - check, campo com lista de dados para validação

    
    
#toda chave primaria terá o mesmo tamanho e título da estrangeira
    
###Criando o relacionamento###

1 - 1 - Pk + Fk_Uk
1 - N - Pk + Fk
N - N - não existe em código sql, usa se duas tabelas 1 - N



    
##visualizando a estrutra de uma tabela
desc nome_tabela
exemplo: desc cargo10



##deletando uma tabela
drop table nome_tabela
exemplo: drop table cargo10



##visualizando constraints
select constraint_name, constraint_type from user_constraints
where table_name = 'CARGO10'





###Exemplo 1 (sem regras)###

create table cargo10
(cd_cargo number(3),
nm_cargo varchar2(25),
salario number(8,2));

desc cargo10




###Exemplo 2 (com regras, sem personalização)###

create table cargo10
(cd_cargo number(3) primary key,
nm_cargo varchar2(25)not null unique,
salario number(8,2));

desc cargo10




###Exemplo 3 boas praticas###

create table cargo10
(cd_cargo number(3) constraint cargo_cd_pk primary key,
nm_cargo varchar2(25)constraint cargo_nome_nn not null
                     constraint cargo_nome_uk unique,
salario number(8,2));




create table funcionario10
(cd_fun number(3) constraint fun-cd-pk primary key,
nm_fun varchar(30) constraint fun_nm_nn not null,
dt_adm date constraint fun_dt_nn not null,
uf_fun char(2) constraint fun_uf_nn not null,
cargo_fk number(3) constraint fun_cargo_fk references cargo10)








###Exercicio###


Criação das tabelas: n_fiscal e produto

15/02/2023

create table n_fiscal
(n_nf number(5) primary key,
dt_nf date not null,
total_nf number(10,2));

select constraint_name from user_constraints where table_name = 'N_FISCAL'

desc n_fiscal

create table produto
(cd_pro number(5) constraint prod_cd_pk primary key,
nm_prod varchar2(30) constraint prod_mn_nn not null
constraint prod_nm_uk unique,
preco number(10,2))

select constraint_name from user_constraints where table_name = 'PRODUTO'

create table tem
(fk_nota number(5) constraint tem_nf_fk references n_fiscal,
fk_prod number(5) constraint tem_prod_fk references produto)





##########################################################################
AULA_02



Inserindo dados
Comando DML - Data Manipulation Language
Novas linhas:
insert into nome_tabela values
(valor1, valor2,...., valorN)

Obs: campos: char, varchar ou varchar2 e date precisam de apóstrofe

Exemplo 1
conhecendo ou visualizando a estrutura
desc n_fiscal
inserindo uma linha

insert into n_fiscal values (1,'10-Jan-00',5000);
insert into n_fiscal values (2,'10-dec-00',5000);

#####Verificando a inserção
select * from n_fiscal

#####Descobrindo o padrão da data
select sysdate from dual
gravando dados fisicamente
commit;







###Exercício###

/*1-) Criar  todas  as  tabelas,  de  acordo  com o  modelo relacional/lógico,
definindo  todas  as restrições de chaves e demais
restrições mencionadas no modelo.*/


/*Categoria classifica Filme*/
create table categoria 
(cod_categoria number(4) constraint cd_categ_pk primary key,
descricao varchar(50) constraint desc_filme_nn not null);

create table classifica
(cd_categ_fk number(4) constraint possui_cdfilme_fk references filme,
cd_filme_fk number(4) constraint possui_cdcateg_fk references categoria);

create table filme
(cod_filme number(4) constraint cd_filme_pk primary key,
titulo varchar(20) constraints nome_filme_nn not null);

/*Ator estrela Filme*/

create table ator
(cod_ator number(4) constraint cd_ator_pk primary key,
nome_popular varchar(50) constraints nm_pop_nn not null,
nome_arte varchar(50),
datanasc date);

create table estrela
(fk_filme number(4) constraint estrela_filme_fk references filme,
fk_ator number(4) constraint estrela_ator_fk references ator);

/*(fk_nota number(5) constraint tem_nf_fk references n_fiscal,
fk_prod number(5) constraint tem_prod_fk references produto)*/

/*DVD possui FILME*/

create table dvd
(num_dvd number(4) constraint num_dvd_pk primary key,
tipo char(1));

create table possui
(dvd_fk number(4) constraint possui_dvd_fk references dvd,
filme_fk number(4) constraint possui_filme_fk references filme);

/*Cliente aluga DVD*/

create table cliente
(cod_cliente number(4) constraint cd_cli_pk primary key,
pre_nome varchar(50) constraint pre_nome_nn not null,
sobre_nome varchar(50),
endereco varchar(70),
telefone varchar(20));

create table aluga
(cliente_fk number(4) constraint cd_cliente_fk references cliente,
dvd_fk number(4) constraint num_dvd_fk references dvd,
data_ret date,
data_dev date);


/*2-) Insira todas os valores apresentados nastabelas FILME, CLIENTE,
DVDe CATEGORIA.(Utilize vários insert’s).*/

/*Insert Filme*/
insert into filme values ('1111', 'Forest Gump');
insert into filme values ('2222', 'Titanic');
insert into filme values ('3333', 'Island soul');
insert into filme values ('4444', 'Jordan Man');

select * from filme

/*Insert Cliente*/

insert into cliente values (6666, 'Victor', 'Shimada', 'Rua Visconde, 566', '11-983272594');
insert into cliente values (5555, 'Beatriz', 'Arantes', 'Rua Pipo, 564', '11-98456994');
insert into cliente values (4444, 'Derli', 'Arantes', 'Rua China, 66', '11-9838886594');
insert into cliente values (3333, 'Eliana', 'Almeida', 'Rua Padre Anchieta, 566', '11-9862594');

select * from cliente

/*Insert DVD*/

insert into dvd values (1111, 'A');
insert into dvd values (9898, 'B');
insert into dvd values (7878, 'C');
insert into dvd values (9887, 'D');

select * from dvd

/*Insert Categoria*/

insert into categoria values (5656, 'É um ótimo filme');
insert into categoria values (8986, 'É um péssimo filme');
insert into categoria values (5787, 'É um filme razoável');
insert into categoria values (5988, 'É um decente filme');

select * from categoria

/*3-) Altere o número da categoria Comédia de 01 para 08 na tabela CATEGORIA.*/

update categoria set cod_categoria = 1234
where cod_categoria = 5656

select * from categoria

/*4-) Insira a coluna SINOPSE na tabela FILME com 300 caracteres.*/

alter table filme add sinopse varchar(300)

desc filme

/*5-) Cadastre uma nova categoria de filme chamada FICÇÃO.*/

insert into categoria values (5555 , 'Ficção');

select * from categoria

/*6-) Apague o filme chamado “Anjos Malditos” e “A melodia da vida” da tabela 
FILME. Para isso, utilize um único comando. */

commit;







#######################################################################
Aula 03 - 01/03/2023

/*Ainda trabalhando com estrutura das tabelas*/

DDL
Create - Ok

/*Alterando ou corrigindo uma estrutura*/ 
alter table nome_tabela

#Opções

add column          - nova coluna
add constraint      - nova regra 
modify              - modifica tipo e/ou tamanho de uma coluna
drop column         - elimina uma coluna
drop constraint     - elimina uma regra


create table tb_teste
(codigo number(2),
nome number(10));


/*Incluindo uma nova coluna*/
alter table tb_teste add dt_nasc date

/*Incluindo uma coluna com regra*/
alter table tb_teste add column cep char(8) not null

/*Incluindo a pk na coluna codigo*/
alter table tb_teste add constraint pk_cod primary key (nome_coluna)
desc tb_teste

/*Modificando apenas o tipo de dados*/
alter table tb_teste modify nome varchar(10)
desc tb_teste

/*Modificando apenas o tamanho da coluna*/
alter table tb_teste modify nome varchar(50)
desc tb_teste

/*Modificando tamanho e tipo ao mesmo tempo*/
alter table tb_teste modify nome number(10)

/*Eliminando uma regra*/
alter table tb_teste drop constraint pk_cod
desc tb_teste

/*Dicionário de dados*/
desc user_constraints
                                        /*o where é o if da programação*/
select constraint_name from user_constraints where table_name = 'TB_TESTE'

/*Eliminando uma coluna*/
alter table tb_teste drop column nome_coluna
desc tb_teste

/*Renomeando uma coluna*/
alter table tb_teste rename column codigo to cod_cliente

/*Renomeando uma constraint*/
alter table tb_teste rename constraint /*Nome atual*/ to /*Novo nome*/

/*Eliminando uma table*/
drop table nome_tabela
drop table tb_teste



/*Exercicio teste*/

create table tb_teste1
(codigo number(1) primary key)

create table tb_teste2
(codigo number(1) references tb_teste1)

desc tb_teste1
desc tb_teste2

/*Insertando os dados*/
insert into tb_teste1 values(1)

insert into tb_teste values(1)

/*Uso do cascade pretende eliminar o relacionamento 
entre as tabelas e excluir a tabela solicitada*/
drop table tb_teste1 cascade constraints


######################################
Atualizando dados 

Uptade

operadores aritméticos: + - * / ()
           relacionais: > >= < <= = !+ ou <>
           lógicos: and or not
           
           
           
update nome_tabela set nome_coluna = novo_valor;


update nome_tabela set nome_coluna = novo_valor
where condição;






/*Exercício*/

create table produto_tb 
(cod_prod number(4) constraint prod_cod_pk primary key, 
unidade varchar2(3),descricao varchar2(20),val_unit number(10,2))

 

insert into produto_tb values (25,'KG','Queijo',0.97);
insert into produto_tb values (31,'BAR','Chocolate',0.87);
insert into produto_tb values (78,'L','Vinho',2.00);
insert into produto_tb values (22,'M','Linho',0.11);
insert into produto_tb values (30,'SAC','Acucar',0.30);
insert into produto_tb values (53,'M','Linha',1.80);
insert into produto_tb values (13,'G','Ouro',6.18);
insert into produto_tb values (45,'M','Madeira',0.25);
insert into produto_tb values (87,'M','Cano',1.97);
insert into produto_tb values (77,'M','Papel',1.05);
commit;


/*Ver os dados inseridos*/
select * from produto_tb


/*Atualizando os dados do preço do produto para R$1,00*/
update produto_tb set val_unit = 1

/*Atualizando os dados do preço do produto para R$1,50
apenas dos produtos de unidade de medida igual a metro*/
update produto_tb set val_unit = 1.5
where unidade = 'M'
select * from produto_tb



/*Atualizando em 15%* o preço dos produtos de código maior que 30.*/
update produto_tb set val_unit = val_unit * 1.15
where cod_prod = 30

select * from produto_tb

/*Atualizar o nome do produto queijo para queijo de minas*/

update produto_tb set descricao = 'Queijo Minas'
where descricao = 'Queijo'


select * from produto_tb


/*Para os produtos Açucar, Madeira e Linha zerar o seu preço. */

update produto_tb set val_unit = 0
where descricao = 'Acucar'

update produto_tb set val_unit = 0
where descricao = 'Madeira'

update produto_tb set val_unit = 0
where descricao = 'Linha'

select * from produto_tb

desc produto_tb

commit;