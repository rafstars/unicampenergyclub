#Importando a biblioteca PyMySQL

import pymysql

#Crindo conexão com o servidor local

database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="unicamp_energy_club"
)

cursor = database.cursor()

# Inserindo dados

com_sql = "insert into empresas(nome, serviços, contato, site) values (%s, %s, %s, %s)"
valor = [("CPFL Energias Renováveis AS", "Atua no ramo da energia solar, biomassa, eolica e hidreletrica", "jornalismo@cpfl.com.br", "http://www.cpflrenovaveis.com.br/"),
         ("Canadian Solar", "Fabricante de módulos fotovoltaicos solares e um fornecedor de soluções", "Telefone: +55 11 3957-4600", "https://canadiansolar.com.br/la/"),
         ("IPERSOL", "Projetos e Instalações Fotovoltaicas", "contato@ipersol.com.br", "https://ipersol.com.br/"),
         ("NeoSol Energia", "Projetos para construção e reformas, focados na geração fotovoltaica", "contato@neosol.com.br", " http://www.neosol.com.br"),
         ("EverSun", "Painel Fotovoltaico, projeto fotovoltaico, inversor, regularização", "fabio@eversun.com.br", "http://eversun.com.br/"),
         ("Dexxtrasolar", "Serviços de Engenharia no ramo de Energias Renováveis", "contato@dexxtrasolar.com.br", " https://www.suncorp.com.br"),
         ("Proinst solar", "Estudo e dimensionamento do sistema de geração fotovoltaico", "solar@proinst.com.br", "https://www.proinst.com.br/"),
         ("SUNCORP", "Serviços e projetos na area de energia solar fotovoltaica", "atendimento@suncorp.com.br", " https://www.suncorp.com.br"),
         ]
cursor.executemany(com_sql, valor)

database.commit()

print(cursor.rowcount, "inserida com sucesso")