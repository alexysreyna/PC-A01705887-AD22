"""
Este es un archivo python para el proyecto de pensamiento computacional
A01705887
Se pretende seguir el pseudocódigo una vez aprendidos los fundamentos
"""


#Se le pide su usuario y contraseña al cliente.
user = input("Usuario: ")
password = input("Contraseña: ")

#Se definen los valores de precio para los woks tanto sencillos como preparados.
#Además se pone el valor de las bebidas que nos ayudará a sacar el precio total al final.
sencillo = 85
preparado = 94
agua = 10
refresco = 20

#Se le da la bienvenida al usuario, usando el input que nos dió previamente en usuario.
print("Bienvenido a la aplicación de Wok", user)

#Se le invita al cliente a ordenar un Wok y basado en su decisión se le mandan distintas opciones.
print("¿Usted desea ordenar un Wok?")

#Se define la varable goodday para usarla cuando el usuario haya terminado su compra o no quiera comprar en ese momento.
#Es parte de una despedida predeterminada de la interfaz.
def goodday():
     print("¡Qué tengas un buen día!")

#Se define la función cuenta total que nos ayudará a que el usuario sepa cuánto dinero debe pagar.
def cuentatotal ():
    print("Selecciona lo que pediste para poder calcular el precio")
    print("Sencillo - 1")
    print("Preparado - 2")
    print("Sin bebida - 0")
    print("Agua - 1")
    print("Refresco - 2")

#Se separan las bebidas y los Woks para poder imprimir mensajes distintos con el precio.
    artfinal = int(input("Wok sencillo o preparado: "))
    if artfinal == 1:
        print("Son 85 pesos")
    elif artfinal == 2:
        print("Son 94 pesos")
    else:
        print("Selecciona por favor lo que ordenaste")

    bebida = int(input("Agua, refresco o sin bebida: "))
    if bebida == 0:
        print("No ordenaste bebida")
    if bebida == 1:
        print("Son 10 pesos")
    if bebida == 2:
        print("Son 20 pesos")

#Se define la función retro, que nos ayudará a ejecutar la parte de retroalimentación del programa.
#En esta función se utiliza la condición y los operadores lógicos para darle el mejor mensaje posible al usuario, según su puntuación.
def retro():
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
     
#Se define la función elegir, ya que por medio de esta elección de condicionales podremos saber lo que el usuario quiere.
#Se le muestran varias opciones y mediante el uso de números enteros el usuario selecciona lo que desea.
#En los condicionales se usa el doble igual para indicar que si el valor es "tal", se debe ejecutar cierta acción.
#Adicionalmente, se crean variables como: select, wokprep y tipowok para facilitar el proceso.
def elegir():
    print("Presiona 1 para sí y 2 para no")
    select = int(input())
    if select == 1:
        print("Redireccionando a la página de selección")
        print("SELECCIONA EL TIPO DE WOK QUE DESEAS")
        print("Presiona 1 para sencillo y 2 para preparado")
        tipowok = int(input())
        if tipowok == 1:
            print("Haz seleccionado un wok sencillo")
            print("Para este tipo de Wok debes ir a la sucursal")
            print("Sin embargo, puedes pagar desde la app")
            retro()
            cuentatotal()
            goodday()
            
        elif tipowok == 2:
            print("Haz seleccionado un wok preparado")
            print("Estas son las opciones")
            print("Fusion Wok - 1")
            print("MHC Wok - 2")
            print("Italian Wok - 3")
            print("Chicken Teriyaki - 4")
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
        print("Esperamos se te antoje un Wok pronto")
        goodday()
    else:
        print("Por favor elige entre 1 y 2")

elegir()

#Se finaliza la interacción con el usuario y se utiliza una función de despedida que ya había sido previamente definida.
print("La aplicación de Wok sigue en desarrollo")
    

#El programa sigue en desarrollo, se piensan agregar todos los ingredientes para el Wok sencillo, así como ciclos
#Y otras opciones, conforme se vayan aprendiendo/repasando en clase.
