#Importando a biblioteca PyMySQL

import pymysql

#Crindo conexão com o servidor local

database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="unicamp_energy_club"
)
mycursor=database.cursor()

#Criando a tabela "professores"
mycursor.execute("CREATE TABLE professores(nome varchar(80), area VARCHAR(255),site VARCHAR(80),contato VARCHAR(255),professoresID tinyint PRIMARY KEY AUTO_INCREMENT)")