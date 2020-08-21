from keras.models import model_from_json
import pandas as pd

json_file = open('/home/adizz/Desktop/MAJOR/DATASETS/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/home/adizz/Desktop/MAJOR/DATASETS/model.h5")
print("Loaded model from disk")
print("Enter input for model")
N=int(input("Enter N1 speed : "))/100
m=int(input("Enter N2 speed : "))/100
P1=int(input("Enter inlet pressure : "))/100
T1=int(input("Enter inlet temprature : "))/100
P3=int(input("Enter outlet pessure : "))/100
T3=int(input("Enter outlet temparature : "))/1000
TJC=int(input("Enter TJC : "))/1000
input_list=[N,m,P1,T1,P3,T3,TJC]
input_df=pd.DataFrame([input_list])
input_df.columns =['N','m','P1','T1','P3','T3','TJC']
pred=loaded_model.predict(input_df)
pred=pred*100
print("Predicted Resonance Amplitude : ",pred[0][0])