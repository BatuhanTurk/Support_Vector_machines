import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import cv2

warnings.filterwarnings('ignore')
sns.set()

sayilar = pd.read_csv("train.csv")

bir = sayilar.iloc[2,1:]
bir = bir.values.reshape(28,28)
plt.imshow(bir)
plt.title("Rakam: 1")
#plt.show()

X = sayilar.drop("label",axis = 1)
y = sayilar["label"]

X = scale(X)

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, train_size=0.2,test_size = 0.8, random_state = 101)



print('X_egitim boyutları:',X_egitim.shape)
print('y_egitim boyutları:',y_egitim.shape)
print('X_test boyutları:',X_test.shape)
print('y_test boyutları:',y_test.shape,"\n")


model_linear = SVC(kernel='linear')

model_linear.fit(X_egitim, y_egitim)

tahmin = model_linear.predict(X_test)

print("Doğruluk oranı:", metrics.accuracy_score(y_true=y_test, y_pred=tahmin), "\n")

"""
model_poly = SVC(kernel='poly')

model_poly.fit(X_egitim,y_egitim)

tahmin = model_poly.predict(X_test)

print("Doğruluk oranı:", metrics.accuracy_score(y_true=y_test, y_pred=tahmin), "\n")


model_rbf = SVC(kernel='rbf')

model_rbf.fit(X_egitim,y_egitim)

tahmin = model_rbf.predict(X_test)

print("Doğruluk oranı:", metrics.accuracy_score(y_true=y_test, y_pred=tahmin), "\n")


model_rbf = SVC(kernel='rbf',gamma = 0.001,C = 10)

model_rbf.fit(X_egitim,y_egitim)

tahmin = model_rbf.predict(X_test)

print("Doğruluk oranı:", metrics.accuracy_score(y_true=y_test, y_pred=tahmin), "\n")
"""
def resimOku(path):
	img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
	img = img.flatten()
	img = img.reshape(1,-1)
	return img
	
tahmin_edilecek_veri = resimOku("Images/resim_0.png")
tahmin = model_linear.predict(tahmin_edilecek_veri)
print("Tahmin Sonucu :",str(tahmin[0]))