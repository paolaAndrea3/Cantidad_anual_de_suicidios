# Análisis Interactivo de Suicidios en Antioquia (2005-2022)

Este proyecto es una aplicación interactiva desarrollada con **Streamlit** que permite analizar los datos de suicidios reportados en el departamento de Antioquia entre los años 2005 y 2022. La aplicación incluye filtros por rango de años, regiones y códigos de región, y muestra los datos filtrados en una tabla interactiva.

## Características principales
- **Visualización interactiva**: Permite explorar los datos de manera dinámica.
- **Filtros avanzados**: Filtra los datos por año, región y código de región.
- **Interfaz amigable**: Diseñada para ser fácil de usar, incluso para personas sin experiencia técnica.

---

## Requisitos previos
Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:
1. **Python 3.8 o superior**: Descárgalo desde [python.org](https://www.python.org/downloads/).
2. **Pip**: El gestor de paquetes de Python (generalmente viene incluido con Python).
3. **Git** (opcional): Para clonar el repositorio desde GitHub.

---

## Pasos para ejecutar la aplicación

### 1. Descargar el proyecto
#### Opción 1: Usando Git
Si tienes Git instalado, abre una terminal y ejecuta:
```bash
git clone https://github.com/paolaAndrea3/Cantidad_anual_de_suicidios.git
```

#### Opción 2: Descarga manual
Si no tienes Git, sigue estos pasos:
1. Ve al repositorio en GitHub: [Cantidad_anual_de_suicidios](https://github.com/paolaAndrea3/Cantidad_anual_de_suicidios.git).
2. Haz clic en el botón verde **Code** y selecciona **Download ZIP**.
3. Extrae el archivo ZIP en una carpeta de tu computadora.

---

### 2. Abrir una terminal
1. Abre una terminal (puedes usar **CMD**, **PowerShell** o **Terminal** en macOS/Linux).
2. Navega a la carpeta donde descargaste el proyecto. Por ejemplo:
   ```bash
   cd C:\Users\usuario\Downloads\Cantidad_anual_de_suicidios
   ```

---

### 3. Crear un entorno virtual (opcional pero recomendado)
Un entorno virtual te ayuda a evitar conflictos con otras dependencias de Python instaladas en tu sistema.

1. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   ```
2. Activa el entorno virtual:
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

---

### 4. Instalar las dependencias
Instala las bibliotecas necesarias para ejecutar la aplicación:
```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar la aplicación
Ejecuta la aplicación con el siguiente comando:
```bash
streamlit run Inicio.py
```

---

### 6. Abrir la aplicación en el navegador
Después de ejecutar el comando anterior, Streamlit abrirá automáticamente la aplicación en tu navegador predeterminado. Si no se abre automáticamente, copia y pega la URL que aparece en la terminal (generalmente `http://localhost:8501`) en tu navegador.

---

## Estructura del proyecto
- **Inicio.py**: Archivo principal que contiene la interfaz de la aplicación.
- **assets/**: Carpeta que contiene las imágenes utilizadas en la aplicación.
- **static/datasets/**: Carpeta que contiene el archivo CSV con los datos de suicidios.
- **README.md**: Este archivo, con instrucciones para ejecutar el proyecto.

---

## Notas importantes
- Asegúrate de que el archivo de datos (`Cantidad_anual_de_suicidios_reportados_en_el_Departamento_de_Antioquia_desde_2005_20250506.csv`) esté en la carpeta `static/datasets`.
- Si encuentras algún error, verifica que todas las dependencias estén instaladas correctamente y que las rutas de los archivos sean correctas.

---

## Créditos
Este proyecto fue desarrollado por:
- **Kevin Olivella**
- **Marvin García**
- **Paola Murillo**

Repositorio oficial: [GitHub](https://github.com/paolaAndrea3/Cantidad_anual_de_suicidios.git)