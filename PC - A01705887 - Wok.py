"""
Este es un archivo python para el proyecto de pensamiento computacional
A01705887
Se pretende seguir el pseudocódigo una vez aprendidos los fundamentos
"""


#Se le pide su usuario y contraseña al cliente.
user = input("Usuario: ")
password = input("Contraseña: ")
print("")

#Se definen los valores de precio para los woks tanto sencillos como preparados.
#Además se pone el valor de las bebidas que nos ayudará a sacar el precio total al final.
sencillo = 85
preparado = 94
agua = 10
refresco = 20

#Se le da la bienvenida al usuario, usando el input que nos dió previamente en usuario.
print("Bienvenido a la aplicación de Wok", user)
print("")

#Se le invita al cliente a ordenar un Wok y basado en su decisión se le mandan distintas opciones.
print("¿Usted desea ordenar un Wok?")

#Se define la función goodday para usarla cuando el usuario haya terminado su compra o no quiera comprar en ese momento.
#Es parte de una despedida predeterminada de la interfaz.
def goodday():
     print("¡Qué tengas un buen día!")
     return goodday


#Se define la función contenido_prep para simplificar el proceso de mostrar los ingredientes de los Woks preparados.
def contenido_prep():
    fusionwok = ["tallarín", "queso", "espinaca", "carne de res", "3 quesos", "chipotle"]
    mexicanhc = ["penne", "mozarella", "zanahoria", "elote", "carne de res", "jalapeño"]
    italianwok = ["spaghetti", "aceituna", "mozarella", "carne de res", "pepperoni", "boloñesa"]
    chickenteriyaki = ["noddles", "zanahoria", "calabaza", "ejote", "cebolla", "pollo", "salsa teriyaki"]

    print("Los ingredientes del Fusion Wok son:")
#A lo largo de este y la próxima función se muestran ciclos for que se usaron para imprimir las listas.
    for x in fusionwok:
        print("-", x)
#Se agregó el carácter "-" para que a la hora de mostrar los ingredientes se vea más entendible.

#Se tomó la decisión de usar estos prints para que el código no se vea tan junto a la hora de ejecutarlo.
    print("")

    print("Los ingredientes del Mexican Hot Cheese son:")
    for x in mexicanhc:
        print("-", x)

    print("")

    print("Los ingredientes del Italian Wok son:")
    for x in italianwok:
        print("-", x)

    print("")

    print("Los ingredientes del Chicken Teriyaki son:")
    for x in chickenteriyaki:
        print("-", x)

#Se define la función contenido_senc para facilitar el proceso de ordenar un Wok sencillo.
#En esta función hay ciclos tanto while como for que permiten juntar en una lista final de ingredientes los valores dados por el usuario.
#Asimismo, la impresión de ingredientes y selección es mucho más cómoda.
def contenido_senc():
    print("")
    pastas = ["1 - tallarines", "2 - noddles", "3 - arroz", "4 - penne"]
    prot = ["1 - carne", "2 - pollo", "3 - tofu", "4 - porción doble + 15", "5 - queso gratinado"]
    vegetales = ["1 - zanahoria", "2 - ejote", "3 - calabaza", "4 - col morada", "5 - papa", "6 - espinaca", "7 - cebolla", "8 - elote", "9 - piña", "10 - aceitunas", "11 - germinado"]
    salsas = ["1 - jalapeño", "2 - chipotle", "3 - 3 quesos", "4 - teriyaki", "5 - boloñesa", "6 - finas hierbas", "7 - buffalo"]

    for x in pastas:
        print(x)

#Se crean distintas variables para que todas las selecciones del usuario se vean reflejadas en la lista final.
    opc_pasta = int(input("Selecciona el número de pasta: "))
    print(f"Usted ha seleccionado la opción {opc_pasta}")
    pasta_seleccionada = pastas[opc_pasta - 1]

    lista_final = []

#Se usa repetidas veces el comando .append para ir agregando valores a una lista vacía.
    lista_final.append(pasta_seleccionada)

#Se usan algunas variables con booleanos, ya que a la hora de usar el ciclo while, permiten detener el mismo.
    solcarne = True
    contcarne = 0

    print("")

    for x in prot:
        print(x)

    print("")

    while solcarne:
        print("Escoge 3 carnes o extras como máximo, pero si solo quieres una, selecciona 10 después de la primera")
        opc_carne = int(input("Selecciona el tipo de carne: "))
        if opc_carne == 10:
            break
        print(f"Usted ha seleccionado la opción {opc_carne}")
        carne_seleccionada = prot[opc_carne - 1]
        lista_final.append(carne_seleccionada)
        contcarne += 1

        if contcarne == 3:
            print("Has seleccionado el máximo de carne y extras")
            solcarne = False
            break

    print("")

    solveg = True
    contveg = 0

    for x in vegetales:
        print(x)
        
    print("")

    while solveg:
        print("Escoge como máximo 9 vegetales, cuando quieras parar entonces selecciona 20")
        opc_veg = int(input("Selecciona los vegetales: "))
        if opc_veg == 20:
            break
        print(f"Usted ha seleccionado la opción {opc_veg}")
        vegetales_seleccionados = vegetales[opc_veg - 1]
        lista_final.append(vegetales_seleccionados)
        contveg += 1

        if contveg == 9:
            print("Has seleccionado el máximo de vegetales")
            solveg = False
            break

    print("")
    solsal = True
    contsal = 0

    for x in salsas:
        print(x)
        
    print("")

    while solsal:
        print("Escoge la salsa que más te guste, si deseas omitir entonces presiona 10")
        opc_sal = int(input("Selecciona tu salsa: "))
        if opc_sal == 10:
            break
        print(f"Usted ha seleccionado la opción {opc_sal}")
        salsa_seleccionada = salsas[opc_sal - 1]
        lista_final.append(salsa_seleccionada)
        contsal += 1

        if contsal == 1:
            solveg = False
            break

    print("")
    print(f"Tu wok contendrá los siguientes ingredientes: {lista_final}")


#Se define la función cuenta total que nos ayudará a que el usuario sepa cuánto dinero debe pagar.
def cuentatotal ():
    print("")
    print("Selecciona lo que pediste para poder calcular el precio")
    print("Sencillo - 1")
    print("Preparado - 2")
    print("Sin bebida - 0")
    print("Agua - 1")
    print("Refresco - 2")
    print("")
    
#Se separan las bebidas y los Woks para poder imprimir mensajes distintos con el precio.
    artfinal = int(input("Wok sencillo o preparado: "))
    if artfinal == 1:
        print("Son 85 pesos")
        print("")
    elif artfinal == 2:
        print("Son 94 pesos")
        print("")
    else:
        print("Selecciona por favor lo que ordenaste")

    bebida = int(input("Agua, refresco o sin bebida: "))
    if bebida == 0:
        print("No ordenaste bebida")
        print("")
    if bebida == 1:
        print("Son 10 pesos")
        print("")
    if bebida == 2:
        print("")
        print("Son 20 pesos")
        print("")

#Se define la función retro, que nos ayudará a ejecutar la parte de retroalimentación del programa.
#En esta función se utiliza la condición y los operadores lógicos para darle el mejor mensaje posible al usuario, según su puntuación.
def retro():
    print("")
    print("Nos gustaría saber tu opinión de la app")
    valordecomida = int(input("Del 1 al 100 que tan bueno es Wok: "))
    if valordecomida <=20 and valordecomida >=0:
        print("Lo sentimos, sería bueno si puedes ir a la sucursal a informarnos cual fue el problema")
    elif valordecomida <=60 and valordecomida >=21:
        problema = str(input("Escribe brevemente cuál fue el problema: "))
    elif valordecomida <=85 and valordecomida >=61:
        print("Trabajamos constantemente en mejorar, esperamos volverte a ver")
    elif valordecomida <=100 and valordecomida >=86:
        print("Nos hace felices saber que tu Wok te gustó, ¡vuelve pronto!")
    else:
        print("No podemos comprender tu calificación")
        return retro
     
#Se define la función elegir, ya que por medio de esta elección de condicionales, ciclos y funciones podremos saber lo que el usuario quiere.
#Se le muestran varias opciones y mediante el uso de números enteros el usuario selecciona lo que desea.
#En los condicionales se usa el doble igual para indicar que si el valor es "tal", se debe ejecutar cierta acción.
#Adicionalmente, se crean variables como: select, wokprep y tipowok para facilitar el proceso.
def elegir():
    select = int(input("A continuación escoge 1 para seguir y 2 para salir: "))
    if select == 1:
        print("")
        print("Redireccionando a la página de selección")
        print("")
        print(". . .")
        print("")
        print("SELECCIONA EL TIPO DE WOK QUE DESEAS")
        print("")
        tipowok = int(input("Presiona 1 para sencillo y 2 para preparado: "))
        if tipowok == 1:
            print("Haz seleccionado un wok sencillo")
            contenido_senc()
            retro()
            cuentatotal()
            goodday()
            
        elif tipowok == 2:
            print("")
            print("Haz seleccionado un wok preparado")
            print("")
            print("Estas son las opciones")

            print("")
            contenido_prep()
            print("")

            print("Selecciona el que deseas:")
            print("Fusion Wok - 1")
            print("MHC Wok - 2")
            print("Italian Wok - 3")
            print("Chicken Teriyaki - 4")
            print("")

            wokprep = int(input("Ingresa el número de tu wok: "))
            if wokprep == 1:
                print("Usted ha escogido un Fusion Wok")
            elif wokprep == 2:
                print("Usted ha escogido un Mexican Hot Cheese Wok")
            elif wokprep == 3:
                print("Usted ha escogido un Italian Wok")
            elif wokprep == 4:
                print("Usted ha escogido un Chicken Teriyaki Wok")
            else:
                print("Seleccione un tipo de Wok o vuelva al menú principal")
            
            retro()     
            cuentatotal()
            goodday()
            
    elif select == 2:
        print("")
        print("Esperamos se te antoje un Wok pronto")
        goodday()
    else:
        print("Por favor elige entre 1 y 2")

elegir()

num = int(input("Elige 1 para volver a pedir y 2 para salir: "))

#Se usa un ciclo while para permitirle al usuario pedir otro Wok.
#Asimismo, se le da la opción de terminar su orden.
while num == 1 :
    elegir()
    num = int(input("Elige 1 para volver a pedir y 2 para salir: "))
#Se apoya de un condicional para insertar un break y romper con el ciclo.
    if num == 2 :
#Se utiliza un break para romper el ciclo cuando se selecciona 2.
        break

print("")
print("Gracias por tu preferencia, espera próximas noticias")
print("La aplicación de Wok sigue en desarrollo")

#¡Se ha avanzado de una manera considerable, sin embargo, siempre se puede mejorar! (:
#El programa ya casi está listo :D
