from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.svm import SVC
from sklearn.ensemble import (
BaggingClassifier,
RandomForestClassifier,
)


from .tasks import shared_train


class TrainAlgorithm:

    def __init__(self,x_train,y_train):
        self.x_train = x_train
        self.y_train = y_train

    def train_logistic_regression(self):
        """
        penalty:{'l1', 'l2'}, default='l2'
        c: Regularizarion parameter
        solver:‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones.
        ‘sag’ only handle L2 penalty, whereas ‘liblinear’ and ‘saga’ handle L1 penalty
        """
        x_train = self.x_train
        y_train = self.y_train
        model = LogisticRegression(penalty='l2', C=2, solver='liblinear')
        model = shared_train.delay(model, x_train, y_train)
        return model.id

    def train_logistic_regression_cv(self):
        """
        Cs: describes the inverse of regularization strength
        cv : number of folds
        penalty{‘l1’, ‘l2’}, default=’l2’
        solver:‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones.
        ‘sag’ only handle L2 penalty, whereas ‘liblinear’ and ‘saga’ handle L1 penalty
        """
        model = LogisticRegressionCV(penalty='l1', Cs=[1.5, 2, 3, 4, 5], solver='liblinear',scoring='roc_auc')
        x_train = self.x_train
        y_train = self.y_train

        model = shared_train.delay(model, x_train, y_train)
        return model.id

    def train_svm(self):
        """"
        c: Regularization parameter
        kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}
        degree: polynomial degree

        in this program, We assumed the poly kernel and degree of 4
        """
        x_train = self.x_train
        y_train = self.y_train
        model = SVC(kernel = 'poly', degree = 4, C = 1000)
        model = shared_train.delay(model, x_train,y_train)
        return model.id

    def train_bagging(self):
        """
        max_features:The number of features to draw from X to train each base estimator
        n_estimators:The number of base estimators in the ensemble
        """
        x_train = self.x_train
        y_train = self.y_train
        model = BaggingClassifier(max_features = 4, n_estimators = 500)
        model = shared_train.delay(model, x_train,y_train)
        return model.id
    
    def train_random_forest(self):
        """
        n_estimators: the number of trees in the forest
        min_samples_split:The minimum number of samples required to split an internal node:
        min_samples_leaf :The minimum number of samples required to be at a leaf node.
        max_features: int, then consider `max_features`, at each split, float: fraction of features
        ccp_alpha:Minimal Cost-Complexity Pruning
        """
        x_train = self.x_train
        y_train = self.y_train
        model = RandomForestClassifier(n_estimators=500,min_samples_split = 10,min_samples_leaf=5, ccp_alpha=0.02, max_features = 0.7)
        model = shared_train.delay(model, x_train,y_train)
        return model.id
