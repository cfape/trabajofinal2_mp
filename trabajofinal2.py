# Trabajo Final 2 Modulos y Paquetes
#Generar nuevo Dataset con graficos
#Generar los siguientes gráficos adicionales:
#Histograma de ventas
#Gráfico de dispersión (Precio vs Cantidad)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. DEFINIR VARIABLES INDEPENDIENTES
productos_base = [
    'Agua de Rosas 50 ml', 'Shampoo Solido Rulos 70 g', 'Mix Oliva y Oregano 30 ml', 
    'Pomada de Calendula 20 g', 'Repelente de Hierba Luisa 75 ml', 'Aceite de Ricino 30 ml', 
    'Aceite de Jojoba 30 ml', 'Aceite de Rosa Mosqueta 30 ml', 'Aceite de Almendras 30 ml', 
    'Aceite de Pepita de Uva 30 ml'
]
precios_base = [18, 25, 25, 17, 18, 20, 23, 40, 20, 22]
ciudades_base = ['Lima', 'Cusco', 'Arequipa', 'Trujillo', 'Iquitos']
distritos_30 = [
    'Miraflores', 'San Isidro', 'Barranco', 'Sacsayhuaman', 'Ollantaytambo',
    'Yanahuara', 'Cayma', 'Victor Larco', 'Huanchaco', 'Belén',
    'Paucarpata', 'Surco', 'La Molina', 'Pisac', 'Chinchero',
    'Moche', 'Punchana', 'San Borja', 'Wanchaq', 'Selva Alegre',
    'Lince', 'Magdalena', 'Urubamba', 'Cerro Colorado', 'El Porvenir',
    'Iquitos Centro', 'Pueblo Libre', 'San Sebastian', 'Jose Luis Bustamante', 'Huancayo'
]

# 2. CREACIÓN DEL DATASET
data = {
    'Producto': productos_base * 3,
    'Precio': precios_base * 3,
    'Cantidad': np.random.randint(10, 150, size=30), 
    'Ciudad': ciudades_base * 6,
    'Distrito': distritos_30
}

ventas_mr2 = pd.DataFrame(data)
ventas_mr2['Ventas'] = ventas_mr2['Precio'] * ventas_mr2['Cantidad']

# --- 3. GUARDAR EN ARCHIVO CSV ---
ventas_mr2.to_csv('ventas_misha_rastrera.csv', index=False, encoding='utf-8-sig')

print("-------------------------Dataset de Ventas Actualizado--------------------")
print(ventas_mr2.head(10))
print("\n¡Éxito! El archivo 'ventas_misha_rastrera.csv' ha sido guardado.")

# --- 4. GRÁFICOS ADICIONALES ---
plt.style.use('ggplot')

# Histograma de Ventas
plt.figure(figsize=(10, 6))
plt.hist(ventas_mr2['Ventas'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Ventas - Misha Rastrera')
plt.xlabel('Monto de Venta (Soles)')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión (Precio vs Cantidad)
plt.figure(figsize=(10, 6))
plt.scatter(ventas_mr2['Precio'], ventas_mr2['Cantidad'], color='green', alpha=0.6, s=100)
plt.title('Dispersión: Relación Precio vs Cantidad')
plt.xlabel('Precio (Soles)')
plt.ylabel('Cantidad Vendida')
plt.grid(True)
plt.show()