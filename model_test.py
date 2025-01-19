import pickle

#labels for iris dataset
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

# test data
# 6.5,2.8,4.6,1.5 -> versicolor
# 4.5,2.3,1.3,0.3 -> setosa
# 6.7,3.3,5.7,2.5 -> virginica

#load the model and test with a custom input
model = pickle.load( open('model.pkl','rb'))
x = [[4.5,2.3,1.3,0.3]]
predict = model.predict(x)
print(predict[0], "->", labels[predict[0]])