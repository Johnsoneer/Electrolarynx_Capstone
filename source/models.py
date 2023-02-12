
# Import Statements



class basicModel(object):
    """
    Parent class for future model objects.
    """
    def __init__(self):
        # TODO: Implement  basicModel object
        return None

    def train(self, X, y):
        """
        Trains model on input matrices

        :param X:
            Input matrix of features to make train our model on (X_train
        :param y:
            Corresponding actual text (y_train)
        :return:
            None
        """
        # TODO: implement basicModel.train()
        return None

    def score(self, X, y):
        """
        Return performance metric for model's prediction given X and y data to test.

        :param X:
            Input matrix of features to make predictions on (X_test)
        :param y:
            Corresponding actual text (y_test)
        :return:
            performance measurement of our choice (TBD)
        """
        # TODO: choose performance measurement for STT models
        # TODO: implement basicModel.score(X,y)
        return None

    def predict(self, X):
        """

        :param X:
            Input matrix of features to make predictions on (X_test)
        :return:
            matrix of predicted text.
        """
        # TODO: implement basicModel.train()
        return None