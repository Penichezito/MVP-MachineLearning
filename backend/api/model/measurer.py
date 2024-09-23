from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:

    def measurer(model, x_test, y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predictions = Model.preditor(model, x_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(y_test, predictions)
                