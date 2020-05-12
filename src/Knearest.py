from sklearn import linear_model
from sklearn import tree 
from sklearn import naive_bayes 
from sklearn.neighbors import KNeighborsClassifier

import loaddata
import dataprep
import test1,test2,test3
Xdata,Ydata,XdataT,YdataT=loaddata.loaddata('E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow')
print(Xdata)
print(Ydata)
print(XdataT)
print(YdataT)
clf = KNeighborsClassifier()
clf.fit(Xdata,Ydata)
Prediction = clf.predict(XdataT)
Score = clf.score(XdataT,YdataT)
print("The Score of the K-Nearest Neighbours classifier is", Score * 100)