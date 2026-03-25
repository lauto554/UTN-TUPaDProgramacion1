print("--- BIENVENIDO A LA ARENA ---")
print()

nombre_gladiador = input("Nombre del Gladiador: ")

while not nombre_gladiador.isalpha() or nombre_gladiador == "":
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_base_gladiador = 15
daño_base_enemigo = 12
turno_gladiador = True

print()
print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    print()
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    print()
    opcion = input("Opción: ")
    print()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
        print()

    opcion = int(opcion)

    if opcion == 1:
        daño_final = daño_base_gladiador

        if vida_enemigo < 20:
            daño_final = daño_base_gladiador * 1.5
            print(">> ¡Golpe crítico!")

        vida_enemigo -= daño_final
        
        print()
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
        print()

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        print()
        
        for _ in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            print()
            
    elif opcion == 3:
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1

            if vida_gladiador > 100:
                vida_gladiador = 100

            print()
            print(">> Te curaste 30 puntos de vida.")
            print()
            
        else:
            print()
            print("¡No quedan pociones!")
            print()
            

    if vida_enemigo > 0:
        vida_gladiador -= daño_base_enemigo
        print()
        
        print(f">> ¡El enemigo contraataca por {daño_base_enemigo} puntos!")
        print()

    if vida_gladiador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

print()

if vida_gladiador > 0:
    print()
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
    print()
else:
    print()
    print("DERROTA. Has caído en combate.")
    print()