from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

digits = load_digits()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

clf = Perceptron(max_iter=1000)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(X_test)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
