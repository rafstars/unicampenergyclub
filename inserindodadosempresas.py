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

com_sql = "insert into empresas(nome, serviços, telefone, e-mail/site para contato, site) values (%s, %s, %s, %s, %s)"
valor = [("CPFL Energias Renováveis AS", "Atua no ramo da energia solar, biomassa, eolica e hidreletrica", "Telefone: (+55) 11 4532-1300", "e-mail: jornalismo@cpfl.com.br", "http://www.cpflrenovaveis.com.br/"),
         ("Canadian Solar", "Fabricante de módulos fotovoltaicos solares e um fornecedor de soluções", "Telefone: (+55) 11 3957-4600", "site para contato: https://canadiansolar.com.br/la/contato/", "https://canadiansolar.com.br/la/"),
         ("IPERSOL", "Projetos e Instalações Fotovoltaicas", "Telefone:", "email: contato@ipersol.com.br", "https://ipersol.com.br/"),
         ("NeoSol Energia", "Projetos para construção e reformas, focados na geração fotovoltaica", "Telefone: (+55) 19 98242-7575", "e-mail: contato@neosol.com.br", "http://www.neosol.com.br"),
         ("EverSun", "Painel Fotovoltaico, projeto fotovoltaico, inversor, regularização", "Telefone: (+55) 11 2853-5161", "e-mail: fabio@eversun.com.br", "http://eversun.com.br/"),
         ("Dexxtrasolar", "Serviços de Engenharia no ramo de Energias Renováveis", "Telefone: (+55) 11 97442-2743", "e-mail: contato@dexxtrasolar.com.br", "https://www.suncorp.com.br"),
         ("Proinst solar", "Estudo e dimensionamento do sistema de geração fotovoltaico","Telefone: (+55) 51 3737-4912", "e-mail: solar@proinst.com.br/ proinst@proinst.com.br", "https://www.proinst.com.br/"),
         ("SUNCORP", "Serviços e projetos na area de energia solar fotovoltaica", "Telefone: (+55) 11 4524-5060", "e-mail: atendimento@suncorp.com.br", "https://www.suncorp.com.br"),
         ("Alva energia solar", "Projetos, Instalação e Manutenção em Sistemas de Geração de Energia Solar.", "Telefone: (+55) 13 97412-6470", "e-mail: contato@alvaengenharia.com.br","https://www.alvaengenharia.com.br/"),
         ("Bom Tempo Energia Solar","serviços turn-key para sistemas de microgeração e minigeração de energia solar fotovoltaica para sistemas conectados à rede", "Telefone: (+55) 15 3342-7954", "e-mail: contato@bomtemposolar.com.br", "https://bomtemposolar.com.br/"),
         ("Power Supply", "Planejamento e instalação de paineis fotovoltaicos", "Telefone: (+55) 11 3395-5504/ (+55) 11 2249-0283","e-mail: comercial@powersupply.com.br","https://www.powersupply.com.br"),
         ("Casa dos Ventos", "Casa dos Ventos é líder no desenvolvimento de parques eólicos no Brasil.","Telefone: (+55) 11 4084-4200", "site para contato: https://casadosventos.com.br/pt/fale-conosco-rodape (não funciona?)","https://www.casadosventos.com.br/pt/"),
         ("Enel Green Power", "Empresa do Grupo Enel dedicada ao desenvolvimento e gestão da geração de energia a partir de fontes renováveis em todo o mundo.","Telefone: (+55) 11 3197 3019", "site de contato: https://globalprocurement.enel.com/pt/contatos", "https://www.enelgreenpower.com/pt/paises/america-do-sul/brasil"),
         ("EDF Renováveis","A EDF Renewables é uma empresa internacional líder em energias renováveis, com capacidade instalada bruta de 13 GW em todo o mundo.", "Telefone: (+55) 21 3974-6100", "site de contato: https://www.edf-renouvelables.com/contact/", "http://www.edf-renouvelables.com"),
         ("GE","Fornecimento de turbinas eólicas", "Telefone: ", "sit de contato: https://www.ge.com/br/contato", "https://www.ge.com/br/"),
         ("WEG", "A WEG possui produtos e soluções para todas as fontes de energia renovável, como eólica, solar, biomassa, hidráulica (CGHs e PCHS) e resíduos (waste to energy), além de armazenamento de nergia (energy storage) e infraestrutura elétrica (transformadores, seccionadoras, subestações)", "Telefone: (+55) 47 3276-4000", "info-br@weg.net", "https://www.weg.net/institutional/BR/pt/"),
         ("Atvos", "Produzimos e comercializamos etanol, açúcar VHP e energia elétrica através da cana-de-açúcar e da biomassa.", "Telefone: (+55) 11 3096-8000", "site de contato: https://www.atvos.com/contato/", "https://www.atvos.com/"),
         ("Vestas", "A Vestas é uma empresa dinamarquesa e a maior companhia mundial produtora de turbinas de energia eólica", " ", " ", "https://www.vestas.com/#!"),
         ("Omega", "Recursos renováveis e meio ambiente", "Telefone: (+55) 11 32549810","e-mail: contato@omegaenergia.com.br", "http://www.omegaenergia.com.br"),
         ("CGN Brazil Energy","atua no desenvolvimento, implantação e operação de projetos de energia renovável.", "Telefone: (+55) 41 3079-7100", "e-mail: contato@atlanticenergias.com.br", "http://atlanticenergias.com.br/"),
         ("Sunew","Fabricação de Painéis fotovoltaicos orgânicos no Brasil", "Telefone: ", "e-mail: contato@sunew.com.br","https://sunew.com.br/?gclid=CjwKCAjwyo36BRAXEiwA24CwGZvMrIASP0lNr4obOJ_0zIvyGhRzD0Mo-RGzGi8Sqk3bApE-KvmrVxoC_IcQAvD_BwE"),
         ("BYD", "Empresa de venda de painíes fotovoltaicos e soluções utilizando energia limpa", "Telefone: (+55) 19 3514-2550", "site de contato: http://www.byd.ind.br/contato/", "http://www.byd.ind.br/"),

cursor.executemany(com_sql, valor)

database.commit()

print(cursor.rowcount, "inserida com sucesso")
