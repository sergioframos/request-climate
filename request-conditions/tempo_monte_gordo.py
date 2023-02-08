from bs4 import BeautifulSoup
import requests
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

url = 'https://www.google.com.br/search?q=temperatura+monte+gordo+&ei=KC-yY6zGCdXa1sQPlZSt0Ag&ved=0ahUKEwis-rmA2qf8AhVVrZUCHRVKC4oQ4dUDCBA&uact=5&oq=temperatura+monte+gordo+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgAEEM6CwguEIAEELEDEIMBOgoIABCxAxCDARBDOggIABCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwgAEIAEELEDEIMBOggIABCABBCxAzoQCC4QsQMQgwEQxwEQ0QMQQzoHCAAQsQMQQzoOCAAQgAQQsQMQgwEQyQM6BQgAELEDOgkIABBDEEYQgAI6CAguELEDEIMBOhAIABCABBCxAxCDARDJAxAKOgcIABCABBAKOg0ILhCABBCxAxCDARAKOg0IABCABBCxAxCDARAKOgoIABCABBCxAxAKOgsIABAWEB4Q8QQQCjoKCAAQgAQQRhCAAjoLCC4QgwEQsQMQgAQ6BAgAEANKBAhBGABKBAhGGABQAFiWWGCzX2gJcAF4AIABkAKIAaUikgEGMC4yNy4xmAEAoAEBwAEB&sclient=gws-wiz-serp'

page = requests.get(url, headers=headers)
atributos_0 = {'id': 'wob_tm'}
atributos_1 = {'id': 'wob_pp'}
atributos_2 = {'id': 'wob_hm'}
atributos_3 = {'id': 'wob_ws'}

soup = BeautifulSoup(page.content, 'html.parser')

print("CLIMATE CONDITIONS IN MONTE GORDO: ")
print("Date: ", datetime.date.today())
temperature = soup.find("span", attrs=atributos_0).get_text()
print("Temperatura: ", temperature, "Graus Celsius")
rain = soup.find("span", attrs=atributos_1).get_text()
print("Probabilidade de Chuva: ", rain)
humidity = soup.find("span", attrs=atributos_2).get_text()
print("Umidade do Ar: ", humidity)
wind = soup.find("span", attrs=atributos_3).get_text()
print("Ventos: ", wind)
