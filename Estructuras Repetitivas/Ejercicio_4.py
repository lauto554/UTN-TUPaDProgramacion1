#Escape Room: La Bóveda

# El juego continua mientras
# energia > 0, tiempo > 0, cerraduras_abiertas < 3, alarma == FALSE

# Condiciones de fin
# Si cerraduras_abiertas == 3 → VICTORIA
# Si energia <= 0 o tiempo <= 0 → DERROTA
# Si se bloquea por alarma → DERROTA (bloqueo)

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

print("########## Escape Room: La Bóveda #########")
print()

nombre_agente = input("Ingresa tu nombre de Agente: ")    

while not nombre_agente.isalpha() or nombre_agente == "":
    print()  
    print("Error. Ingrese un nombre válido")
    nombre_agente = input("Ingresa tu nombre de Agente: ")  
    
print()
    
while True:
    # Mostrar estado en cada turno
    print("================ MENU ==============")
    print()
    menu = ["Forzar Cerradura (costo: -20 energía, -2 tiempo)", "Hackear Panel  (costo: -10 energía, -3 tiempo)", "Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)"]
    for idx, m in enumerate(menu):
        print(f"{idx + 1}. {m}")
    print()
    print("-------- Estado actual --------")
    print(f"Agente: {nombre_agente}")
    print(f"Energia disponible: {energia}")
    print(f"Tiempo disponible: {tiempo}")
    print(f"Cerraduras Abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'Prendida!' if alarma else 'Apagada'}")
    print(f"Cerraduras Forzadas Consecutivas: {forzar_seguidas}")
    print(f"Codigo Parcial: {codigo_parcial}")
    print()

    # Condiciones de fin
    if cerraduras_abiertas == 3:
        print()
        print("Ganaste!")
        print("Abriste la bóveda a tiempo")
        print()
        break
    if (energia <= 0 or tiempo <= 0) and cerraduras_abiertas < 3:
        print()
        print("Perdiste")
        print("Te quedaste sin energia o sin tiempo y no abriste la bóveda")
        print()
        break
    if tiempo <= 3 and alarma == True:
        print()
        print("Perdiste")
        print("La alarma esta sonando y tu tiempo es menor o igual a 3")
        print()
        break

    menu_elegido_indice = input("Elija la opción del menú para avanzar (1,2,3): ")
    print()
    while not menu_elegido_indice.isdigit() or int(menu_elegido_indice) < 1 or int(menu_elegido_indice) > 3:
        print("Error. Ingrese una opción válida")
        menu_elegido_indice = input("Elija la opción del menú para avanzar (1,2,3): ")
        print()
    menu_elegido = int(menu_elegido_indice)

    if menu_elegido == 1:
        forzar_seguidas += 1
        if forzar_seguidas == 3:
            print()
            print("Bloqueaste la cerradura. Alarma activada")
            alarma = True
            energia -= 20
            tiempo -= 2
            forzar_seguidas = 0
            continue
        if energia < 40:
            print()
            print("Riesgo de alarma")
            print()
            clave_alarma = input("Ingresa un numero del 1 al 3 para evitar q suene: ")
            while not clave_alarma.isdigit() or int(clave_alarma) < 1 or int(clave_alarma) > 3:
                print("Error. Ingrese una numero válida")
                clave_alarma = input("Ingresa un numero del 1 al 3 para evitar q suene: ")
                print()
            if int(clave_alarma) == 3:
                alarma = True
        print()
        print("Cerradura abierta")
        cerraduras_abiertas += 1
        energia -= 20
        tiempo -= 2
    elif menu_elegido == 2:
        forzar_seguidas = 0
        print("Hackeando panel...")
        for i in range(4):
            print(f"Progreso hackeo paso {i+1}/4")
            letra_parcial = input("Ingresa una letra para el código: ")
            while not letra_parcial.isalpha() or letra_parcial == "":
                print("Error. Ingrese una letra válida")
                letra_parcial = input("Ingresa una letra para el código: ")
            while len(letra_parcial) != 1:
                print("Error. Ingrese de a 1 letra")
                letra_parcial = input("Ingresa una letra para el código: ")
            codigo_parcial += letra_parcial
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print()
            print("Cerradura abierta")
            print()
        energia -= 10
        tiempo -= 3
    elif menu_elegido == 3:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
        print("Descansaste. Energia y tiempo actualizados.")
        forzar_seguidas = 0
        
        print()
        print("Descansaste.")
        print()
        
        if energia == 100:
            energia = 100
            tiempo -= 1
            print("Tu energia esta completa")
            continue
            
        if alarma:
            energia -= 10
            print("La alarma esta prendida. Restas -10 de energia")
            
        energia += 15
        
          
        
        