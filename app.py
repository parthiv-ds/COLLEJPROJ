from Harvestify.pipeline.prediction import PredictionPipeline1
from Fertilizer.pipeline.prediction import PredictionPipeline2
import os
import numpy as np   
from flask import Flask, render_template,request
import requests
import yaml
import json
import joblib

#http://api.openweathermap.org/data/2.5/weather?appid=9d7cde1f6d07ec55650544be1631307e&q=
#https://github.com/simranvolunesia/Irrigreat?tab=readme-ov-file


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = "9d7cde1f6d07ec55650544be1631307e"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None
    
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/crop',methods=['POST','GET'])
def home():
    return render_template("crop.html")

@app.route('/Fertilizer',methods=['POST','GET'])
def home1():
    return render_template("Fertilizer.html")

@app.route('/train1',methods=['GET'])  # route to train the pipeline
def training1():
    os.system("python main1.py")
    return "Training Successful!" 

@app.route('/train2',methods=['GET'])  # route to train the pipeline
def training2():
    os.system("python main2.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
            #  reading the inputs given by the user
            N = int(request.form['nitrogen'])
            P = int(request.form['phosphorous'])
            K = int(request.form['pottasium'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            city = str(request.form.get("city"))
            if weather_fetch(city) != None:
                temperature, humidity = weather_fetch(city)
                data = [N,P,K,temperature,humidity,ph,rainfall]
                data = np.array(data).reshape(1, 7)
                obj = PredictionPipeline1()
                predict = obj.predict(data)
                return render_template('cropresult.html', prediction = str(predict))

    else:
        return render_template('index.html')


@app.route('/predict2',methods=['POST','GET'])
def predict2():
    if request.method == 'POST':
            soil_jl = joblib.load('artifacts2/data_transformation/soil.joblib')
            crop_jl= joblib.load('artifacts2/data_transformation/crop.joblib')
            Fertilizer_jl = joblib.load('artifacts2/data_transformation/Fertilizer.joblib')
            #  reading the inputs given by the user
            temperature = int(request.form['temprature'])
            humidity = int(request.form['humidity'])
            Moisture = int(request.form['Moisture'])
            #city = str(request.form.get("city"))
            crop_data = request.form.get("crop")
            soil_data = request.form.get("soil")
            soil = soil_jl.get(soil_data,-1)
            crop = crop_jl.get(crop_data,-1)
            N = int(request.form['nitrogen'])
            P = int(request.form['phosphorous'])
            K = int(request.form['pottasium'])
            '''
            if weather_fetch(city) != None:
                temperature, humidity = weather_fetch(city)
            '''
            data = [temperature,humidity,Moisture,soil,crop,N,K,P]
            data = np.array(data).reshape(1, 8)
            obj = PredictionPipeline2()
            predict22 = obj.predict(data)
            predict2 = next((fertilizer for fertilizer,value  in Fertilizer_jl.items() if value == predict22),'Unknown')
            return render_template('Fertilizerresult.html', prediction = str(predict2))

    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)