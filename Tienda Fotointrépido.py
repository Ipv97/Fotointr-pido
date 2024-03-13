from colorama import *
import os


#Lista para las diferentes marcas de cámaras.
marca_cámaras = ["Nikon","Canon","Sony"]
#Lista para las gamas de nikon.
gama_nikon = ["DSLR","Z"]
#Lista para los modelos dslr nikon.
modelo_dslr_nikon = ["D6","D780","D850","D7500","D5600"]
#Lista para los modelos Z nikon.
modelo_z_nikon = ["Zf","Z8","Zfc","Z30","Z9","Z6II","Z7II","Z5","Z50"]
#Lista de los objetivos nikon.
objetivos_nikon_dslr = ["AF-S DX NIKKOR 18-300mm f/3.5-6.3G ED VR","AF-S NIKKOR 35mm f/1.8G ED"]
objetivos_nikon_z = ["NIKKOR Z 85mm f/1.2 S","NIKKOR Z MC 50mm f/2.8","NIKKOR Z 35mm f/1.8 S","NIKKOR Z 70-200mm f/2.8 VR S"]
#Lista para las gamas de canon.
gama_canon = ["Réflex","Mirrorless"]
#Lista para los modelos Réflex canon.
modelo_reflex_canon = ["EOS 2000D","EOS 250D","EOS 4000D","EOS 77D","EOS 850D","EOS 90D"," EOS 5D Mark IV","EOS 6D Mark II","EOS-1D X Mark III"]
#Lista para los modelos Mirrorless canon.
modelo_mirrorless_canon = ["EOS R3","EOS R5","EOS R7","EOS R10","EOS RP"]
#Lista de objetivos canon.
objetivos_canon = ["Canon EF 85 mm f/1.8 USM","Canon RF 50mm F1.8 STM Lens","Canon EF 35 mm f/1.4L II USM"]
#Lista modelos sony.
modelo_sony_e_fullframe = ["Alpha 9 III","Alpha 7R V","Alpha 9 II","Alpha 7R III"]
modelo_sony_e_apsc = ["Alpha 6700","Alpha 6400","Alpha 6600","Alpha 6300"]
modelo_sony_a = ["Alpha 99 II","Alpha 77 II","Alpha 58 ","Alpha 68"]
#Lista gama sony.
gama_sony = ["Mirrorles montura E fullframe","Mirrorles montura E APS-C","Montura A"]
#Lista objetivos sony.
objetivos_sony = ["G Master 50mm f/1.4 full-frame","G Master OSS II 70-200mm f/2.8 full-frame","G OSS 70-300mm f/4.5-5.6 full-frame"]
#Lista accesorios.
accesorios = ["Flash","Trípode","Foco de luz","Mochila","Reflector"]
#Lista vacía para registrar los clientes.
registro_clientes = []
#Lista para registrar la compra realizada.
registro_compra = []

cartel_tienda = f"""
========================================
|                                      |
|                                      |
|           Fotointrépido              |
|                                      |
|                                      |
========================================
"""

print(cartel_tienda)
print(f"Bienvenido/a a Fotointrépido.\nEn nuestra tienda encontrarás todo lo necesario para empezar en el mundo de la fotografía.\n")
print("Estas son las marcas de cámaras que disponemos:")

for marca in marca_cámaras:
    print(marca)

seleccion_marca = input("¿En qué marca está interesado/a?: ")

os.system("cls")

if seleccion_marca == "Nikon":
    registro_compra.append(seleccion_marca)
    print("De la marca Nikon disponemos de estas gamas:")
    for i, gama in enumerate(gama_nikon, start=1):
        print(Fore.YELLOW, i, gama, Fore.RESET)
    
    seleccion_compra = int(input("Seleccione la gama de esta marca: "))
    if seleccion_compra == 1:
        registro_compra.append(gama_nikon[0])
        print("De la gama dlsr disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_dslr_nikon, start=1):
            print(Fore.YELLOW, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_dslr_nikon[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama dslr disponemos:")
        for i, objetivo in enumerate(objetivos_nikon_dslr, start=1):
            print(Fore.YELLOW, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_nikon_dslr[seleccion_compra_objetivo - 1])
    
    elif seleccion_compra == 2:
        registro_compra.append(gama_nikon[1])
        print("De la gama z disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_z_nikon, start=1):
            print(Fore.YELLOW, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_z_nikon[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama z disponemos:")
        for i, objetivo in enumerate(objetivos_nikon_z, start=1):
            print(Fore.YELLOW, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_nikon_z[seleccion_compra_objetivo - 1])

elif seleccion_marca == "Canon":
    registro_compra.append(seleccion_marca)
    print("De la marca Canon disponemos de estas gamas:")
    for i, gama in enumerate(gama_canon, start=1):
        print(Fore.RED, i, gama, Fore.RESET)
    
    seleccion_compra = int(input("Seleccione la gama de esta marca: "))
    if seleccion_compra == 1:
        registro_compra.append(gama_canon[0])
        print("De la gama reflex disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_reflex_canon, start=1):
            print(Fore.RED, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_reflex_canon[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama reflex disponemos:")
        for i, objetivo in enumerate(objetivos_canon, start=1):
            print(Fore.RED, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_canon[seleccion_compra_objetivo - 1])
    
    elif seleccion_compra == 2:
        registro_compra.append(gama_canon[1])
        print("De la gama mirrorless disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_mirrorless_canon, start=1):
            print(Fore.RED, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_mirrorless_canon[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama mirrorless disponemos:")
        for i, objetivo in enumerate(objetivos_canon, start=1):
            print(Fore.RED, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_canon[seleccion_compra_objetivo - 1])

elif seleccion_marca == "Sony":
    registro_compra.append(seleccion_marca)
    print("De la marca Sony disponemos de estas gamas:")
    for i, gama in enumerate(gama_sony, start=1):
        print(Fore.GREEN, i, gama, Fore.RESET)
    
    seleccion_compra = int(input("Seleccione la gama de esta marca: "))
    if seleccion_compra == 1:
        registro_compra.append(gama_sony[0])
        print("De la gama E fullframe disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_sony_e_fullframe, start=1):
            print(Fore.GREEN, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_sony_e_fullframe[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama E fullframe disponemos:")
        for i, objetivo in enumerate(objetivos_sony, start=1):
            print(Fore.GREEN, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_sony[seleccion_compra_objetivo - 1])
    
    elif seleccion_compra == 2:
        registro_compra.append(gama_sony[1])
        print("De la gama E APS-C disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_sony_e_apsc, start=1):
            print(Fore.GREEN, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_sony_e_apsc[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama E APS-C disponemos:")
        for i, objetivo in enumerate(objetivos_sony, start=1):
            print(Fore.GREEN, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_sony[seleccion_compra_objetivo - 1])

    elif seleccion_compra == 3:
        registro_compra.append(gama_sony[2])
        print("De la gama A disponemos de estos modelos:")
        for i, modelo in enumerate(modelo_sony_a, start=1):
            print(Fore.GREEN, i, modelo, Fore.RESET)
        
        seleccion_compra_modelo = int(input("Seleccione un modelo de esta gama: "))
        registro_compra.append(modelo_sony_a[seleccion_compra_modelo - 1])
        
        print("En cuanto a los objetivos de la gama A disponemos:")
        for i, objetivo in enumerate(objetivos_sony, start=1):
            print(Fore.GREEN, i, objetivo, Fore.RESET)
        
        seleccion_compra_objetivo = int(input("Seleccione un objetivo para esta gama: "))
        registro_compra.append(objetivos_sony[seleccion_compra_objetivo - 1])

os.system("cls")

print("Tambien disponemos de los siguientes accesorios: ")
for i, accesorio in enumerate(accesorios,start=1):
    print(Fore.BLUE,i,accesorio,Fore.RESET)

seleccion_accesorio = int(input("¿Qué accesorio necesita?: "))

if seleccion_accesorio == 1:
    registro_compra.append(accesorios[0])
elif seleccion_accesorio == 2:
    registro_compra.append(accesorios[1])
elif seleccion_accesorio == 3:
    registro_compra.append(accesorios[2])
elif seleccion_accesorio == 4:
    registro_compra.append(accesorios[3])
elif seleccion_accesorio == 5:
    registro_compra.append(accesorios[4])

os.system("cls")

nombre_apellidos = input("Por favor ingrese su nombre y apellidos para tenerle registrado/a: ")
registro_clientes.append(nombre_apellidos)

os.system("cls")

print(f"Cliente:\n {nombre_apellidos}")
print("Compra:")

for item in registro_compra:
    print(item)

print("¡Gracias por visitar nuestra tienda!")

input()