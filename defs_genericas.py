def verifica_numero(msg,msg_erro):
   numero = input(msg)
   while not numero.isnumeric():
       print(msg_erro)
       numero = input(msg)
   numero = int(numero)
   return numero

def forca_opcao(msg,lista_opcoes, msg_erro):
   opcao = input(msg)
   while not meu_in(lista_opcoes,opcao, ):
       print(msg_erro)
       opcao = input(msg)
   return opcao

def meu_in(lista, buscar):
   for i in range(len(lista)):
       elem = lista[i]
       if elem == buscar:
           return True
   return False

def meu_index(lista, buscar):
   for i in range(len(lista)):
       elem = lista[i]
       if elem == buscar:
           return i
   return False
