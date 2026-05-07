import os
import matplotlib
matplotlib.use('Agg')  # Necesario para correr en servidores web
from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

app = Flask(__name__)

# Asegurar que las carpetas existan
os.makedirs('static/images', exist_ok=True)

def ejecutar_modelo_kmeans():
    # 1. Carga y Limpieza (Fase 3 del informe)
    df = pd.read_csv('data/Sample_Superstore_Cleaned_UTF8.csv')
    df = df.drop_duplicates()
    df = df.dropna(subset=['Sales', 'Profit', 'Quantity', 'Discount'])
    
    # Conversión de fechas
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    
    # 2. Preparación de variables
    features = ['Sales', 'Profit', 'Quantity', 'Discount']
    X = df[features].copy()
    
    # Estandarización (Z-score)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 3. Aplicación de K-Means (K=4 justificado por el Método del Codo)
    kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # 4. Generación de Gráficas Profesionales
    if not os.path.exists('static/images/metodo_codo.png'):
        inercias = []
        rango_k = range(1, 11)
        for k in rango_k:
            km_temp = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, random_state=42)
            km_temp.fit(X_scaled)
            inercias.append(km_temp.inertia_)
        
        plt.figure(figsize=(8, 4))
        plt.plot(rango_k, inercias, marker='o', linestyle='-', color='#2E75B6', linewidth=2)
        plt.axvline(x=4, color='#ED7D31', linestyle='--', label='K Óptimo (K=4)')
        plt.title('Método del Codo para selección de K', fontweight='bold')
        plt.xlabel('Número de Clústeres (K)')
        plt.ylabel('Inercia (WCSS)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.savefig('static/images/metodo_codo.png', dpi=150)
        plt.close()
    # --- PCA 2D Visualization ---
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    
    plt.figure(figsize=(10, 6))
    colors = ['#2E75B6', '#ED7D31', '#70AD47', '#D9534F']
    for i in range(4):
        mask = df['Cluster'] == i
        plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[i], label=f'Clúster {i}', alpha=0.6, s=25)
    
    centroids_pca = pca.transform(kmeans.cluster_centers_)
    plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], c='black', marker='X', s=200, label='Centroides')
    
    plt.title('Segmentación de Clientes (Espacio PCA 2D)', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.savefig('static/images/pca_clusters.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- Heatmap de Centroides ---
    plt.figure(figsize=(8, 4))
    sns.heatmap(pd.DataFrame(kmeans.cluster_centers_, columns=features), 
                annot=True, fmt='.2f', cmap='RdYlGn', center=0, linewidths=0.5)
    plt.title('Influencia de Variables por Clúster', fontweight='bold')
    plt.savefig('static/images/heatmap.png', dpi=150, bbox_inches='tight')
    plt.close()

    return df, kmeans, scaler, features

@app.route('/')
def index():
    df, kmeans, scaler, features = ejecutar_modelo_kmeans()
    
    # Datos para las tablas
    # Centroides en escala real
    centroides_reales = scaler.inverse_transform(kmeans.cluster_centers_)
    tabla_centroides = pd.DataFrame(centroides_reales, columns=features).round(2)
    tabla_centroides.insert(0, 'ID Clúster', range(4))

    # Muestra de datos con su clúster
    muestra_datos = df[['Order ID', 'Category', 'Sales', 'Profit', 'Quantity', 'Discount', 'Cluster']].head(15)

    return render_template('index.html', 
                           filas=muestra_datos.values.tolist(),
                           centroides=tabla_centroides.values.tolist(),
                           total=len(df))

if __name__ == '__main__':
    app.run(debug=True)