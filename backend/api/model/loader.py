import pandas as pd

class Loader:

    def load_data(self, url: str):
        """Carrega e retorna um DataFrame."""
        
        # Definindo os nomes das colunas
        headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", 
                   "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price", "Recomendadation"]
        
        return pd.read_csv(url, names=headers, header=0, skiprows=0, delimiter=',')











# class Loader:

#     def load_data(self, url: str, attributes: list):
#         """ Carrega e retorna um DataFrame. Há diversos parâmetros 
#         no read_csv que poderiam ser utilizados para dar opções 
#         adicionais.
#         """
        
#         return pd.read_csv(url, names=attributes, header=0,
#                            skiprows=0, delimiter=',') # Esses dois parâmetros são próprios para uso deste dataset. Talvez você não precise utilizar