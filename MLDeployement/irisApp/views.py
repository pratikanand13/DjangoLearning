from django.shortcuts import render
from joblib import load

model = load('./Notebook/abc.joblib')


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Load your machine learning model here
# Example: model = load_model()

def predictor(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length', 0))
        sepal_width = float(request.POST.get('sepal_width', 0))
        petal_length = float(request.POST.get('petal_length', 0))
        petal_width = float(request.POST.get('petal_width', 0))

        # Make a prediction using the loaded model
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        y_pred = model.predict(features)

        # Map the predicted class to a flower species
        if y_pred[0] == 0:
            predicted_species = 'Setosa'
        elif y_pred[0] == 1:
            predicted_species = 'Versicolor'
        else:
            predicted_species = 'Virginica'

        return render(request, 'main.html', {'result': predicted_species})

    return render(request, 'main.html')

# def formInfo(request):
#     if request.method == 'GET':
#         sepal_length = float(request.GET.get('sepal_length', 0))
#         sepal_width = float(request.GET.get('sepal_width', 0))
#         petal_length = float(request.GET.get('petal_length', 0))
#         petal_width = float(request.GET.get('petal_width', 0))

#         # Make a prediction using the loaded model
#         features = [[sepal_length, sepal_width, petal_length, petal_width]]
#         y_pred = model.predict(features)

#         # Map the predicted class to a flower species
#         if y_pred[0] == 0:
#             predicted_species = 'Setosa'
#         elif y_pred[0] == 1:
#             predicted_species = 'Versicolor'
#         else:
#             predicted_species = 'Virginica'

#         return render(request, 'result.html', {'result': y_pred})

#     return render(request, 'result.html', {'result': 'Invalid input'})
