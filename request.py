import requests
# Change the value of experience that you want to test
url = 'http://127.0.0.1:5000/api'
#feature = [[5.1, 3.5, 1.4, 0.2]]
#feature = [[6.1, 2.8, 4.0, 1.3]]
feature = [[4.5,2.3,1.3,0.3]]
#labels ={
#  0: "versicolor",
#  1: "versicolor",
#  2: "virginica"
#}

r = requests.post(url,json={'feature': feature})
print(r.json())