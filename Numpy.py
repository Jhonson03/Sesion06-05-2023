import numpy as np

'''Obtener el valor maximo y minimo de una array

Arrays = np.matrix('[1, 2, 3; 4, 5, 6 ; 7, 8, 9]')

ValorMaximo = Arrays.max()
Valorminimo = Arrays.min()

print(ValorMaximo)
print(Valorminimo)'''

data = np.loadtxt('Productos.txt', dtype=str, delimiter=',')

print(f"Productos existentes -> \n {data}")

print("Agregar nuevo producto")

Nombre = input("Ingrese el nombre -> ")
Proveedor = input("Ingrese el proveedor -> ")
Cantidad = int(input("Ingrese la cantidad -> "))

NuevoProducto = np.array([[Nombre, Proveedor, Cantidad]], dtype=str)
data = np.vstack((data, NuevoProducto))
np.savetxt('Productos.txt', data, delimiter=',', fmt='%s')

print(f"Productos actualizados -> \n{data}")