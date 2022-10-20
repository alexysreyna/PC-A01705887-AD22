"""
Este es un archivo python para el proyecto de pensamiento computacional
A01705887
"""

#Se le pide su usuario y contraseña al cliente.
user = input("Usuario: ")
password = input("Contraseña: ")

#Se definen los valores de precio para los woks tanto sencillos como preparados.
#Se utiliza una matriz para poder imprimir fácilmente una tabla de precios.
matrizprecios = [["sencillo", 85], ["preparado", 94], ["agua", 10], ["refresco", 20]]

#Se le da la bienvenida al cliente, usando el input que nos dió previamente en usuario.
print(f"\nBienvenido a la aplicación de Wok {user} \n")


#Por medio de un ciclo for y la matriz se muestra el menú.
print("A continuación están nuestros precios:")
for articulo in matrizprecios:
    print(articulo)
    
#Se le invita al cliente a ordenar un Wok y basado en su decisión se le mandan distintas opciones.
print("\n¿Usted desea ordenar un Wok?")

#Se define la función goodday para usarla cuando el usuario haya terminado su compra o no quiera comprar en ese momento.
#Es parte de una despedida predeterminada de la interfaz.
def goodday():
     print("\n¡Qué tengas un buen día!")


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
#También se usa "\n" en ciertos momentos para que el programa tenga espaciados coherentes.
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
#Esta opción se usa en todas las selecciones de los Woks sencillos, para al final poder imprimir la lista de ingredientes seleccionados
    lista_final.append(pasta_seleccionada)

#Se usan algunas variables con booleanos, ya que a la hora de usar el ciclo while, permiten detener el mismo.
#El contador sirve en esta sección para que no se exceda el límite de carneso vegetales permitidos. 
    solcarne = True
    contcarne = 0

    print("")

    for x in prot:
        print(x)

    print("")

#Se le da la opción al usuario de dejar de escoger carnes al presionar 10.
#Esto se hace por si solamente busca una cantidad menor al máximo permitido.
    while solcarne:
        print("Escoge 3 carnes o extras como máximo, pero si solo quieres una o dos, selecciona 10 para saltar a la siguiente parte")
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

    print("")

#Al igual que en la sección de carnes, se establece un valor booleano para detener el ciclo.
#Y un contador que servirá para controlar el número máximo de vegetales.
    solveg = True
    contveg = 0

    for x in vegetales:
        print(x)
        
    print("")

    while solveg:
        print("Escoge como máximo 9 vegetales, cuando quieras parar entonces selecciona 20")
        opc_veg = int(input("Selecciona los vegetales: "))
#Para no elegir los 9 vegetales máximos, puedes presionar el 20 para continuar a la siguiente sección.
        if opc_veg == 20:
            break
        print(f"Usted ha seleccionado la opción {opc_veg}")
        vegetales_seleccionados = vegetales[opc_veg - 1]
        lista_final.append(vegetales_seleccionados)
        contveg += 1

        if contveg == 9:
            print("Has seleccionado el máximo de vegetales")
            solveg = False

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
            solsal = False

#Se imprime la lista con los elementos previamente agregados en los procesos anteriores.
    print(f"\nTu wok contendrá los siguientes ingredientes: {lista_final}")


#Se define la función cuenta total que nos ayudará a que el usuario sepa cuánto dinero debe pagar.
def cuentatotal ():
    sumafinal = 0
    print("\nSelecciona lo que pediste para poder calcular el precio")
    print("Sencillo - 1")
    print("Preparado - 2")
    print("Sin bebida - 0")
    print("Agua - 1")
    print("Refresco - 2\n")
    
#Se separan las bebidas y los Woks para poder imprimir mensajes distintos con el precio.
#A lo largo de esta sección se le pide al usuario seleccione la cantidad de artículos que compró.
#Por medio de operaciones aritméticas se suman a un total general.
    artfinal = int(input("Wok sencillo o preparado: "))
    while artfinal == 1 or 2:
        if artfinal == 1:
            print("Has seleccionado el artículo wok sencillo")
            print("El precio por Wok sencillo es de 85 pesos")
            cantidadart = int(input("¿Cuántos compraste?: "))
            sencfinal = 85*cantidadart
            sumafinal = sumafinal + sencfinal
            break
            
        elif artfinal == 2:
            print("Has seleccionado el artículo wok preparado")
            print("El precio por Wok preparado es de 94 pesos")
            cantidadart = int(input("¿Cuántos compraste?: "))
            prepfinal = 94*cantidadart
            sumafinal = sumafinal + prepfinal
            break

        else:
            print("Selecciona por favor lo que ordenaste")
            artfinal = int(input("Wok sencillo o preparado: "))
            break

    bebida = int(input("Agua, refresco o sin bebida: "))
    while bebida == 0 or 1 or 2:
        if bebida == 0:
            print("Has seleccionado no tomar alguna bebida")
            break
        
        elif bebida == 1:
            print("Has seleccionado una botella de agua")
            print("El precio por botella es de 10 pesos")
            cantidadart = int(input("¿Cuántas compraste?: "))
            aguasfinal = 10*cantidadart
            sumafinal = sumafinal + aguasfinal
            break
            
        elif bebida == 2:
            print("Has seleccionado un refresco")
            print("El precio es de 20 pesos")
            cantidadart = int(input("¿Cuántos compraste?: "))
            refrescosfinal = 20*cantidadart
            sumafinal = sumafinal + refrescosfinal
            break
            
        else:
            print("No seleccionaste una opción válida")
            bebida = int(input("Agua, refresco o sin bebida: "))
        
#Por medio del return guardamos el valor final de la cuenta para su impresión al final del código.
    return sumafinal


#Se define la función retro, que nos ayudará a ejecutar la parte de retroalimentación del programa.
#En esta función se utiliza la condición y los operadores lógicos para darle el mejor mensaje posible al usuario, según su puntuación.
def retro():
    print("\nNos gustaría saber tu opinión de la app")
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
        return problema
#Este return podría ser útil para guardar los diferentes comentarios que la gente puede llegar a tener acerca de la aplicación.
     


#Se define la función elegir, ya que por medio de esta elección de condicionales, ciclos y funciones podremos saber lo que el usuario quiere.
#Se le muestran varias opciones y mediante el uso de números enteros el usuario selecciona lo que desea.
#En los condicionales se usa el doble igual para indicar que si el valor es "tal", se debe ejecutar cierta acción.
#Adicionalmente, se crean variables como: select, wokprep y tipowok para facilitar el proceso.

#Es importante mencionar que se usan varios ciclos while para que cuando el usuario eliga una opción inválida ...
# ... el programa regrese a pedir las opciones válidas iniciales.

#De igual manera, es fundamental decir que varias funciones definidas previamente son usadas dentro de la función elegir.
def elegir():
    select = int(input("A continuación escoge 1 para seguir y 2 para salir: "))
    while select == 1 or 2:
        if select == 1:
            print("\nRedireccionando a la página de selección")
            print("\n. . .")
            print("\nSELECCIONA EL TIPO DE WOK QUE DESEAS\n")
            tipowok = int(input("Presiona 1 para sencillo y 2 para preparado: "))
            while tipowok == 1 or 2:
                if tipowok == 1:
                    print("Haz seleccionado un wok sencillo")
                    contenido_senc()
                    retro()                    
                    break
                    
                elif tipowok == 2:
                    print("\nHaz seleccionado un wok preparado")
                    print("\nEstas son las opciones\n")

                    contenido_prep()

                    print("\nSelecciona el que deseas:")
                    print("Fusion Wok - 1")
                    print("MHC Wok - 2")
                    print("Italian Wok - 3")
                    print("Chicken Teriyaki - 4\n")

                    wokprep = int(input("Ingresa el número de tu wok: "))
                    while wokprep == 1 or 2 or 3 or 4:
                        if wokprep == 1:
                            print("Usted ha escogido un Fusion Wok")
                            break
                        elif wokprep == 2:
                            print("Usted ha escogido un Mexican Hot Cheese Wok")
                            break
                        elif wokprep == 3:
                            print("Usted ha escogido un Italian Wok")
                            break
                        elif wokprep == 4:
                            print("Usted ha escogido un Chicken Teriyaki Wok")
                            break
                        else:
                            print("Seleccione un tipo de Wok o vuelva al menú principal")
                            wokprep = int(input("Ingresa el número de tu wok: "))

                    retro()  
                    break
                  
                else:
                    print("Selecciona una opción válida")
                    tipowok = int(input("Presiona 1 para sencillo y 2 para preparado: "))
        
            break
     
        elif select == 2:
            print("\nEsperamos se te antoje un Wok pronto\n")
            break
          


        else:
            print("Por favor elige entre 1 y 2")
            select = int(input("A continuación escoge 1 para seguir y 2 para salir: "))

#Se invoca la función principal para que el código funcione.
elegir()

num = int(input("Elige 1 para volver a pedir y 2 para salir: "))
#Se usa un ciclo while para permitirle al usuario pedir otro Wok.
#Asimismo, se le da la opción de terminar su orden.
while num == 1 or 2:
    if num == 1:
        elegir()
#Una vez repetida la función, el usuario puede terminar o volver a pedir.
        num = int(input("Elige 1 para volver a pedir y 2 para salir: "))
    
#Se apoya de un segundo condicional para insertar un break y romper con el ciclo.
    elif num == 2:
#Se utiliza un break para romper el ciclo cuando se selecciona 2, es decir, que el usuario quiere pasar al final.
        break

#Se invoca la función para poder saber el precio total.
#Una vez terminado el proceso, el programa agradece y se despide.
print(f"Su total es: {cuentatotal()}")
print("Gracias por tu preferencia, espera próximas noticias")
goodday()
print("La aplicación de Wok sigue en desarrollo")

#¡Se ha avanzado de una manera considerable, sin embargo, siempre se puede mejorar! (:
#Espero poder optimizar este código a lo largo de mi carrera.
