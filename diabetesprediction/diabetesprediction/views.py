import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from django.shortcuts import render
import seaborn as sns
sns.set()
def home(request):
    return render(request,'home.html')
def predict(request):
    return render(request,'predict.html')
def result(request):

    url = 'https://github.com/spandanasalian/dataset/blob/7ffd506a816b44a37c3ef92e713aeb0af5698982/diabetes.csv?raw=true'
    data = pd.read_csv(r'C:\Users\SPANDANA\Desktop\Mini Project\diabetes.csv')
    x = data.drop("Outcome", axis=1)
    y = data['Outcome']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)

    rf_model = RandomForestClassifier(n_estimators=100)
    rf_model.fit(x_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = rf_model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result1 = ""
    color1 = ""
    if pred == [1]:
        result1 = "Positive"
        color1 = "red"
    elif pred == [0]:
        result1 = "Negative"
        color1 = "green"
    else:
        result1 = "No results to show !"
        color1 = "Blue"


    return render(request,'predict.html',{"result2":result1,"color":color1})