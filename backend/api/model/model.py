from model.preprocessor import PreProcessor
from sklearn.neighbors import KNeighborsClassifier
import pickle

class Model:
    """Modela os dados."""

    def __init__(self):
        self.model = None
        self.preprocessor = PreProcessor()

    def load_model(self, path):
        if path.endswith('/backend/api/MachineLearning/pipelines/pipeline.pkl'):
            with open(path, 'rb') as file:
                self.model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return self.model

    def train(self, x_train, y_train):
        """Treina o modelo com os dados fornecidos."""
        x_train_encoded = self.preprocessor.fit_transform_encoder(x_train)
        x_train_processed = self.preprocessor.prepare_form(x_train_encoded)
        self.model = KNeighborsClassifier(metric='euclidean', n_neighbors=7)
        self.model.fit(x_train_processed, y_train)

    def predict(self, x):
        """Realiza a predição com o modelo treinado."""
        if self.model is None:
            raise Exception("Modelo não treinado. Treine o modelo antes de fazer previsões.")
        x_encoded = self.preprocessor.transform_encoder(x)
        x_processed = self.preprocessor.prepare_form(x_encoded)
        return self.model.predict(x_processed)

















# class Model:
    
#     # TODO: Guardar model como atributo e o preditor receber as entradas.
#     # TODO: preditor -> realiza_predicao
    
#     def load_model(self, path):
#         """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
#         """
        
#         if path.endswith('.api/MachineLearning/pipeline/pipeline.pkl'):
#             with open(path, 'rb') as file:
#                 model = pickle.load(file)
#         else:
#             raise Exception('Formato de arquivo não suportado')
#         return model
    
#     def predictor(self, model, x_input):
#         """Realiza a predição de um laptop com base no modelo treinado
#         """
#         diagnosis = model.predictor(x_input)
#         return diagnosis