from django.contrib import admin

from .models import  (
    DataSet,
    MLModel,
    )

@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'dataset', 'description')


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'model_name', 'model_async_id','model_parameters','model_param_values')

