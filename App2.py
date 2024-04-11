#pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np
import secrets
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",
                   page_title="Ciclo y Sena",
                   page_icon=":chart_with_upwards_trend:")

st.set_option('deprecation.showPyplotGlobalUse', False)

# DataFrame de ejemplo
data = {'usuarios': ['usuario1', 'usuario2', 'usuario3'],
        'contrasenas': ['pass1', 'pass2', 'pass3'],  # Guarda las contraseñas de forma segura en un entorno de producción
        'carrera': ['Psicología', 'Ing.Comercial', 'Medicina']}
df = pd.DataFrame(data)

# Agregar una imagen en la columna 2
img_url = 'https://th.bing.com/th/id/OIP.xLXmc4CdNcfRYJ_Qb5DXoAHaHa?w=165&h=180&c=7&r=0&o=5&pid=1.7'  # Reemplaza con la URL de tu imagen
st.image(img_url, width=100)  

titulo_login = 'Inicio de sesión'
st.title(titulo_login)

col1, col2 = st.columns([1, 2])
   
   # Página de inicio de sesión
def login_page():
    username = col1.text_input('Usuario')
    password = col1.text_input('Contraseña', type='password')
    login_button = col1.button('Iniciar sesión')
   
    if login_button:
        # Verificar credenciales
        user_data = df[df['usuarios'] == username]
        if not user_data.empty and user_data['contrasenas'].iloc[0] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.password = password
            return True
        else:
            st.warning('Credenciales incorrectas')
        return False

        if st.session_state.logged_in == True:
            titulo_login = 'sin titulo'
        else:
            titulo_login = 'Inicio'
           
# Función para cerrar la sesión
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.password = None

# Página principal después del inicio de sesión
def main_page():
    titulo_login = None
    st.title(f'Bienvenido(a), {st.session_state.username}!')
    opcion = st.sidebar.selectbox("Elige una opción", ["Ciclo", "SENA"])
    valor = st.sidebar.slider("Selecciona un valor", 0, 100, 50)
    st.write(f"Has seleccionado la opción: {opcion}")
    st.write(f"El valor seleccionado es: {valor}")
    # Filtrar DataFrame por nombre de usuario
    user_data = df[df['usuarios'] == st.session_state.username]
    
    # Mostrar datos filtrados
    st.write('Datos del usuario:')
    st.dataframe(user_data)

# Aplicación principal
def main():
    # Barra lateral con el botón de cerrar sesión
    if st.sidebar.button('Cerrar sesión'):
        logout()

    # Verificar el inicio de sesión
    if not st.session_state.get('logged_in'):
        login_page()
    else:
        main_page()

if __name__ == '__main__':
    main()

# Agregar una selección de opciones en la barra lateral


# Agregar una barra deslizante en la barra lateral


data2 = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro', 'Sofía', 'Luis', 'Elena', 'Marta', 'Daniel'],
    'Edad': [25, 30, 22, 28, 35, 27, 29, 31, 26, 33],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Zaragoza', 'Málaga', 'Alicante', 'Murcia', 'Granada'],
    'Puntuación': [85, 92, 78, 88, 90, 87, 84, 91, 79, 94]
}

df2 = pd.DataFrame(data2)
# Utilizando st.write()
#st.write(df2)

# Barra lateral para filtrar por ciudad
ciudad_elegida = st.sidebar.selectbox("Selecciona una ciudad", df2['Ciudad'].unique())

# Barra lateral para seleccionar múltiples ciudades
ciudades = st.sidebar.multiselect("Selecciona ciudades", df2['Ciudad'].unique())

# Filtrar el DataFrame según la ciudad seleccionada
filtered_df = df2[df2['Ciudad'].isin(ciudades)]

filtered_df2 = df2[df2.Ciudad==ciudad_elegida]

# Mostrar la tabla filtrada
st.dataframe(filtered_df)

st.dataframe(filtered_df2)
# Mostrar resultados en el cuerpo principal de la aplicación

def color_survived(val):
    color = 'blue' if val else 'red'
    return f'background-color: {color}'

st.dataframe(df2.style.applymap(color_survived, subset=['Edad']))

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    try:
        st.image("https://th.bing.com/th/id/OIP.xLXmc4CdNcfRYJ_Qb5DXoAHaHa?w=165&h=180&c=7&r=0&o=5&pid=1.7", width=200) # I changed here on purpose to raise an error
    except FileNotFoundError:
        st.text("File not found")

with tab2:
    st.header("A dog")
    try:
        st.image("https://th.bing.com/th/id/OIP.xLXmc4CdNcfRYJ_Qb5DXoAHaHa?w=165&h=180&c=7&r=0&o=5&pid=1.7", width=200)
    except FileNotFoundError:
        st.text("File not found")

with tab3:
    st.header("An owl")
    try:
        st.image("https://th.bing.com/th/id/OIP.xLXmc4CdNcfRYJ_Qb5DXoAHaHa?w=165&h=180&c=7&r=0&o=5&pid=1.7", width=200)
    except FileNotFoundError:
        st.text("File not found")
        
        
# Genera algunos datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crea un DataFrame de Pandas con los datos
data = {'X': x, 'Y1': y1, 'Y2': y2, 'Y3': y3}
df = pd.DataFrame(data) 
        # Define tres columnas
col1, col2, col3 = st.columns(3)

# Grafica en la primera columna
with col1:
    st.subheader('Gráfico 1')
    plt.plot(df['X'], df['Y1'])
    st.pyplot()

# Grafica en la segunda columna
with col2:
    st.subheader('Gráfico 2')
    plt.plot(df['X'], df['Y2'])
    st.pyplot()

# Grafica en la tercera columna
with col3:
    st.subheader('Gráfico 3')
    plt.plot(df['X'], df['Y3'])
    st.pyplot()
    


