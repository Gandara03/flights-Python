
#Imports

import random

# Funciones

# función para validar datos
def validacion_de_datos(valor,maximo,minimo):
    resultado=True
    if valor >maximo or valor< minimo:
        resultado=False
    return resultado

# función para elegir la opción que continuara el programa 
def inicio_y_seleccion_de_opciones():
    while True:
        try:
            opciones=("- Opción 1: Jugar","- Opción 2: Puntaje de jugadores","- Opción 3: Salir/ver ganador")
            print('\n'.join(opciones))
            opcion= int(input("\n• Ingrese la opción: "))
            resultado=validacion_de_datos(opcion,3,1)
            if resultado:
                if opcion ==2:
                    registro_de_puntajes_()
                else:
                    return opcion
            else:
                print("Número de opción no existente, reintente.\n")
        except(ValueError,TypeError,KeyboardInterrupt):
            print("\nPor favor ingrese nuevamente una opción valida\n")
            
# función para seleccionar la tematica
def seleccionar_la_tematica(palabras_usadas):
    while True:
        try:
            temas=("Tema 0: Animales","Tema 1: Bebidas","Tema 2: Musculos del cuerpo","Tema 3: Aplicaciones","Tema 4: Paises","Tema 5: Deportes","Tema 6: Frutas","Tema 7: Marcas de celulares")
            print('\n'.join(temas))
            tema=int(input("\n• Escoja una opción(numero): "))
            resultado=validacion_de_datos(tema,7,0)
            if resultado:
                palabra=tematicas_para_palabras(tema,palabras_usadas)
                return palabra
            else:
                print("El numero de tema no se encuentra entre los incluidos. Porfavor reintentelo a continuacion:\n")
        except(ValueError, TypeError, KeyboardInterrupt):
            print("Por favor ingrese una opción valida")
            
# función para elegir la palabra en la tematica que anteriormente selecciono el usuario
def tematicas_para_palabras(tema,palabras_usadas):
    temas=(("perro","gato","caballo","elefante","jirafa","foca","ballena","cocodrilo","leopardo","leon","tigre"),("agua","cerveza","vino","cocacola","jugo","fernet","whisky","sprite"),
           ("tricep","trapecios","cuadriceps","abdominales","biceps"),("youtube","facebook","instagram","whatsapp",),
           ("argentina","alemania","japon","china","brasil","honduras","belgica","marruecos"),("futbol","boxeo","natacion","golf","voley","baloncesto"),
           ("mandarina","manzana","kiwi","anana","naranja","ciruela","banana","frutilla"),("samsung","apple","xiaomi","huawei","sony","motorola"))
    palabra_seleccionada=random.choice(temas[tema])
    while palabra_seleccionada in palabras_usadas:
            palabra_seleccionada=random.choice(temas[tema])
    return palabra_seleccionada

#funcion para elegir la palabra en la tematica que anteriormente selecciono el usuario  
def matriz_para_ahorcado(contador_ahorcado,matriz_ahorcado):
    if contador_ahorcado==0:
        matriz_ahorcado = [ ["┌","─","─","┐"],
                            ["|"," "," "," "," "],
                            ["|"," "," "," "," "],
                            ["|"," "," "," "," "],
                            ["|"," "," "," "," "],
                            ["┌","─","─","─","┐"],
                            ["└","─","─","─","┘"]]
    elif contador_ahorcado==1:
        matriz_ahorcado[1][3]="0"
    elif contador_ahorcado==2:
        matriz_ahorcado[2][3]="|"
    elif contador_ahorcado==3:
        matriz_ahorcado[2][2]="/"
    elif contador_ahorcado==4:
        matriz_ahorcado[2][4]=("\\"[0])
    elif contador_ahorcado==5:
        matriz_ahorcado[3][2]="/"
    else:
        matriz_ahorcado[3][4]=("\\"[0])
    print()
    imprimir_matriz_recursividad(matriz_ahorcado,0,0)
    return matriz_ahorcado
#funcion para imprimir la matriz utilizando recursividad   
def imprimir_matriz_recursividad(matriz,fila,columna=0): # -RECURSIVIDAD-
    if fila<len(matriz):
        for columna in range(len(matriz[fila])):
            print(matriz[fila][columna],end="")
        print("")
        imprimir_matriz_recursividad(matriz,fila+1)
    else:
        print("\n")

# función para obtener el puntaje del jugador y guardarlo en un archivo
def puntaje_y_registro_en_archivo(nombre_jugador, intentos,jugadores):
    salida=open("lista_de_puntos.txt","a")
    total_puntos=12
    if intentos==6:
        puntaje=total_puntos+3
    else:
        puntaje=intentos*2
    print("El jugador",nombre_jugador, "sumo:",puntaje,"puntos\n")
    try:
            a=str(nombre_jugador)+";"+str(puntaje)+"\n"
            salida.write(a)
    except FileNotFoundError as mensaje:
            print("No se pudo abrir el archivo", mensaje)
    except OSError as mensaje:
            print("ERROR", mensaje)
    else:
        pass
    finally:
        try:
            salida.close()
        except NameError:
            pass
        
# función para imprimir el archivo con los puntajes hasta el momento
def registro_de_puntajes_():
    try:
        entrada=open("lista_de_puntos.txt","rt")
        print("--------------------------------------------------")
        print("REGISTRO DE PUNTAJES".center(52),"\n")
        print("Jugador".center(30),"Puntaje".center(14), "\n")
        for linea in entrada:
            linea=linea.rstrip("\n")
            nombre,punto=linea.split(";")
            print(nombre.center(30),(punto).center(14))
        print("-------------------------------------------------\n")
    except FileNotFoundError as mensaje:
        print("No se pudo abrir el archivo", mensaje)
    except OSError as mensaje:
        print("ERROR", mensaje)
    else:
        pass
    finally:
        try:
            entrada.close()
        except NameError:
            pass
        
# función para determinar y dar el ganador de la partida
def ganador():
    mayor_puntaje=["nadie",-100000000000000]
    mayor_puntaje[1]=int(mayor_puntaje[1])
    try:
        lista_puntos=open("lista_de_puntos.txt","rt")
        for linea in lista_puntos:
                linea=linea.strip('\n')
                linea=linea.split(";")
                linea[1]=int(linea[1])
                if linea[1] > mayor_puntaje[1]:
                    mayor_puntaje[0]=linea[0]
                    mayor_puntaje[1]=linea[1]
                    jugadoresempatados=[]
                elif linea[1]==mayor_puntaje[1]:
                    if len(jugadoresempatados)==0:
                        jugadoresempatados=[mayor_puntaje[0],linea[0]]
                    else:
                        jugadoresempatados.append(linea[0])
    finally:
        try:
            lista_puntos.close()
        except NameError:
                pass
    if mayor_puntaje[0]=="nadie":
        print("usted ha salido del programa sin ingresar ningun dato.")
    else:
        mayor_puntaje[1]=str(mayor_puntaje[1])
        nombre_del_ganador=mayor_puntaje[0]
        puntos_del_ganador=mayor_puntaje[1]
        puntos_del_ganador=mayor_puntaje[1]
      
        if nombre_del_ganador not in jugadoresempatados:
            nombre_del_ganador=mayor_puntaje[0]
            puntos_del_ganador=mayor_puntaje[1]
            mensaje_de_ganador=f"el ganador es ... ¡¡{nombre_del_ganador} con {puntos_del_ganador} puntos!!"
            print (mensaje_de_ganador.center(150))
        else:
            mensaje_de_ganador="HUBO UN EMPATE!! los siguientes usuarios obtuvieron :"+puntos_del_ganador+" puntos"
            print (mensaje_de_ganador.center(150))
            #print(jugadoresempatados)
            for i in jugadoresempatados:
                print(i.center(150))
                
# función para borrar archivo
def borrararchivo():
    try:
        lista_puntos=open("lista_de_puntos.txt","w")
    finally:
        try:
            lista_puntos.close()
        except NameError:
                pass       
            
#Programa principal
            
#prints de bienvenida
print("~~ Bienvenidos al Juego del Ahorcado(también llamado colgado) ~~".center(150))
print("")
print("RESUMEN DE LAS REGLAS: es un juego de adivinanzas  para dos o más jugadores. Un jugador piensa en una palabra, frase u oración y el otro trata de adivinarla")
print("Según lo que sugiere por letras o dentro de un cierto número de oportunidades. Usando una fila de guiones, se representa la palabra a adivinar, dando el número de letras, números y categoría. Si el jugador adivinador sugiere una letra o número que aparece en la palabra, el otro jugador la escribe en todas sus posiciones correctas. Si la letra o el número sugerido no ocurre en la palabra, el otro jugador saca un elemento de la figura de hombre palo ahorcado como una marca de conteo. El juego termina cuando:")
print("")
print("-El jugador adivinador completa la palabra")
print("-El otro jugador completa el diagrama")
print("")
print("En este programa el juego sera contra la maquina sin embargo podremos jugar mas de un jugador de manera tal que los puntos hechos por cada jugador seran agregados")
print("en un archivo y quien obtenja mas puntaje al final sera el vencedor, los jugadores tendran un maximo de 6 intentos para fallar.")
print("\nPuntajes:")
print("- sin fallos = (15) puntos \n- un fallo = (10) puntos \n- dos fallos = (8) puntos \n- tres fallos = (6) puntos \n- cuatro fallos = (4) puntos \n- cinco fallos = (2) puntos \n- seis fallos = (0) puntos")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("¡Ahora si a jugar!".center(150))
# Inicio de variables
jugadores=[]
palabras_usadas=[]
finalizar=0
# Inicio de programa
while finalizar!=-1:
    opcion=inicio_y_seleccion_de_opciones()
    if opcion ==1:
        ahorcado=0
        vidas=6
        completado=False
        letras_descubiertas=[]
        palabras_adivinadas=[]
        matriz_ahorcado=[]
        nombre_jugador=input("• Ingrese su nombre: ").capitalize()
        while nombre_jugador in jugadores:
            print("el nombre ingresado ya fue utilizado, le recordamos que el programa fue diseñado para que puedan jugar varios jugadores pero en una sola ronda , en caso de queres repetir debera reiniciar el programa")
            nombre_jugador=input("• ingrese su nombre: ").capitalize()
        jugadores.append(nombre_jugador)
        print("Escoja el Tema".center(150))
        palabra=seleccionar_la_tematica(palabras_usadas)
        palabras_usadas.append(palabra)
        palabra_invisible="__ "*len(palabra)
        matriz_ahorcado = matriz_para_ahorcado(ahorcado,matriz_ahorcado)
        print(palabra_invisible)
        while not completado and vidas>0:
            adivinar=input("\n• Adivina una letra o la palabra: ").lower()
            #para saber si ingrese letras o no
            if adivinar.isalpha():
                #para adivinar palabra entera
                if len(adivinar) > 1:
                    if adivinar != palabra:
                        print("\nLa palabra ingresada no es correcta.")
                        vidas -= 1
                        ahorcado += 1
                        print("vidas restantes:", vidas)
                    else:
                        completado=True
                        palabra_invisible=palabra
                        print(palabra_invisible,palabra)
                #para adivinar palabra por letra
                elif len(adivinar) == 1:
                    if adivinar in letras_descubiertas:
                        print("\nYa adivinaste esa letra:", adivinar)
                        print("vidas restantes", vidas)
                    elif adivinar not in palabra:
                        print(f"\nLa letra '{adivinar}' no esta en la palabra.")
                        vidas -= 1
                        ahorcado += 1
                        print("Vidas restantes:",vidas)
                    else:
                        print("\nHas adivinado una letra de la palabra:", adivinar)
                        print("Intentos restantes",vidas)
                        letras_descubiertas.append(adivinar)
                        palabra_como_lista=list(palabra_invisible.split())
                        #remplaza el guion por la letra adivinada
                        letra_en_ubicacion_de_palabra=[i for i, letra in enumerate(palabra) if letra == adivinar]
                        for ubicacion in letra_en_ubicacion_de_palabra:
                            palabra_como_lista[ubicacion] = adivinar
                            palabra_invisible=" ".join(palabra_como_lista)
                            #si no hay guiones significa que fue completada
                            if "__" not in palabra_invisible:
                                completado= True
            # cuando falla
            else:
                print("No es válido. Por favor ingrese nuevamente una opción valida")
                print("vidas restantes", vidas)
            matriz_para_ahorcado(ahorcado,matriz_ahorcado)
            print(palabra_invisible)
            print("\n")
        #resultado
        if palabra != ("").join(palabra_invisible.split(" ")):
            print("¡perdiste! tus vidas se han agotado, la palabra era: "+(palabra.upper()) )
        else:
            print("¡Adivinaste la palabra!")
        puntaje_y_registro_en_archivo(nombre_jugador,vidas,jugadores)
        print(f"{'-' * 93}\n{'-' * 93}\n")
    elif opcion==3:
        finalizar=-1
ganador()
borrararchivo()
#final del programa
