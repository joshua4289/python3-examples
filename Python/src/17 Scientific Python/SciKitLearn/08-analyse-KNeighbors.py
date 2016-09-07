from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# load iris data set
iris = load_iris()
X = iris.data
Y = iris.target

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def predict(K, test_size):
    estimator = KNeighborsClassifier(n_neighbors=K)
    # split data into train and test
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=4)
    # train for different values of K
    estimator.fit(X_train, Y_train)
    # predict
    prediction = estimator.predict(X_test)
    # compare with actual
    return metrics.accuracy_score(Y_test, prediction)

# vary K
results = []
for K in range(1, 26):
    results.append(predict(K, 0.4))

set_title("plot the relationship between K and testing accuracy")
plt.plot(range(1, 26), results)
plt.xlabel('Value of K for KNN (test_size=0.4)')
plt.ylabel('Testing Accuracy')
plt.show()

# vary test_size
results = []
for test_size in np.arange(0.1, 1.0, 0.1):
    results.append(predict(10, test_size))

set_title("plot the relationship between test_size and testing accuracy")
plt.plot(np.arange(0.1, 1.0, 0.1), results)
plt.xlabel('Value of test_size (K=10)')
plt.ylabel('Testing Accuracy')
plt.show()


#     fig = plt.figure()
#     ax = Axes3D(fig)
#     surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False)
#     ax.set_title(cmap.name)
