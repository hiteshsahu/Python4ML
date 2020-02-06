from sklearn import tree
from sklearn import svm

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],[190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


class ScikitLearn:
    """Example of Scikit learn to train model and then predict"""
    def __init__(self, classifier):
        self.clf = None
        self._classifier = classifier

    def trainModel(self, x, y):
        """train model with test data"""
        self.clf = self._classifier.fit(x, y)

    def predict(self, data):
        """predict data"""
        print(self.clf.predict(data))


# Decision tree Classifier
scikit = ScikitLearn(tree.DecisionTreeClassifier())
scikit.trainModel(X,Y)
scikit.predict([[190, 70, 43]])

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3


