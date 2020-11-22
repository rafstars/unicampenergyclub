import csv
import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.canalsolar.com.br/noticias").content
soup = BeautifulSoup(html,"html.parser")
csv_file = open("canal_solar.csv","x")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Titulo", "Link"])# não coloquei resumo porque no canal solar não tem o subtitulo nas noticias

for catItemHeader in soup.find_all("div",class_="catItemHeader"):
        titulo= catItemHeader.h3.a.text
        print(titulo)
        link = catItemHeader.h3.a["href"]
        link_canal_solar = f"https://www.canalsolar.com.br{link}"
        print(link_canal_solar)
        csv_writer.writerow([titulo,link_canal_solar])
csv_file.close()