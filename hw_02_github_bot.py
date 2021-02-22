'''
- Ask for a list of github usernames and download their avatar images
input('Users:')
galileoguzman, frasgado, eduardo_luna, ....
'''

import requests

BASE_URL = 'https://api.github.com/'

users = input('Give me a users list separated with comma (,):\n')

usuarios = users.split(sep=',')
print(usuarios)
type(usuarios)

def download_file(url_file):
    '''
    Name: download_file
    Params: url_file -> String
    Returns: None or image file
    '''
    #print(url_file)
    response = requests.get(url_file)
    print(response.status_code)
    if response.status_code != 200:
        return None
    # Obtener el contenido de la respuesta y guardarlo en un archivo
    #print(response.content)
    response_content = response.content # Store response content to be save later 
    # filename = f'tmp/usuario.png'
    filename = f'tmp/{username}.png'
    #print(f'filename={filename}')
    # Crear contexto con With
    with open(filename, 'wb') as image:
        image.write(response_content)
        return image

for i in usuarios:
    print('------------------------------------------------------------')
    print(i)
    username = i.strip()
    if username:
        endpoint_url = BASE_URL + f'users/{username}'
        print(endpoint_url)
        response = requests.get(endpoint_url)

        # download_file('https://avatars.githubusercontent.com/u/2016072?v=4')
        # download_file('https://avatars.githubusercontent.com/u/190476?v=4')
        user = response.json() # From json to python Dict
        ruta = user['avatar_url']
        print(f'ruta={ruta}')
        #print(f'endpoint_url={endpoint_url}')
        download_file(ruta)
