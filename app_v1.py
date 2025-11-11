import streamlit as st
import pandas as pd

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(page_title="Proyecto Sprint 1 - EDA", layout="centered")

st.title("📊 Proyecto Sprint 1 — Exploratory Data Analysis (EDA)")
st.markdown("""
Este proyecto muestra cómo limpiar, transformar y resumir datos de usuarios.
A continuación, se presentan los pasos realizados en el análisis, junto con el código ejecutado y su resultado.
""")

# ==============================
# PASO 1: Limpiar nombre de usuario
# ==============================
st.header("Paso 1 — Limpieza de nombres")
st.write("Eliminamos espacios y reemplazamos el guion bajo por un espacio.")

code_step1 = """
user_name = ' mike_reed '
user_name = user_name.strip()
user_name = user_name.replace('_', ' ')
user_name
"""
st.code(code_step1, language="python")

user_name = ' mike_reed '
user_name = user_name.strip()
user_name = user_name.replace('_', ' ')
st.success(f"Resultado: {user_name}")

# ==============================
# PASO 2: Separar nombre y apellido
# ==============================
st.header("Paso 2 — Separar nombre y apellido")
st.write("Convertimos el nombre completo en una lista con nombre y apellido.")

code_step2 = """
user_name_list = user_name.split(' ')
user_name_list
"""
st.code(code_step2, language="python")

user_name_list = user_name.split(' ')
st.success(f"Resultado: {user_name_list}")

# ==============================
# PASO 3: Conversión de edad
# ==============================
st.header("Paso 3 — Conversión de edad a entero")
st.write("Convertimos la edad a un número entero, manejando errores.")

code_step3 = """
user_age = 'treinta y dos'

try:
    user_age_int = int(user_age)
except:
    user_age_int = None
    print('Please provide your age as a numerical value.')
"""
st.code(code_step3, language="python")

user_age = 'treinta y dos'
try:
    user_age_int = int(user_age)
except:
    st.error("Please provide your age as a numerical value.")

# ==============================
# PASO 4: Total de gastos
# ==============================
st.header("Paso 4 — Cálculo del total gastado")
st.write("Sumamos los montos gastados en las diferentes categorías.")

code_step4 = """
spendings_per_category = [894, 213, 173]
total_amount = sum(spendings_per_category)
total_amount
"""
st.code(code_step4, language="python")

spendings_per_category = [894, 213, 173]
total_amount = sum(spendings_per_category)
st.success(f"Total amount spent: {total_amount}")

# ==============================
# PASO 5: Crear resumen del usuario
# ==============================
st.header("Paso 5 — Cadena de resumen del usuario")
st.write("Creamos un resumen con la información del usuario en una cadena formateada.")

code_step5 = """
user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

final_string = f"User {user_id} is {user_name[0].capitalize()}, who is {user_age} years old."
final_string
"""
st.code(code_step5, language="python")

user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32
final_string = f"User {user_id} is {user_name[0].capitalize()}, who is {user_age} years old."
st.success(final_string)

# ==============================
# PASO 6: Lista de usuarios
# ==============================
st.header("Paso 6 — Conteo de usuarios registrados")
st.write("Calculamos el número de usuarios registrados en la base de datos.")

code_step6 = """
users = [
 ['32415', 'mike reed', 32.0],
 ['31980', 'kate morgan', 24.0],
 ['32156', 'john doe', 37.0],
]

user_info = f"We have received data from {len(users)} clients."
user_info
"""
st.code(code_step6, language="python")

users = [
 ['32415', 'mike reed', 32.0],
 ['31980', 'kate morgan', 24.0],
 ['32156', 'john doe', 37.0],
]
st.success(f"We have received data from {len(users)} clients.")