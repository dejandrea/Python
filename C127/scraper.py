from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome(
    "D:\Documentos\BYJUS\AulasVScode\Aulas\Alunos\Aluno 0\Python\C127\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Defina o método de coleta de dados dos exoplanetas


def scrape():

    for i in range(0, 10):
        print(f'Coletando dados da página {i+1} ...')

        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # page_source obtem o código da pagina html
        # html.parser extrai o conteúdo das tags html

        

        # Loop para encontrar o elemento dentro das tags ul e li
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")

            temp_list = []

            for index, li_tag in enumerate(li_tags):
              # enumerate retorna o índice junto com o elemento

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

        # XML ==> Linguagem de marcação extensível

        # Encontre todos os elementos na página e clique para passar para a próxima página
        # //*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    print(planets_data[1])


# Chamando o método
scrape()

# Defina o cabeçalho
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

#dataframe armazena dados no formato tabular
# Defina o dataframe do pandas
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Converta para CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")