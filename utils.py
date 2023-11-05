import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


dic1 = {'A2':False,'A3':False,'A4':False,'A5':False,'B1':False,'B2':False,'B3':False,'B4':False,'B5':False,'C1':False,'C2':False,'C3':False,
            'C4':False,'C5':False,'D1':False,'D2':False,'D3':False,'D4':False,'D5':False,'E1':False,'E2':False,'E3':False,'E4':False,'E5':False,
            'F1':False,'F2':False,'F3':False,'F4':False,'F5':False,'G1':False,'G2':False,'G3':False,'G4':False,'G5':False
            }
dic2 = {'Source Verified':False,'Verified':False}
dic3 = {'INDIVIDUAL':False,'JOINT':False}
dic4 = {"w":False}
dic5 = {"credit_card":False,"debt_consolidation":False,"educational":False,"home_improvement":False,"house":False,"major_purchase":False,
        "medical":False,"moving":False, "other":False, "renewable_energy":False,"small_business":False,"vacation":False,"wedding":False }
dic6 = {'OTHER':False,'OWN':False,'RENT':False}




class Preprocess:
    def __init__(self, feature_list):
        self.list = feature_list
    def out_array(self):
        output =[]
        for num in range(0,13):
            output.append(self.list[num])
        subgrade = dic1
        if self.list[13] == "A1":
            output = output + list(dic1.values())
        else:
            subgrade[self.list[13]] =True
            output = output + list(subgrade.values())

        verification = dic2
        if self.list[14] == "Not Verified":
            output = output + list(dic2.values())
        else:
            verification[self.list[14]] =True
            output = output + list(verification.values())

        app_type = dic3
        if self.list[15] == "DIRECT_PAY":
            output = output + list(dic3.values())
        else:
            verification[self.list[15]] =True
            output = output + list(app_type.values())

        lis_status = dic4
        if self.list[16]=='f':
            output = output + list(dic4.values())
        else:
            lis_status[self.list[16]] = True
            output = output + list(lis_status.values())

        purpose = dic5
        if self.list[17]=="car":
            output= output + list(dic5.values())
        else:
            purpose[self.list[17]]=True
            output = output + list(purpose.values())

        ownership = dic6
        if self.list[18]=="MORTGAGE":
            output = output + list(dic6.values())
        else:
            ownership[self.list[18]]=True
            output = output + list(ownership.values())

        output = output + list(self.list[19:])
        output_array = np.array(output)
        scaler = StandardScaler()
        output_array = scaler.transform(output_array)
        return output_array        

class Model:
    def __init__(self,input_array):
        self.array = input_array
    def predict(self):
        model = load_model("models/model.h5")
        pred = model.predict(self.array)
        return pred
            
    