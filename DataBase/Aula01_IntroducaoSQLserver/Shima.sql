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

create table produto
(id_pro char(8) constraint id_pro_pk primary key,
ds_pro varchar2(10) constraint ds_pro_nn not null,
qtd_pro number(2) constraint qtd_pro__nn not null;

create table n_fiscal
(n_nf char(8) constraint n_nf_pk primary key,
dt_emissao data constraint dt_emissao_nn not null,
qtd_pro number(2) constraint qtd_pro_nn not null);

create table posse
(n_nf references n_fiscal,
id_pro references produto);







