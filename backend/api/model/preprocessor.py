import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

class PreProcessor:
    def __init__(self):
        self.encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

    def split_test_train(self, dataset, percentual_test, seed=7):
        # limpeza dos dados e eliminação de outliers
        # (implemente a lógica de limpeza e eliminação de outliers aqui)

        # feature selection
        # (implemente a lógica de feature selection aqui)

        # divisão em treino e teste
        x = dataset.drop(['Recomendado'], axis=1).values
        y = dataset['Recomendado'].values
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=percentual_test, shuffle=True, random_state=seed, stratify=y)
            
        return x_train, x_test, y_train, y_test

    def fit_transform_encoder(self, x_train):
        """Codifica e ajusta os dados de treino."""
        return self.encoder.fit_transform(x_train)

    def transform_encoder(self, x):
        """Transforma os dados de entrada."""
        return self.encoder.transform(x)

    def prepare_form(self, form):
        """Prepara os dados recebidos do front para serem usados no modelo."""
        if isinstance(form, np.ndarray):
            x_input = form  # Caso o form já seja um np.ndarray, podemos usá-lo diretamente.
        else:
            x_input = np.array(
                [
                    form.manufacturer,
                    form.category,
                    form.screen,
                    form.gpu,
                    form.os,
                    form.cpu_core,
                    form.screen_size_inch,
                    form.cpu_core,
                    form.ram_gb,
                    form.storage_gb,
                    form.weight_kg,
                    form.price,
                ]
            )
            x_input = x_input.reshape(1, -1)
        return x_input









