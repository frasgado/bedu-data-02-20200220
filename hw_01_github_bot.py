'''
Ask for a username and download his/her avatar image
'''

import requests

BASE_URL = 'https://api.github.com/'

username = input('Give me a github username:\t')
endpoint_url = BASE_URL + f'users/{username}'

print(endpoint_url)
response = requests.get(endpoint_url)


def download_file(url_file):
    '''
    Name: download_file
    Params: url_file -> String
    Returns: None or image file
    '''
    response = requests.get(url_file)
    if response.status_code != 200:
        return None
    # Obtener el contenido de la respuesta y guardarlo en un archivo
    response_content = response.content # Store response content to be save later 
    # filename = f'tmp/usuario.png'
    filename = + f'tmp/{username}.png'
    # Crear contexto con With

    with open(filename, 'wb') as image:
        image.write(response_content)
        return image

# download_file('https://avatars.githubusercontent.com/u/2016072?v=4')
# download_file('https://avatars.githubusercontent.com/u/190476?v=4')
user = response.json() # From json to python Dict
ruta = user['avatar_url']
download_file(ruta)
