from flask import Flask, render_template, request,jsonify
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
import joblib
import  pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
df=pd.read_csv('Dataset_new.csv')
df.drop(columns=['Model_rank', 'fuel_rank'],axis=1,inplace=True)
df=df.rename(columns={'Company Name':'Company_Name','Car Age': 'Car_Age' })
df_cont = df[['Car_Age','km']]
df_cat=df[['Company_Name','location','Model', 'fuel','Owner']]
df_dum=pd.get_dummies(df_cat,drop_first=True)
X=pd.merge(df_cont,df_dum,on=df_cat.index)
y= df[['price']]



#model = pickle.load(open('car_sell_xgbr_best_model.pkl', 'rb'))
model = pickle.load(open("car_sell_xgbr_best_model.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
        
    if request.method == 'POST':
        Company = str(request.form['Company'])
		
        Company_Honda=0
        Company_Hyundai=0
        Company_Mahindra=0
        Company_Maruti_Suzuki=0
        Company_Renault=0
        Company_Skoda=0
        Company_Tata=0
        Company_Toyota=0
        Company_Volkswagen=0
        if(Company=='Honda'):
            Company_Honda=1
        elif(Company=='Hyundai'):
            Company_Hyundai=1
        elif(Company=='Mahindra'):
            Company_Mahindra=1
        elif(Company=='Maruti_Suzuki'):
            Company_Maruti_Suzuki=1
        elif(Company=='Renault'):
            Company_Renault=1
        elif(Company=='Skoda'):
            Company_Skoda=1
        elif(Company=='Tata'):
            Company_Tata=1
        elif(Company=='Toyota'):
            Company_Toyota=1
        elif(Company=='Volkswagen'):
            Company_Volkswagen=1
        
		
        km=int(request.form['km'])
        
        carName=str(request.form['carName'])
        carName_A_Star=0
        carName_Accord=0
        carName_Alphard=0
        carName_Alto=0
        carName_Altroz=0
        carName_Alturas=0
        carName_Amaze=0
        carName_Ameo=0
        carName_Aria=0
        carName_Aspire=0
        carName_BR_V=0
        carName_Baleno=0
        carName_Beetle=0
        carName_Bolero=0
        carName_Bolt=0
        carName_Brio=0
        carName_CR_V=0
        carName_Camry=0
        carName_Captur=0
        carName_Celerio=0
        carName_Ciaz=0
        carName_City=0
        carName_Civic=0
        carName_Classic=0
        carName_Corolla=0
        carName_Creta=0
        carName_Cross=0
        carName_Duster=0
        carName_Dzire=0
        carName_EcoSport=0
        carName_Eeco=0
        carName_Elantra=0
        carName_Elite=0
        carName_Endeavour=0
        carName_Eon=0
        carName_Ertiga=0
        carName_Estilo=0
        carName_Etios=0
        carName_Fiesta=0
        carName_Figo=0
        carName_Fluence=0
        carName_Fluidic=0
        carName_Fortuner=0
        carName_GTI=0
        carName_Getz=0
        carName_Grand=0
        carName_Harrier=0
        carName_Hexa=0
        carName_Ignis=0
        carName_Ikon=0
        carName_Indica=0
        carName_Indigo=0
        carName_Innova=0
        carName_Jazz=0
        carName_Jetta=0
        carName_KUV100=0
        carName_Kodiaq=0
        carName_Koleos=0
        carName_Kona=0
        carName_Kwid=0
        carName_Land=0
        carName_Laura=0
        carName_Lodgy=0
        carName_Manza=0
        carName_Marazzo=0
        carName_Mobilio=0
        carName_Nano=0
        carName_Nexon=0
        carName_NuvoSport=0
        carName_Octavia=0
        carName_Omni=0
        carName_Passat=0
        carName_Polo=0
        carName_Pulse=0
        carName_Quanto=0
        carName_Rapid=0
        carName_Ritz=0
        carName_S_Cross=0
        carName_SX4=0
        carName_Safari=0
        carName_Santa=0
        carName_Santro=0
        carName_Scorpio=0
        carName_Sonata=0
        carName_Sumo=0
        carName_Superb=0
        carName_Swift=0
        carName_TUV300=0
        carName_Thar=0
        carName_Tiago=0
        carName_Tigor=0
        carName_Tiguan=0
        carName_Triber=0
        carName_Tucson=0
        carName_Vento=0
        carName_Venue=0
        carName_Verna=0
        carName_Vitara=0
        carName_WR_V=0
        carName_Wagon=0
        carName_XL6=0
        carName_XUV300=0
        carName_XUV500=0
        carName_Xcent=0
        carName_Xylo=0
        carName_Yaris=0
        carName_Yeti=0
        carName_Zen=0
        carName_Zest=0
        carName_e2o=0
        carName_i10=0
        carName_i20=0
        
        if(carName=='A-Star'):
            carName_A_Star=1
        elif(carName=='Accord'):
            carName_Accord=1
        elif(carName=='Alphard'):
            carName_Alphard=1
        elif(carName=='Alto'):
            carName_Alto=1
        elif(carName=='Altroz'):
            carName_Altroz=1
        elif(carName=='Alturas'):
            carName_Alturas=1
        elif(carName=='Amaze'):
            carName_Amaze=1
        elif(carName=='Ameo'):
            carName_Ameo=1
        elif(carName=='Aria'):
            carName_Aria=1
        elif(carName=='Aspire'):
            carName_Aspire=1
        elif(carName=='BR-V'):
            carName_BR_V=1
        elif(carName=='Baleno'):
            carName_Baleno=1
        elif(carName=='Beetle'):
            carName_Beetle=1
        elif(carName=='Bolero'):
            carName_Bolero=1
        elif(carName=='Bolt'):
            carName_Bolt=1
        elif(carName=='Brio'):
            carName_Brio=1
        elif(carName=='CR-V'):
            carName_CR_V=1
        elif(carName=='Camry'):
            carName_Camry=1
        elif(carName=='Captur'):
            carName_Captur=1
        elif(carName=='Celerio'):
            carName_Celerio=1
        elif(carName=='Ciaz'):
            carName_Ciaz=1
        elif(carName=='City'):
            carName_City=1
        elif(carName=='Civic'):
            carName_Civic=1
        elif(carName=='Classic'):
            carName_Classic=1
        elif(carName=='Corolla'):
            carName_Corolla=1
        elif(carName=='Creta'):
            carName_Creta=1
        elif(carName=='Cross'):
            carName_Cross=1
        elif(carName=='Duster'):
            carName_Duster=1
        elif(carName=='Dzire'):
            carName_Dzire=1
        elif(carName=='EcoSport'):
            carName_EcoSport=1
        elif(carName=='Eeco'):
            carName_Eeco=1
        elif(carName=='Elantra'):
            carName_Elantra=1
        elif(carName=='Elite'):
            carName_Elite=1
        elif(carName=='Endeavour'):
            carName_Endeavour=1
        elif(carName=='Eon'):
            carName_Eon=1
        elif(carName=='Ertiga'):
            carName_Ertiga=1
        elif(carName=='Estilo'):
            carName_Estilo=1
        elif(carName=='Etios'):
            carName_Etios=1
        elif(carName=='Fiesta'):
            carName_Fiesta=1
        elif(carName=='Figo'):
            carName_Figo=1
        elif(carName=='Fluence'):
            carName_Fluence=1
        elif(carName=='Fluidic'):
            carName_Fluidic=1
        elif(carName=='Fortuner'):
            carName_Fortuner=1
        elif(carName=='GTI'):
            carName_GTI=1
        elif(carName=='Getz'):
            carName_Getz=1
        elif(carName=='Grand'):
            carName_Grand=1
        elif(carName=='Harrier'):
            carName_Harrier=1
        elif(carName=='Hexa'):
            carName_Hexa=1
        elif(carName=='Ignis'):
            carName_Ignis=1
        elif(carName=='Ikon'):
            carName_Ikon=1
        elif(carName=='Indica'):
            carName_Indica=1
        elif(carName=='Indigo'):
            carName_Indigo=1
        elif(carName=='Innova'):
            carName_Innova=1
        elif(carName=='Jazz'):
            carName_Jazz=1
        elif(carName=='Jetta'):
            carName_Jetta=1
        elif(carName=='KUV100'):
            carName_KUV100=1
        elif(carName=='Kodiaq'):
            carName_Kodiaq=1
        elif(carName=='Koleos'):
            carName_Koleos=1
        elif(carName=='Kona'):
            carName_Kona=1
        elif(carName=='Kwid'):
            carName_Kwid=1
        elif(carName=='Land'):
            carName_Land=1
        elif(carName=='Laura'):
            carName_Laura=1
        elif(carName=='Lodgy'):
            carName_Lodgy=1
        elif(carName=='Manza'):
            carName_Manza=1
        elif(carName=='Marazzo'):
            carName_Marazzo=1
        elif(carName=='Mobilio'):
            carName_Mobilio=1
        elif(carName=='Nano'):
            carName_Nano=1
        elif(carName=='Nexon'):
            carName_Nexon=1
        elif(carName=='NuvoSport'):
            carName_NuvoSport=1
        elif(carName=='Octavia'):
            carName_Octavia=1
        elif(carName=='Omni'):
            carName_Omni=1
        elif(carName=='Passat'):
            carName_Passat=1
        elif(carName=='Polo'):
            carName_Polo=1
        elif(carName=='Pulse'):
            carName_Pulse=1
        elif(carName=='Quanto'):
            carName_Quanto=1
        elif(carName=='Rapid'):
            carName_Rapid=1
        elif(carName=='Ritz'):
            carName_Ritz=1
        elif(carName=='S-Cross'):
            carName_S_Cross=1
        elif(carName=='SX4'):
            carName_SX4=1
        elif(carName=='Safari'):
            carName_Safari=1
        elif(carName=='Santa'):
            carName_Santa=1
        elif(carName=='Santro'):
            carName_Santro=1
        elif(carName=='Scorpio'):
            carName_Scorpio=1
        elif(carName=='Sonata'):
            carName_Sonata=1
        elif(carName=='Sumo'):
            carName_Sumo=1
        elif(carName=='Superb'):
            carName_Superb=1
        elif(carName=='Swift'):
            carName_Swift=1
        elif(carName=='TUV300'):
            carName_TUV300=1
        elif(carName=='Thar'):
            carName_Thar=1
        elif(carName=='Tiago'):
            carName_Tiago=1
        elif(carName=='Tigor'):
            carName_Tigor=1
        elif(carName=='Tiguan'):
            carName_Tiguan=1
        elif(carName=='Triber'):
            carName_Triber=1
        elif(carName=='Tucson'):
            carName_Tucson=1
        elif(carName=='Vento'):
            carName_Vento=1
        elif(carName=='Venue'):
            carName_Venue=1
        elif(carName=='Verna'):
            carName_Verna=1
        elif(carName=='Vitara'):
            carName_Vitara=1
        elif(carName=='WR-V'):
            carName_WR_V=1
        elif(carName=='Wagon'):
            carName_Wagon=1
        elif(carName=='XL6'):
            carName_XL6=1
        elif(carName=='XUV300'):
            carName_XUV300=1
        elif(carName=='XUV500'):
            carName_XUV500=1
        elif(carName=='Xcent'):
            carName_Xcent=1
        elif(carName=='Xylo'):
            carName_Xylo=1
        elif(carName=='Yaris'):
            carName_Yaris=1
        elif(carName=='Yeti'):
            carName_Yeti=1
        elif(carName=='Zen'):
            carName_Zen=1
        elif(carName=='Zest'):
            carName_Zest=1
        elif(carName=='e2o'):
            carName_e2o=1
        elif(carName=='i10'):
            carName_i10=1
        elif(carName=='i20'):
            carName_i20=1
		
        carAge=int(request.form['Age'])
        owner=int(request.form['Owner'])
        owner_2=0
        owner_3=0
        owner_4=0
        if(owner=='2'):
            owner_2=1
        elif(owner=='3'):
            owner_3=1
        elif(owner=='4'):
            owner_4=1
            
        fuel=request.form['Fuel_Type_Petrol']
        fuel_Diesel=0
        fuel_Electric=0
        fuel_LPG=0
        fuel_Petrol=0
      
        if(fuel=='Diesel'):
            fuel_Diesel=1
        elif(fuel=='Electric'):
            fuel_Electric=1
        elif(fuel=='LPG'):
            fuel_LPG=1
        elif(fuel=='Petrol'):
            fuel_Petrol=1

       #probelm###
        prediction=[[km,carAge,owner_2,owner_3,owner_4,carName_A_Star,carName_Accord,carName_Alphard,carName_Alto
		,carName_Altroz
	    ,carName_Alturas
		,carName_Amaze
		,carName_Ameo
		,carName_Aria
		,carName_Aspire
		,carName_BR_V
		,carName_Baleno
        ,carName_Beetle
        ,carName_Bolero
        ,carName_Bolt
        ,carName_Brio
        ,carName_CR_V
        ,carName_Camry
        ,carName_Captur
        ,carName_Celerio
        ,carName_Ciaz
        ,carName_City
        ,carName_Civic
        ,carName_Classic
        ,carName_Corolla
        ,carName_Creta
        ,carName_Cross
        ,carName_Duster
        ,carName_Dzire
        ,carName_EcoSport
        ,carName_Eeco
        ,carName_Elantra
        ,carName_Elite
        ,carName_Endeavour
        ,carName_Eon
        ,carName_Ertiga
        ,carName_Estilo
        ,carName_Etios
        ,carName_Fiesta
        ,carName_Figo
        ,carName_Fluence
        ,carName_Fluidic
        ,carName_Fortuner
        ,carName_GTI
        ,carName_Getz
        ,carName_Grand
        ,carName_Harrier
        ,carName_Hexa
        ,carName_Ignis
        ,carName_Ikon
        ,carName_Indica
        ,carName_Indigo
        ,carName_Innova
        ,carName_Jazz
        ,carName_Jetta
        ,carName_KUV100
        ,carName_Kodiaq
        ,carName_Koleos
        ,carName_Kona
        ,carName_Kwid
        ,carName_Land
        ,carName_Laura
        ,carName_Lodgy
        ,carName_Manza
        ,carName_Marazzo
        ,carName_Mobilio
        ,carName_Nano
        ,carName_Nexon
        ,carName_NuvoSport
        ,carName_Octavia
        ,carName_Omni
        ,carName_Passat
        ,carName_Polo
        ,carName_Pulse
        ,carName_Quanto
        ,carName_Rapid
        ,carName_Ritz
        ,carName_S_Cross
        ,carName_SX4
        ,carName_Safari
        ,carName_Santa
        ,carName_Santro
        ,carName_Scorpio
        ,carName_Sonata
        ,carName_Sumo
        ,carName_Superb
        ,carName_Swift
        ,carName_TUV300
        ,carName_Thar
        ,carName_Tiago
        ,carName_Tigor
        ,carName_Tiguan
        ,carName_Triber
        ,carName_Tucson
        ,carName_Vento
        ,carName_Venue
        ,carName_Verna
        ,carName_Vitara
        ,carName_WR_V
        ,carName_Wagon
        ,carName_XL6
        ,carName_XUV300
        ,carName_XUV500
        ,carName_Xcent
        ,carName_Xylo
        ,carName_Yaris
        ,carName_Yeti
        ,carName_Zen
        ,carName_Zest
        ,carName_e2o
        ,carName_i10
        ,carName_i20
        ,Company_Honda
        ,Company_Hyundai
        ,Company_Mahindra
        ,Company_Maruti_Suzuki
        ,Company_Renault
        ,Company_Skoda
        ,Company_Tata
        ,Company_Toyota
        ,Company_Volkswagen
        ,fuel_Diesel
        ,fuel_Electric
        ,fuel_LPG
        ,fuel_Petrol]]
        final_features = np.array(prediction).reshape(1, -1)
        prediction1 = model.predict(final_features)
        output=round(prediction1[0],2)

        prediction_text = 'Sorry you cannot sell this car'
        
       
        if output<0:
            prediction_text="Sorry you cannot sell this car"
        else:
            prediction_text="You can sell the Car at {} lakhs".format(output)

        response = jsonify({
            'message': prediction_text
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)