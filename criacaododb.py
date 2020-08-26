#Importando a biblioteca PyMySQL

import pymysql

#Crindo conexão com o servidor local

database = pymysql.connect(
    host="localhost",
    user="root",
    passwd=""
)

#Criação do banco de dados
cursor = database.cursor()
cursor.execute("create database unicamp_energy_club")
