#### Comienzo 8/04/2024
#### 28/07/2024

def menu():
    
    opcion = str(input('''Tips Menu ☺ Bob Ross:
    \t 1| Learn to draw
    \t 2| Phrase
    \t 3| Exit 
    \t 4| 2 Textos.
Select: '''))

    if opcion == "1":
        print("'how to draw better' \n the artist: drawing")
    elif opcion == "2":
        print("We don't make mistakes, just happy accidents and we learn to work with them.")
    elif opcion =="3":
        exit

    elif opcion == "4":
        a = input("text_1:   ")
        b = input("text_2:   ")
   
        
        menu()
    else:
        menu()
        print("Dato invalido")
    return  opcion

menu()


# C:\Users\OPTIPLEX\docs\py_practica
# py home.py <Run Terminal >
