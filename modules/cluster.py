import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def process_cluster(file_stream):
    # Lendo o arquivo Excel
    df = pd.read_excel(file_stream)
    
    # Supondo que todas as colunas exceto 'id' sejam características para clusterização
    features = df.drop('id', axis=1)
    
    # Normalizando as características
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Aplicando K-Means
    kmeans = KMeans(n_clusters=3)  # Definir o número de clusters conforme necessário
    df['cluster'] = kmeans.fit_predict(features_scaled)
    
    # Retornando o DataFrame modificado
    return df
