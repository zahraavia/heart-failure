import pandas as pd
import numpy as np
import streamlit as st
import sklearn
from sklearn.preprocessing import LabelEncoder

#Load the Dataset
hfailure = pd.read_csv ("heart.csv")

le = LabelEncoder()
hfailure['Sex']=le.fit_transform(hfailure['Sex'])
hfailure['ChestPainType']=le.fit_transform(hfailure['ChestPainType'])
hfailure['FastingBS']=le.fit_transform(hfailure['FastingBS'])
hfailure['ExerciseAngina']=le.fit_transform(hfailure['ExerciseAngina'])
hfailure['RestingECG']=le.fit_transform(hfailure['RestingECG'])
hfailure['ST_Slope']=le.fit_transform(hfailure['ST_Slope'])

#Define X and Y

X = hfailure.drop('HeartDisease',axis=1)
Y = hfailure['HeartDisease']

## Splitting X and y into training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4,
                                                    random_state=1)


st.title("Do I Have a Heart Failure?")

#Input Data 1

Sex = st.selectbox("Sex",
('Female','Man'))
'You selected', Sex

if Sex=="Female":
    Sex=0
else:
    Sex=1

#Input Data 2
Age = st.text_input("Age")

#Input Data 3
RestingBP = st.text_input("Resting Blood Pressure (mm Hg)")

#Input Data 4
ChestPainType = st.selectbox("Chest Pain Type",
('Asymptomatic', 'Non-Anginal Pain', 'Atypical Angina', 'Typical Angina'))

if ChestPainType=="Asymptomatic":
    ChestPainType=0
elif ChestPainType=='Non-Anginal Pain':
    ChestPainType=2
elif ChestPainType=='Typical Angina':
    ChestPainType==3
else:
    ChestPainType=1

#Input Data 5
Cholesterol = st.text_input("Serum Cholestrol (mm/dl)")

#Input Data 6
MaxHR = st.slider("Maximum Heart Rate Achieved",int(X.MaxHR.min()),int(X.MaxHR.max()))

#Input Data 7
FastingBS = st.selectbox("Fasting Blood Sugar",
('Fasting BS > 120 mg/dl', 'Otherwise'))

if FastingBS=='120 mg/dl':
    FastingBS=1
else:
    FastingBS=0

#Input Data 8
RestingECG = st.selectbox("Resting Electrocardiogram Results",
('Normal','LVH','ST'))

if RestingECG=='LVH':
    RestingECG=0
if RestingECG=='Normal':
   RestingECG=1
else:
    RestingECG=2


#Input Data 9
ExerciseAngina = st.selectbox("Exercise-Induced Angina",
('Yes', 'No'))

if ExerciseAngina=='Yes':
    ExerciseAngina=1
else:
    ExerciseAngina=0

#Input Data 10
Oldpeak = st.slider("Depression Numerical Value",int(X.Oldpeak.min()),int(X.Oldpeak.max()))

#Input Data 11
ST_Slope =  st.selectbox("The slope of the peak exercise ST segment",
('Upsloping', 'Down', 'Flat'))

if ST_Slope =='Upsloping':
    ST_Slope =2
if ST_Slope=='Down':
    ST_Slope=0
else:
    ST_Slope =1

## training model

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr = lr.fit(X_train, Y_train)

#Output data

if st.button("Heart Failure Diagnosis"):
        result=lr.predict([[Age, Sex, ChestPainType, RestingBP,
       Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina,
       Oldpeak, ST_Slope]])
    
        if (result[0]==0):
            st.success("I dont have a heart failure.")
        else:
            st.warning("I have a heart failure.")
    




