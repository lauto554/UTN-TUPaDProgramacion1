
# Agenda de Turnos con Nombres (sin listas)

# No listas, no diccionarios, no sets, no tuplas.
# Se permite usar "" como “vacío”.
# Validaciones con .isalpha() y .isdigit() (sin try/except).


print("################# AGENDA TURNOS ########################")
print()

# Variables
lunes_t1 = ""
lunes_t2 = ""
lunes_t3 = ""
lunes_t4 = ""

martes_t1 = ""
martes_t2 = ""
martes_t3 = ""

while True:
    print("========== MENU =============")
    print()

    print("1. Reservar Turno")
    print("2. Cancelar Turno")
    print("3. Ver Agenda del dia")
    print("4. Ver Resumen General")
    print("5. Cerrar Sistema")
    
    print()
    menu_elegido_indice = input("Elija la opción del menú que desea(1,2,3,4,5): ")

    while not menu_elegido_indice.isdigit() or int(menu_elegido_indice) > 5 or int(menu_elegido_indice) <= 0:
        print("Error. Ingrese una opción válida")
        menu_elegido_indice = input("Elija la opción del menú que desea(1,2,3,4,5): ")
        print()    
    
    menu_elegido = int(menu_elegido_indice)    
    
    if menu_elegido == 1:
        print()
        print("------- Reservar Turno -----------")
        
        print()
        print("Indica dia del turno: ")
        dia_turno = input("[1 = Lunes] - [2 = Martes]: ")

        while not dia_turno.isdigit() or int(dia_turno) > 2 or int(dia_turno) <= 0:
            print()  
            print("Error. Ingrese una opción válida")
            dia_turno = input("[1 = Lunes] - [2 = Martes]: ")
        
        nombre_paciente = input("Nombre del Paciente: ")
        
        while not nombre_paciente.isalpha() or nombre_paciente == "":
            print()  
            print("Error. Ingrese un nombre válido")
            nombre_paciente = input("Nombre del Paciente: ")
        
        while int(dia_turno) == 1:
                if lunes_t1 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                elif lunes_t2 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                elif lunes_t3 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                elif lunes_t4 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                
                if lunes_t1 == "":
                    lunes_t1 = nombre_paciente
                    break
                if lunes_t2 == "":
                    lunes_t2 = nombre_paciente
                    break
                if lunes_t3 == "":
                    lunes_t3 = nombre_paciente
                    break
                if lunes_t4 == "":
                    lunes_t4 = nombre_paciente
                    break
                
        while int(dia_turno) == 2:
                if martes_t1 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                elif martes_t2 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                elif martes_t3 == nombre_paciente:
                    print()  
                    print(f"Error. El Paciente {nombre_paciente} ya posee turno para el día seleccionado")
                    break
                
                if martes_t1 == "":
                    martes_t1 = nombre_paciente
                    break
                if martes_t2 == "":
                    martes_t2 = nombre_paciente
                    break
                if martes_t3 == "":
                    martes_t3 = nombre_paciente
                    break
              
        print()
        print("Turno asignado correctamente")
        print()
        
    if menu_elegido == 2:
        print()
        print("------- Cancelar Turno -----------")
        
        print()
        print("Indica dia del turno a cancelar: ")
        dia_turno = input("[1 = Lunes] - [2 = Martes]: ")
    
        while not dia_turno.isdigit() or int(dia_turno) > 2 or int(dia_turno) <= 0:
            print()  
            print("Error. Ingrese una opción válida")
            dia_turno = input("[1 = Lunes] - [2 = Martes]: ")
        
        nombre_paciente = input("Nombre del Paciente: ")
        
        while not nombre_paciente.isalpha() or nombre_paciente == "":
            print()  
            print("Error. Ingrese un nombre válido")
            nombre_paciente = input("Nombre del Paciente: ")
        
        while int(dia_turno) == 1:
                if lunes_t1 == nombre_paciente:
                    print()  
                    lunes_t1 = ""
                    break
                elif lunes_t2 == nombre_paciente:
                    print()  
                    lunes_t2 = ""
                    break
                elif lunes_t3 == nombre_paciente:
                    print()  
                    lunes_t3 = ""
                    break
                elif lunes_t4 == nombre_paciente:
                    print()  
                    lunes_t4 = ""
                    break
                
        while int(dia_turno) == 2:
                if martes_t1 == nombre_paciente:
                    print()  
                    martes_t1 = ""
                    break
                elif martes_t2 == nombre_paciente:
                    print()  
                    martes_t2 = ""
                    break
                elif martes_t3 == nombre_paciente:
                    print()  
                    martes_t3 = ""
                    break
        
        print()
        print("Turno cancelado exitosamente")
        print()
        
    if menu_elegido == 3:
        print()
        print("------- Agenda del día -----------")
        
        print()
        dia_agenda = input("[1] Ver Agenda Lunes - [2] Ver Agenda Martes: ")
        
        while not dia_agenda.isdigit() or int(dia_agenda) > 2 or int(dia_agenda) <= 0:
            print()  
            print("Error. Ingrese una opción válida")
            dia_agenda = input("[1] Ver Agenda Lunes - [2] Ver Agenda Martes: ")
        
        if int(dia_agenda) == 1:
            print()
            print("Agenda Lunes")
            print()
            
            print(f"1er Turno: {"(libre)" if lunes_t1 == "" else lunes_t1 }")
            print(f"2do Turno: {"(libre)" if lunes_t2 == "" else lunes_t2 }")
            print(f"3er Turno: {"(libre)" if lunes_t3 == "" else lunes_t3 }")
            print(f"4to Turno: {"(libre)" if lunes_t4 == "" else lunes_t4 }")
            print()
            
        if int(dia_agenda) == 2:
            print()
            print("Agenda Martes")
            print()
            
            print(f"1er Turno: {"(libre)" if martes_t1 == "" else martes_t1 }")
            print(f"2do Turno: {"(libre)" if martes_t2 == "" else martes_t2 }")
            print(f"3er Turno: {"(libre)" if martes_t3 == "" else martes_t3 }")
            print()
            
    if menu_elegido == 4:
        print()
        print("------- Resumen General -----------")
        
        lunes_turnos_ocupados = 0
        lunes_turnos_disponibles = 0
        
        martes_turnos_ocupados = 0
        martes_turnos_disponibles = 0
        
        if lunes_t1 == "":
            lunes_turnos_disponibles  += 1     
        else:
            lunes_turnos_ocupados  += 1
        
        if lunes_t2 == "":
            lunes_turnos_disponibles  += 1
        else:
            lunes_turnos_ocupados  += 1
        
        if lunes_t3 == "":
            lunes_turnos_disponibles  += 1
        else:
            lunes_turnos_ocupados  += 1
        
        if lunes_t4 == "":
            lunes_turnos_disponibles  += 1
        else:
            lunes_turnos_ocupados  += 1
            
        if martes_t1 == "":
            martes_turnos_disponibles  += 1            
        else:
            martes_turnos_ocupados  += 1
            
        if martes_t2 == "":
            martes_turnos_disponibles  += 1
        else:
            martes_turnos_ocupados  += 1
            
        if martes_t3 == "":
            martes_turnos_disponibles  += 1
        else:
            martes_turnos_ocupados  += 1
            
        dias_mas_turnos = "Lunes" if lunes_turnos_ocupados > martes_turnos_ocupados else ("Martes" if martes_turnos_ocupados > lunes_turnos_ocupados else ("Sin turnos asignados" if lunes_turnos_disponibles == 4 and martes_turnos_disponibles == 3 else "Empatados"))
                
        print()
        print(f"Turnos ocupados Lunes: {lunes_turnos_ocupados}")
        print(f"Turnos disponibles Lunes: {lunes_turnos_disponibles}")
        print()
        print(f"Turnos ocupados Martes: {martes_turnos_ocupados}")
        print(f"Turnos disponibles Martes: {martes_turnos_disponibles}")
        print()
        
        print(f"Dias con mas turnos: {dias_mas_turnos}")
        print()

    if menu_elegido == 5:
        print()
        print("Cerrando sistema...")
        print()
        break
    
    
    
    
            