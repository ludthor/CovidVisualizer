from sklearn.linear_model import Ridge

class MachineLearning():

    def __init__(self):
        self.model = None

    def train_model(self, X,y):
        lr = Ridge(alpha=0.5)
        lr.fit(X,y)
        print(lr)
        self.model = lr

    def predict(self, X):
        preds = self.model.predict(X)
        return preds




