'''
hw_03_csv_gtihub.py

- Given a github username extrac all his/her folowers and store them into a CSV File
1. Consulto los followers del usuario github que se proporciona. 
2. Por cada respuesta satisfactoria guardarlo en un row.

https://api.github.com/users/{user}/followers

'''
import csv

from github_user_function import get_user_with_followers
from github_user_function import get_user


#BASE_URL = 'https://api.github.com/'

username = input('Give me a github username:\t')
PER_PAGE = 100
page = 1
#endpoint_url = BASE_URL + f'users/{username}/followers'


# Definir las columnas que va a tener tu archivo

COLUMNS = []

COLUMNS = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin']

# DEFINIR EL ARCHIVO DONDE SE VA A GUARDAR
FILENAME = f'tmp/{username}_github.csv'
# SALVAR EL DICCIONARIO

user = get_user(username)
print('.................................................')
print(user)
print('.................................................')
print(f"Número de seguidores: {user['followers']}")
followers = user['followers']
num_pages = followers//PER_PAGE
print(f'Numero de páginas:{num_pages}')
faltantes = followers%PER_PAGE
print(f'Faltantes:{faltantes}')
if faltantes > 0:
    num_pages += 1
print('.................................................')
print(f'Numero de páginas considerando residuos: {num_pages}')
print('.................................................')


# CREAR UN CONTEXTO

# Descarga en formato de diccionario
# Opening file in writable mode
with open(FILENAME, mode='w', newline='') as csv_file:
    # crear un descriptor que se llame writer
    writer = csv.DictWriter(csv_file, fieldnames = COLUMNS)

    # Write columns
    # mandar a llamar al descritor
    writer.writeheader()

    # Escribit el diccionario en el archivo
    # Escribir cada una de las columnas que deseemos
    # Write at least ONE ROW
    for nu_pagina in range(1, num_pages+1):
        print(f'Obteniendo página No: {nu_pagina} de {num_pages}')
        followers = get_user_with_followers(username, 'followers', nu_pagina)
        for i in followers:
            writer.writerow(i)

print(f'Se han obtenido todos los followers de {username}')

'''
    "login": "KevinHock",
    "id": 3076393,
    "node_id": "MDQ6VXNlcjMwNzYzOTM=",
    "avatar_url": "https://avatars.githubusercontent.com/u/3076393?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/KevinHock",
    "html_url": "https://github.com/KevinHock",
    "followers_url": "https://api.github.com/users/KevinHock/followers",
    "following_url": "https://api.github.com/users/KevinHock/following{/other_user}",
    "gists_url": "https://api.github.com/users/KevinHock/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/KevinHock/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/KevinHock/subscriptions",
    "organizations_url": "https://api.github.com/users/KevinHock/orgs",
    "repos_url": "https://api.github.com/users/KevinHock/repos",
    "events_url": "https://api.github.com/users/KevinHock/events{/privacy}",
    "received_events_url": "https://api.github.com/users/KevinHock/received_events",
    "type": "User",
    "site_admin": false
'''