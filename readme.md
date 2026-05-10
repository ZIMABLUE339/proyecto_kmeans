## Proyecto K-Means: Análisis de Agrupamiento Web

Este proyecto es una aplicación web interactiva diseñada para realizar análisis de datos utilizando el algoritmo de agrupamiento K-Means. Permite cargar conjuntos de datos y visualizar de forma gráfica cómo se agrupan los elementos según sus características.

## Características

Interfaz Web: Construida con HTML y CSS para una experiencia de usuario intuitiva.
Algoritmo K-Means: Implementado en Python para el procesamiento de clusters.
Visualización: El sistema procesa los datos y devuelve resultados visuales a través de plantillas dinámicas.

## Tecnologías Utilizadas

Backend: Python.
Framework Web: Flask.
Frontend: HTML y CSS
Librerías sugeridas: Pandas, Scikit-learn, Matplotlib (gestionadas en requirements.txt).

## Estructura del Proyecto

proyecto_kmeans/
├── data/           # Archivos de datos de entrada (CSVs)
├── static/         # Archivos estáticos (CSS, imágenes)
├── templates/      # Plantillas HTML para la interfaz web
├── .gitignore      # Archivos y carpetas ignorados por Git
├── app.py          # Lógica principal del servidor y algoritmo
└── requirements.txt # Dependencias necesarias para ejecutar el proyecto


## Instalación y Ejecución

Clonar el repositorio:
Instalar las dependencias: Se recomienda usar un entorno virtual:
Iniciar la aplicación:
Luego, abre tu navegador en http://localhost:5000 (o el puerto que indique la consola).

## Sobre el Conjunto de Datos

El sistema utiliza el dataset **"Sample Superstore"**, un conjunto de datos clásico utilizado para el análisis de ventas minoristas y el comportamiento del consumidor.

*   **Fuente:** [Kaggle - EDA on Sample Superstore Data Set](https://www.kaggle.com/datasets/prixpam/eda-on-sample-superstore-data-set-using-mysql)
*   **Contenido:** El archivo contiene registros de transacciones de una tienda departamental, incluyendo detalles sobre:
    *   **Geografía:** Ciudad, Estado, Región.
    *   **Producto:** Categoría (Tecnología, Muebles, etc.) y Subcategoría.
    *   **Métricas de Rendimiento:** Ventas, Cantidad, Descuento y Ganancia (Profit).

### Aplicación de K-Means en estos datos
En este proyecto, aplicamos el algoritmo K-Means sobre este dataset para identificar **segmentos de mercado** o **perfiles de clientes**. Esto permite al sistema agrupar automáticamente las transacciones o productos que comparten características similares de rentabilidad y volumen de ventas, facilitando la toma de decisiones estratégicas.

### Ubicación de los Datos
El archivo CSV principal del sistema se escuentra en la carpeta ../data/