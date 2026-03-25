# Login con intentos + menú de acciones con validación estricta.

print("################# LOGIN USUARIO ########################")
print()

usuario_correcto = "alumno"
clave_correcta = "python123"

max_intentos = 3
intento = 0

while not intento > max_intentos:
    if intento == max_intentos:
        print()
        
        print("Cuenta bloqueada")
        break
    
    print()
    print(f"Intento {intento + 1}/3")
    
    usuario_input = input("Usuario: ")
    
    while usuario_input.strip() == "":
        print("Error: Usuario no puede ir vacío")
        print()
        usuario_input = input("Usuario: ")
        
        
    clave_input = input("Clave: ")
    
    while clave_input.strip() == "":
        print("Error: Clave no puede ir vacío")
        print()
        clave_input = input("Clave: ")
    
    
    if usuario_input != usuario_correcto or clave_input != clave_correcta:
        print("Error: Credenciales inválidas")
        intento += 1
    else:
        print()
        print("Acceso concedido")
        print()
        break
    
menu = ["Ver estado Inscripcion", "Cambiar Clave", "Mostrar mensaje motivacional", "Salir"]

while True:
    
    print("================ MENU ==============")
    print()
    
    index = 0
    for m in menu:
        print(f"{index + 1}. {m}")
        index += 1
    
    print()
    menu_elegido_indice = input("Elija la opción del menú que desea(1,2,3,4): ")
    print()
    
    while not menu_elegido_indice.isdigit() or index < int(menu_elegido_indice) or int(menu_elegido_indice) <= 0:
        print("Error. Ingrese una opción válida")
        menu_elegido_indice = input("Elija la opción del menú que desea(1,2,3,4): ")
        print()
        
    menu_elegido = int(menu_elegido_indice)
    
    if menu_elegido == 1:
        print()
        print("Inscripto")
        print()
    
    if menu_elegido == 2:
        print()
        print("-------------- Cambio de clave ------------")
        print()
        
        nueva_clave = input("Ingresa nueva clave (debe tener minimo 6 caracteres): ")
        
        while True:
            if nueva_clave == "":
                print("Error: Nueva clave no puede ir vacía")
                print()
                nueva_clave = input("Ingresa nueva clave (debe tener minimo 6 caracteres): ")
                continue
            if len(nueva_clave) < 6:
                print()
                print("La clave debe ser mayor a 6 dígitos")
                print()
                nueva_clave = input("Ingresa nueva clave (debe tener minimo 6 caracteres): ")
                continue
            break
        confirmar_nueva_clave = input("Confirmar nueva clave: ")
        
        while confirmar_nueva_clave == "":
            print("Error: Confirmar nueva clave no puede ir vacía")
            print()
            confirmar_nueva_clave = input("Confirmar nueva clave: ")
        if nueva_clave != confirmar_nueva_clave:
            print()
            print("Las claves no coinciden")
            print()
        else:
            print()
            print("Cambio de clave exitoso")
            print()
            
    if menu_elegido == 3:
        print()
        print("No se trata de ver para creer, sino de creer para ver...")
        print()
        
    if menu_elegido == 4:
        print()
        print("Cerrando programa...")
        print()
        break
    

