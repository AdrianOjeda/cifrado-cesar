file = open('song.txt', 'r') #abrimos el archivo que contiene la letra, en modo lectura

character = file.read(1)#empezamos a leer el archivo caracter por caracter

List = [] #declaramos una lista vacia que contendra los caracteres sin cifrar
ListCiphered = [] #una segunda lista donde guardaremos los caracteres cifrados
contador = 0 #inicializamos una variable contador iniciando desde 0

while character != "": #ciclo while que recorre el archivo original hasta que se llegue a su fin
    List.append(character) #almacenamos el caracter en la lista
    character = file.read(1)
    asciichar = ord(List[contador]) #convertimos el caracter en su forma ascii
    if(asciichar >= 97 and asciichar <= 122): #evaluamos si es una letra minuscula
        if(asciichar == 122): #evaluamos si es z
            asciichar = 97
            letra = chr(asciichar) #reconvertimos el ascii a caracter
            ListCiphered.append(letra) #almacenamos en la lista cifrada
        else:
            asciichar = asciichar+1 #sumamos 1 al ascii para cambiar a la letra que le sigue
            letra = chr(asciichar)
            ListCiphered.append(letra)
    else:
        letra = chr(asciichar)# si es mayuscula o simbnolo, no se hace nada
        ListCiphered.append(letra)#append a la lista cifrada
    contador = contador + 1 #incrementamos el contador para pasar al siguiente caracter

print("".join(ListCiphered))#imprimimos la letra cifrada
file.close()#cerramos el archivo