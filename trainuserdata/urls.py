from django.contrib import admin  
from django.urls import path

from . import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.home, name='home'),  
    path('uploadform/', views.model_form_upload, name='model_form_upload'),
    path('ajax/create-train-model', views.create_train_model, name='create_train_model'),
    path('ajax/predict-model-data', views.predict_model_data, name='predict_model_data'),
    
]  