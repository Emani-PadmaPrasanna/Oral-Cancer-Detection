from django.shortcuts import render,redirect
import pandas as pd
from .models import OralPrediction
from django.http import HttpResponse, request

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')    

    
def predict(request):
    features = request.session["features"]
    model = pd.read_pickle('hello.pickle')
    classification = model.predict([features])
    obj = OralPrediction(
        tumor_size=features[0],
        tobacco_use=features[1],
        alcohol_consumption=features[2],
        reverse_smoking=features[3],
        restricted_mouth_opening=features[4],
        gender=features[5],
        age_group=features[6],
        classification=classification[0]
    )
    obj.save()

    return render(request, 'predict.html', {'classification_result': classification[0]})

def home(request):
    if request.method == "POST":
       	tumor_size = request.POST['tumor_size']
        tobacco_use = request.POST['tobacco_use']
        alcohol_consumption = request.POST['alcohol_consumption']
        reverse_smoking = request.POST['reverse_smoking']
        restricted_mouth_opening = request.POST['restricted_mouth_opening']
        gender = request.POST['gender']
        age_group = request.POST['age_group']
        request.session["features"] = [	tumor_size, tobacco_use, alcohol_consumption, reverse_smoking,restricted_mouth_opening, gender, age_group]
        return redirect(predict)
    return render(request, 'home.html')

def db_record(request):
    Oral_predictions = OralPrediction.objects.all()

    context = {
        'Oral_records': Oral_predictions
    }

    return render(request, 'database.html', context)

def delete(request, pk):
    Oral_data = OralPrediction.objects.get(id=pk)
    Oral_data.delete()
    return redirect('records')

