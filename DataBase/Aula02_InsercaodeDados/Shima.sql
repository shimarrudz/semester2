###############################AULA_01##############################
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







