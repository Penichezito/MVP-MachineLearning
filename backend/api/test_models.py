import pytest
import pandas as pd
from model import Model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar dados de teste
data = pd.read_csv('./MachineLearning/data/test.csv') 
x = data.drop('Recomendado', axis=1)
y = data['Recomendado']

# Dividir os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=7)

# Criar uma instância do modelo
model = Model()

# Testes
def test_model_train():
    """Testa se o modelo pode ser treinado."""
    model.train(x_train, y_train)
    assert model.model is not None

def test_model_predict():
    """Testa se o modelo pode fazer previsões."""
    model.train(x_train, y_train)
    predictions = model.predict(x_test)
    assert len(predictions) == len(x_test)

def test_model_accuracy():
    """Testa a acurácia do modelo."""
    model.train(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy > 0.7 # Defina o limite de acurácia desejado
