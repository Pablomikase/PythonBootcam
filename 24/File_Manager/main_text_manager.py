#Escribir de manera clasica
#file = open("my_file.txt")
#content = file.read()
#print(content)
#file.close()

#Lectura de manera correcta
#with open("my_file.txt") as file:
#    content = file.read()
#    print(content)


#Escritura
#with open("my_file.txt", mode="a") as file:
#    file.write("\nText enviado desde codigo")

#Creación de un nuevo fichero
with open("This_is_my_new_file", mode="w") as file:
    file.write("\nTexto por default :S")