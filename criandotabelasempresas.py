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

#Criando a tabela "empresas"
mycursor.execute("CREATE TABLE empresas(nome VARCHAR(30), serviços VARCHAR(255), contato VARCHAR(255), site VARCHAR(80), empresasID tinyint PRIMARY KEY AUTO_INCREMENT)")