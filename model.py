#!/usr/bin/env python
# coding: utf-8
import pickle
from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target

#labels for iris dataset
#labels ={
#  0: "setosa",
#  1: "versicolor",
#  2: "virginica"
#}

#split the data set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.15)

#Using decision tree algorithm
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)

#export the model
pickle.dump(classifier, open('model.pkl','wb'))