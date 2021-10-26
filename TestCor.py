import os
import pathlib
#Hago un bucle en el que pido las palabras  
words = []
while True: 
    newWord = input(" Enter new word (To finish enter Q): ")
    if newWord != 'Q' : 
        words.append(newWord) 
    else:
        break

newList = [] 
availableWords = True

#recorro la lista 'words'
while words: 
    if availableWords is False: 
        break
    #obtengo la primera palabra de la lista y obtengo la ultima letra, si hay mas palabras guardadas, obtengo la ultima letra de la ultima palabra guardada
    if newList == []:
        newList.append(words[0])
        lastLetter = words[0][-1]
        words.pop(0)
    else: 
        lastLetter = newList[-1][-1]   

    #recorro la lista 'words' en busca de una palabra que pueda unir, si no encuentro, se vuelve una lista no viable
    for j in range(len(words)):  
        if words[j][0] == lastLetter: 
            newList.append(words[j]) 
            words.pop(j)
            break
        elif words[j] == words[-1] and words[j][0] != lastLetter:
            availableWords = False
            break

if availableWords  is False: 
    print("No se puede encadenar todas las palabras")
    print("Encadenadas: ", newList)
    print("Faltantes: ", words)
else: 
    #obtengo ruta en la que ejecuto el .py 
    path = os.path.abspath(os.getcwd())
    #creo el archivo txt en la ruta en la que ejecuto el .py 
    file = open(path  + '\palabras.txt', "w")
    for word in newList:  
        file.write(word + "\n")  
    file.close()
    print("Archivo creado en ruta: ", path)



    
