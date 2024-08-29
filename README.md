# jogo-linguagens
Jogo de adivinhar qual é a linguagem de programação, pela descrição.

<div align='center'>
    <img src='https://www.superti360.com.br/wp-content/uploads/2022/02/0-destaque-linguagens-de-programacao-2019.jpg' title='Linguagens' width='340px' />
</div> 

## Como funciona?

Nesse jogo a pessoa irá receber a descrição de uma linguagem de programação e deve acertar qual é a linguagem.
## Start
```
$ python main.py
```

ou crie seu próprio arquivo com o seguinte script, e depois siga o procedimento acima com o nome correspondente:
```Python
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
```
## Guia para estudar antes de jogar:
```
JAVA SCRIPT (JS)
-> Desenvolvimento Web cliente/servidor
-> Aplicação de navegador 

PYTHON 
-> Ciência de dados e atomação 
-> Inteligência artificial 

JAVA
-> Desenvolvimento de androide 
-> Aplicativos desktops empresariais de larga escala
-> Desenvolvimentos de aplicativos diversificados

C#
-> Desenvolvimento de plataformas Microsoft 
-> Desenvolvimento Windows 
-> Desenvolvimento Gamer

PHP
-> Desenvolvimento de sites dinâmicos com aplicações Web

TYPE SCRIPT (TS)
-> Extenção do JS que adiciona tipagem estática, facilitando desenvolvimento de grandes projetos

C++ 
-> Sistemas embarcados
-> Jogos
-> Desenvolvimento de software 
-> Linguagem mais flexível 

C
-> Sistemas operacionais
-> Drivers de hardware
-> Desenvolvimento de software de nível baixo

SWIFT e KOTLIN
-> Desenvolvimento de aplicativos mobile (Swift pro IOS e Kotlin pro Androide)
-> Kotlin é projetado para ser executado na plataforma Java e pode ser compilado em Bytecode java
```