# PC-A01705887-AD22
Este repositorio fue creado para el desarrollo del proyecto de la materia de Pensamiento Computacional.

### Contexto

La pasta es un alimento universal que a la mayoría de la gente le gusta, en las diferentes culturas asiáticas se acostumbra mezclarla con otros ingredientes para conseguir sabores exquisitos. Es por eso que se ha hecho cada vez más común encontrar lugares que vendan este tipo de comida.

Dentro del Tecnológico de Monterrey campus Querétaro y campus Monterrey existe un puesto de comida muy popular entre los jóvenes que se llama Fusion Wok. Día con día cientos de jóvenes van a comer ahí, ya que venden diferentes tipos de pasta combinados con vegetales e incluso una que otra fruta y proteínas. En el TEC campus Querétaro, este establecimiento se encuentra en el lugar conocido como "Plaza roja", a un costado del Nutrisa.

Se sirve principalmente pasta con otros complementos como pueden ser vegetales variados como aceitunas, zanahoria, espinaca, champiñones, papas, entre muchos otros, al igual que con proteína como es la carne, pollo o tofu y algún aderezo. Debido a su popularidad, en ciertas horas pico se arman grandes filas para poder comprar una de las cajitas con el alimento que venden. Normalmente, el precio de estos oscila entre los 85 y los 100 pesos, dependiendo del tipo de Wok que elijas, además también tienes la opción de comprar bebidas refrescantes como agua natural o Fuze tea. Adicionalmente, la tienda te da un sistema de recompensas en el que acumulas visitas y la quinta vez que compres un producto, el sexto es gratis.

### Razón

La razón por la que decidí trabajar este tema, es porque creo que en el futuro así será la industria de la comida rápida, por ejemplo: en Starbucks puedes ordenar tu bebida desde tu celular para que cuando llegues a la cafetería, ya esté hecha y solamente la recojas. Además, considero que es un proceso de automatización que puede llegar a ahorrar tiempo e incluso dinero. También, cabe mencionar que es uno de mis lugares favoritos para comer en la escuela, ya que desde mi punto de vista es una comida muy completa.

### Propósito

En este programa se busca crear una especie de formulario donde el cliente pueda pedir su wok con anticipación para que cuando llegue esté listo y así se pueda evitar las largas filas, de igual manera, se busca automatizar la opción del pago, al permitir las tarjetas de débito o crédito.

## Algoritmo
1. Abrir la aplicación
2. Iniciar sesión
    
    2.1 Si contraseña correcta
      
    - 2.1.1 Pasar a la interfaz de usuario
       
    2.2 Si contraseña incorrecta
      
    - 2.2.1 Regresar a 2.1
        
(Una vez en la interfaz de usuario)

3. Mostrar nombre del cliente

4. Invitar al cliente a ordenar un Wok

    4.1 Si cliente acepta
    
      - 4.1.1 Dirigir a las opciones de comida
       
    4.2 Si cliente rechaza
    
      - 4.2.1 Cerrar ventana
      
      - 4.2.2 Mandar a la interfaz de usuario
      
      - 4.2.3 Esperar que de clic en opciones de comida
      
        - 4.2.3.1 Si cliente no hace clic en nada
           
        - 4.2.3.2 Hacer una encuesta de satisfacción
            
(En las opciones de comida)

5. Desplegar todos los tipos de pasta

6. Desplegar tipos de proteína

7. Desplegar tipo de verdura

8. Desplegar tipo de aderezo

9. Mostrar botón de listo

    9.1 Si cliente da clic en "listo"
    
      - 9.1.1 Entonces mostrar precio
        
      - 9.1.2 Preguntar si confirma su orden
        
        - 9.1.2.1 Si confirma
            
          - 9.1.2.1.1 Preguntar información de la tarjeta o forma de pago
                
           - 9.1.2.1.2 Mostrar QR para la entrega
                
         - 9.1.2.2 Si rechaza
            
            - 9.1.2.2.1 Regresar a las opciones de comida
