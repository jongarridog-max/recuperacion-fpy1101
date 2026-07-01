


def calcular_descuento(subtotal):# ESTA FUNCIONA ES PARA CALCULAR EL DESCUENTO 
    if subtotal >= 50000:#EL DESCEUNTO APLICA A COMPRA SUPERIORES O IGUAL A 50000
        return subtotal * 0.10   #aca se multiplica por el sub total
    else:
        return 0
    
#ENTRADA
def mostrar_resultado(nombre_del_producto, subtotal, descuento, total):# ACA SE INGRESA LA INFORMACION  
    print("====RESUMEN DE VENTA=====")
    print(f"PRODUCTO:{nombre_del_producto}")
    print(f"SUBTOTAL:${subtotal}")
    print(f"DESCUENTO:${descuento}")
    print(f"TOTAL A PAGAR ${total}")

#PROCESO 
respuesta_usuario = "s"

while respuesta_usuario.lower() == "s":
    nombre_del_producto = input("INGRESE EL NOMBRE DEL PRODCUTO :").strip()#SE ESCRIBE EL NOMBRE
    while nombre_del_producto == "":#SI ESCRIBE ALGUNA OTRA COSA QUE NO SEA EL NOMBRE DE UN PRODUCTO DARA ERROR 
        print("[ERROR] EL NOMBRE NO PUEDE ESTAR VACIO!!")
        nombre_del_producto = input("INGRESE EL NOMBRE DEL PRODUCTO :").strip()

    
    precio_unitario = 0
    while precio_unitario <= 0:
        try:
            precio_unitario = float(input("INGRESE EL VALOR UNITARIO :"))#SE INGRESA EL VALOR , SE COLOCA 
            if precio_unitario <= 0:
                print("[ERROR]EL PRECIO DEBE SER MAYOR A CERO!!")#AL IGUAL QUE EL NOMBRE SI NO SE INGRESA UN NUMERO EN CESIMAL O  DARA ERROR
        except ValueError:
            print("[ERROR]EL PRECIO DEBE SER UN DATO NUMERICO!!")
            precio_unitario = 0

    cantidad_comprada = 0
    while cantidad_comprada <= 0:
        try:
            cantidad_comprada = int(input("INGRESE LA CANTIDAD COMPRADA :"))# SE INGRESA LA CANTIDAD SE COLOCA UN INT PARA QUE SEA NUMERO ENTERO
            if cantidad_comprada <= 0:#SI SE INGRESA UN NUMERO MENOR A CERO O UN NUMERO QUE NO SEA UNO ENTERO DARA ERROR 
                print("[ERROR] LA CANTIDAD DEBE SER MAYOR A CERO!!")
        except ValueError:
            print("[ERROR] LA CANTIDAD DEBE SER UN NUMERO ENTERO!!")
            cantidad_comprada = 0

    subtotal = precio_unitario * cantidad_comprada

    descuento = calcular_descuento(subtotal)

    total = subtotal - descuento

   #salida
    mostrar_resultado(nombre_del_producto, subtotal, descuento, total)

    #CUANDO TERMINE EL RPOCESO ACA PREGUNTA SI QUIERO AGREGAR OTRA COMPRA 
    respuesta_usuario = input("¿DESEA REALIZAR OTRA VENTA?(S/N) ").strip()
    while respuesta_usuario.lower() not in ["s", "n"]:
        print("[ERROR] opcion no valida .INGRESE [S] O [N] .")
        respuesta_usuario = input("¿DESEA REALIZAR OTRA VENTA? (S/N) ").strip()


print("\nPrograma finalizado.")
