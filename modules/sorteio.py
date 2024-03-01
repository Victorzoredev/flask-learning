import pandas as pd
import numpy as np

def process_sorteio(file_stream):
    # Lendo o arquivo Excel
    df = pd.read_excel(file_stream)
    
    # Gerando valores aleatórios de 1 até N para cada linha
    n = len(df)
    df['Sorteio'] = np.random.choice(range(1, n + 1), n, replace=False)
    
    # Retornando o DataFrame modificado
    return df
