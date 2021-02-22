import csv

from github_user_function import get_user

print(get_user('galileoguzman'))

# Definir las columnas que va a tener tu archivo

COLUMNS = []

COLUMNS = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'name', 'company', 'blog', 'location', 'email', 'hireable', 'bio', 'twitter_username', 'public_repos', 'public_gists', 'followers', 'following', 'created_at', 'updated_at',]

# DEFINIR EL ARCHIVO DONDE SE VA A GUARDAR
FILENAME = 'tmp/user_github.csv'

# SALVAR EL DICCIONARIO
user = get_user('galileoguzman')

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
    writer.writerow(user)



'''
"login": "frasgado",
  "id": 190476,
  "node_id": "MDQ6VXNlcjE5MDQ3Ng==",
  "avatar_url": "https://avatars.githubusercontent.com/u/190476?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/frasgado",
  "html_url": "https://github.com/frasgado",
  "followers_url": "https://api.github.com/users/frasgado/followers",
  "following_url": "https://api.github.com/users/frasgado/following{/other_user}",
  "gists_url": "https://api.github.com/users/frasgado/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/frasgado/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/frasgado/subscriptions",
  "organizations_url": "https://api.github.com/users/frasgado/orgs",
  "repos_url": "https://api.github.com/users/frasgado/repos",
  "events_url": "https://api.github.com/users/frasgado/events{/privacy}",
  "received_events_url": "https://api.github.com/users/frasgado/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": "Analista y Programador",
  "twitter_username": null,
  "public_repos": 6,
  "public_gists": 0,
  "followers": 2,
  "following": 6,
  "created_at": "2010-01-26T22:14:03Z",
  "updated_at": "2021-01-13T04:32:02Z"
  '''