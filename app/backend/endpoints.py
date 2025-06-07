from flask import Flask,request,jsonify
import json
import pickle
import numpy as np
import os
application=Flask(__name__)
app=application

# print(os.getcwd())
# print("loading..")
model=pickle.load(open('../../models/model.pkl','rb'))
scaler=pickle.load(open('../../models/scaler.pkl','rb'))

@app.route('/predict-fwi',methods=['POST'])
def predict():
    # take inputs
    try:
        inputLabels=request.get_json()
        if not inputLabels:
            return jsonify({"error":"Invalid Input"})
        else:
            scaled_input=scaler.transform(np.reshape([inputLabels['day'], inputLabels['month'], inputLabels['Temperature'], inputLabels['RH'], inputLabels['Ws'], inputLabels['Rain'], inputLabels['FFMC'], inputLabels['DMC'], inputLabels['ISI'],inputLabels[
       'Region']],(1,10)))
            fwi=model.predict(scaled_input)[0]
        return jsonify({"fwi":fwi,"error":None})
    except Exception as e:
        print(e)
        return jsonify({"error":"Unknown Error"})

    
if __name__ == '__main__':
    app.run(debug=True)