# MlWeb

**The machine Learning based Web app with asynchrobous training with Celery
**
It is assumed that the Explanatory Data Analysis is performed on data

used to test the following algorithms:

1 	Logistic Regression

2 	Logistic Regression CV

3 	Bagging

4 	Support Vector Machine

5 	Random Forest


It can be run in Ubunto and Fedora

the app is developer by Django Framework

# Configuration of Celery:
for celery we configured the celery with Rabitmq server 

the results are saved in Redis DataBase

in celery_conf.py file:

I choosed my timezone for Tehran, you can change it based on your area:

CELERY_TIMEZONE = 'Asia/Tehran' #Europe/London


# Installation steps:
install Redis from link:

https://redis.io/topics/quickstart

install Rabbitmq:

https://www.rabbitmq.com/install-debian.html

pip install -r requirements.txt


# running from local:
this app can be run in local as following steps:

after activating the virtual environment:

python managage.py runserver

celery -A communereML worker -l INFO

to see the results on realtime, you can run flower as follow:

celery -A communereML flower



# use the Web :
after running the local server:

go to http://127.0.0.1:8000/

upload the dataset(csv format):

the dataset must be classification dataset and with only two classes, also the last column must have 'output' column for the outputs


after uploading the dataset, select the dataset or enter the id of dataset in dataset_id input

then select the algorithm, then click on Train, the model will be updated in trained models list


click the trained model, and then put the list of input features(separated by comma (,))

the click predict button

Note: the models saved in redis database will be removed after 1 hour(can be changed in celery_conf.py)

if you want to handle the model for long term, the file for model can be saved with joblib dump library

for example one dataset (file_1.csv) is uploaded 

one example for predicting is as follow:

0.626,-3.243,4.053,2.555,-1.149,0.865,1.955,-5.554,-2.206,-1.349,0.62,3.616,-2.388,-2.206,-0.791,1.719,2.324,-1.562,2.13,3.763

expected output: 0

-3.978,0.633,-0.13,0.064,2.078,1.901,-1.781,-0.066,-0.282,-1.836,-1.336,2.634,0.838,1.225,-0.293,0.814,2.301,0.287,-0.815,1.792

expected output:1
