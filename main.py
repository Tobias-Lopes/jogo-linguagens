import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url) 
data = resposta.json()
len(data)
valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica_secreta = valor_secreto['dica']
chute = input (f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica_secreta}')
if chute == palavra_secreta:
  print ('acertou')
else:
  print (f'errou, a palavra era {palavra_secreta}')
