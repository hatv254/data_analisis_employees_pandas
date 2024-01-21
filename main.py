import pandas as pd

empleados = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Carlos'],
    'Edad': ['25', '30', '27', '35', '40'],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'Salario': ['2000', '2500', '2200', '3000', '3500']
})

#Convierte las columnas 'Edad' y 'Salario' de tipo str a tipo int utilizando pd.to_numeric()
empleados['Edad'] = pd.to_numeric(empleados['Edad'], errors='coerce')
empleados['Salario'] = pd.to_numeric(empleados['Salario'], errors='coerce')
print(empleados.info())

#Accede a la columna 'Ciudad' y muestra sus valores
print(empleados['Ciudad'])

#Selecciona los datos del empleado llamado 'Pedro' utilizando el método loc o iloc
datos_pedro = empleados.iloc[2,:]
print(empleados.iloc[2,:])
datos_pedro = empleados.loc[empleados['Nombre'] == 'Pedro']
print(datos_pedro)

#Encuentra a los empleados que tienen más de 30 años utilizando operadores de comparación
empleadoos_mayores = empleados.loc[empleados['Edad'] > 30]
print("Empleados mayores\n")
print(empleadoos_mayores)