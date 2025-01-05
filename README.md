Lista de Exercicios do Curso em Video

Feito por Henrique Flávio Guimarães

Install(libs)

'''random, math, pygame'''

ANOTAÇÕES:

-~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-

  int()  --> Para números inteiros ------------ 17, 21, 35, 42

  float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

  bool() --> Armazena True ou False --------True, False

  str() ----> Conjunto de caracteres -------- 'narigudo', 'Pedro', 'feioso'

  type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

  + -> Adição              ** -> Potencia
  - -> Subtração           // -> Divisão inteira
  * -> Multiplicação        % -> Resto da divisão
  / > Divisão -


           Ordem de Precedência

  1° -> ()
  2° -> **
  3° -> *  /  //  %
  4° -> +  -

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


~-~-~-~-~-~-~--~-~-~ Módulos -~-~-~-~-~-~-~-~-~-~-~

  Import > Importa uma biblioteca - import math

  from math import cos -> Importa somente a funçao cos da biblioteca math

  math -> Biblioteca de operadores aritméticos {

     sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
     floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
     ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
     hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
     radians()-> Converte em graus radianos ---------- print(math.radians(180))
     cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
     tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))
  }

  random -> Gerar numeros pseudoaleatorios {

      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
  }
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-
  
  frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

  frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
  frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
  frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA
  len() -------------> Mostra quantas letras tem a frase -------------------------------- len(frase) = 38 letras
  count() ---------> Conta quantas vezes aparece a letra escolhida e tambem obtém o número de ocorrências de um elemento dentro da lista ----------- frase.count('s')
  find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')
  replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript')
  upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
  lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
  capilalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
  title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
  strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
  split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
  .join() -----------> Juntar uma coisa com a outra -------------------------------------- '-'.join.frase Estou-aprendendo-a-programar-em-python

  .insert()---------> Insere um elemento novo na lista em um indice expecifico ---> lista_compras.insert(4, "melão")
  del -----> a sentença del elimina um elemento da lista ----> : del lista_compras[1]
  .append ------> o método append acrescenta um elemento ao final de lista (é só informar qual elemento que deve ser adicionado ao final da lista) --> lista_compras.append("mel")
  .sort -----------> método para colocar em ordem crescente os elementos da lista -------> lista_compras.sort()
  .reverse --------> método que inverte a posição de todos os elementos -------> lista_compras.reverse()
  .index ---------------> obtém o índice da primeira ocorrência do elemento dentro da lista ----> lista.index(44)
  min() -----------------> retorna o elemento com o menor valor da lista ----------> min(lista)
  max() ------------------> retorna o elemento com o maior valor da lista ---------> max(lista)
  sum() ------------------> retorna a soma dos elementos da lista --------> sum(lista)
      – Quando aplicados a uma string, as funções min e max determinam o menor e
        o maior elemento de acordo com a posição do elemento dentro da ordem alfabética
      – A função sum não se aplica a strings
  
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
*CORES NO TERMINAL*
text                    background
 
30   black       preto      40
31   red         vermelho   41
32   green       verde      42
33    yellow     amarelo    43
34    blue       azul       44
35    Magenta    Magenta    45
36    cyan       ciano      46
37    grey       cinza      47
97    white      branco     107

Lista de Exercicios do Curso em Video

Feito por Henrique Flávio Guimarães

Install(libs)

'''random, math, pygame'''

ANOTAÇÕES:

-~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-

  int()  --> Para números inteiros ------------ 17, 21, 35, 42

  float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

  bool() --> Armazena True ou False --------True, False

  str() ----> Conjunto de caracteres -------- 'narigudo', 'Pedro', 'feioso'

  type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

  + -> Adição              ** -> Potencia
  - -> Subtração           // -> Divisão inteira
  * -> Multiplicação        % -> Resto da divisão
  / > Divisão -


           Ordem de Precedência

  1° -> ()
  2° -> **
  3° -> *  /  //  %
  4° -> +  -

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


~-~-~-~-~-~-~--~-~-~ Módulos -~-~-~-~-~-~-~-~-~-~-~

  Import > Importa uma biblioteca - import math

  from math import cos -> Importa somente a funçao cos da biblioteca math

  math -> Biblioteca de operadores aritméticos {

     sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
     floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
     ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
     hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
     radians()-> Converte em graus radianos ---------- print(math.radians(180))
     cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
     tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))
  }

  random -> Gerar numeros pseudoaleatorios {

      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
  }
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-
  
  frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

  frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
  frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
  frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA
  len() -------------> Mostra quantas letras tem a frase -------------------------------- len(frase) = 38 letras
  count() ---------> Conta quantas vezes aparece a letra escolhida e tambem obtém o número de ocorrências de um elemento dentro da lista ----------- frase.count('s')
  find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')
  replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript')
  upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
  lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
  capilalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
  title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
  strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
  split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
  .join() -----------> Juntar uma coisa com a outra -------------------------------------- '-'.join.frase Estou-aprendendo-a-programar-em-python

  .insert()---------> Insere um elemento novo na lista em um indice expecifico ---> lista_compras.insert(4, "melão")
  del -----> a sentença del elimina um elemento da lista ----> : del lista_compras[1]
  .append ------> o método append acrescenta um elemento ao final de lista (é só informar qual elemento que deve ser adicionado ao final da lista) --> lista_compras.append("mel")
  .sort -----------> método para colocar em ordem crescente os elementos da lista -------> lista_compras.sort()
  .reverse --------> método que inverte a posição de todos os elementos -------> lista_compras.reverse()
  .index ---------------> obtém o índice da primeira ocorrência do elemento dentro da lista ----> lista.index(44)
  min() -----------------> retorna o elemento com o menor valor da lista ----------> min(lista)
  max() ------------------> retorna o elemento com o maior valor da lista ---------> max(lista)
  sum() ------------------> retorna a soma dos elementos da lista --------> sum(lista)
      – Quando aplicados a uma string, as funções min e max determinam o menor e
        o maior elemento de acordo com a posição do elemento dentro da ordem alfabética
      – A função sum não se aplica a strings
  
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
*CORES NO TERMINAL*
text                    background
 
30   black       preto      40
31   red         vermelho   41
32   green       verde      42
33    yellow     amarelo    43
34    blue       azul       44
35    Magenta    Magenta    45
36    cyan       ciano      46
37    grey       cinza      47
97    white      branco     107

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
print(f'{variavel:b}')

a opção :b dentro das {} exibe o valor da variável num já convertido em binário, sem o 0b no início.

:b - binário
:o - octal
:x - hexadecimal com letras minúsculas
:X - hexadecimal com letras maiúsculas


