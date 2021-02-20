import requests

# response = requests.get('https://galileoguzman.com')
response = requests.get('https://api.github.com/users/frasgado')

print(response.content)
# resultado de la peticion o de la respuesta
# 404 contenido no disponible
print(response.status_code)
print('-------------------------------------')
response = requests.get('https://avatars.githubusercontent.com/u/190476?v=4pip ')
print(response.content)
print(response.status_code)