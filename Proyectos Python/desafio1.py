venta1=float(input("ingresar el Total de las Venta 1: "))
venta2=float(input("ingresar el Total de las Venta 2: "))
venta3=float(input("ingresar el Total de las Venta 3: "))

vendedor=input("ingresar el nombre del vendedor: ")
comision=((venta1*6)/100)
total= venta1+comision
print(f"La comision del Vendedor {vendedor} es: {comision}")

print(f"el Total + la Comision es: {total}")
