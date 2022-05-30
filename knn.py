import basic
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

df = basic.create_training_set()

df = df[["Age", "Gender", "Student", "Confident", "Happy", "Addicted"]]
df["Age"].replace({"0-15": 0, "16-19": 1, "20-24": 2, "28 +": 3}, inplace=True)
df["Gender"].replace({"kobieta": 0, "mężczyzna": 1}, inplace=True)
df["Confident"].replace({"not confident": 0, "semi-confident": 1, "confident": 2}, inplace=True)
df["Happy"].replace({"not happy": 0, "semi-happy": 1, "happy": 2}, inplace=True)
print(df)
print("\n\n")
X = df.iloc[:, :-1]
y = df.iloc[:, 5]
print(X)  # attributes
print("\n\n")
print(y)  # labels
print("\n\n")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=5, algorithm="ball_tree", metric="minkowski")
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(y_pred)

cm = confusion_matrix(y_test, y_pred)
ac = round(accuracy_score(y_test, y_pred), 2)
print("\n\n")
print(cm)
print("\n\n")
print(ac)
