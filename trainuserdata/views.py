from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.http import  require_POST, require_GET
from django.http import JsonResponse
import pandas as pd
from celery.result import AsyncResult

from .models import (
    DataSet,
    MLModel,
    )

from .train_algorithms import TrainAlgorithm
from .forms import DatasetForm


def home(request):
    contex = {}
    datasets = DataSet.objects.all()
    models = MLModel.objects.filter(user__exact = request.user).select_related('user')
    contex['datasets'] = datasets
    contex['models'] = models
    return render(request, 'home.html', contex)

def model_form_upload(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DatasetForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

@require_POST
def create_train_model(request):
    allinfo = request.POST 
    data_set_id = allinfo['dataset_id']
    model_name = allinfo['model_name']

    selected_dataset = DataSet.objects.get(id__exact = data_set_id)
    dataset_path = selected_dataset.dataset.path
    if dataset_path:
        dataset = pd.read_csv(dataset_path)
        x_train = dataset.loc[:,dataset.columns!='output']
        y_train = dataset['output']
    else:
        return JsonResponse({'error': 'selected dataset id is not correct.'}, status=400)

    train_obj = TrainAlgorithm(x_train,y_train)

    if model_name == 'Logistic Regression':
        model_async_id = train_obj.train_logistic_regression()
    elif model_name == 'Bagging':
        model_async_id = train_obj.train_bagging()
    elif model_name == 'Support Vector Machine':
        model_async_id = train_obj.train_svm()
    elif model_name == 'Logistic Regression CV':
        model_async_id = train_obj.train_logistic_regression_cv()
    elif model_name == 'Random Forest':
        model_async_id = train_obj.train_random_forest()
    
    #create model
    mdl = MLModel.objects.create(
        user = request.user,
        model_dataset = selected_dataset,
        model_name = model_name,
        model_async_id = model_async_id,
        model_parameters = '',
        model_param_values = '',
    )
    mdl.save()
    models = MLModel.objects.filter(user__exact = request.user)

    return render(request, 'trained_models_partial.html', {'models':models})

@require_GET
def predict_model_data(request):
    all_info = request.GET
    context = {}
    model_id = all_info['model_id']
    input_test_data = all_info['input_test_data']
    input_test_data = [float(x) for x in input_test_data.split(',')]

    model_async_id = MLModel.objects.get(id = model_id).model_async_id

    loaded_model = AsyncResult(model_async_id)
    model_state = loaded_model.state
    if model_state == 'SUCCESS':
        loaded_model = loaded_model.result
        predicted_result = str(loaded_model.predict([input_test_data])[0])
        context['predicted_result'] = predicted_result
        return render(request, 'prediction_result_partial.html', context)
    elif model_state == 'PENDING':
        MLModel.objects.get(id = model_id).delete()
        models = MLModel.objects.filter(user__exact = request.user).select_related('user')
        t = loader.get_template('trained_models_partial.html')
        context['t'] =  t.render({'models': models})
        context['error'] = 'selected model was expired and removed from database'
        return JsonResponse(context, status=400)
    else:
        MLModel.objects.get(id = model_id).delete()
        models = MLModel.objects.filter(user__exact = request.user).select_related('user')
        t = loader.get_template('trained_models_partial.html')        
        context['t'] =  t.render({'models': models})
        return JsonResponse(context, status=400)
