import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


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
        
        verify = dic2
        if self.list[14]=="Not Verified":
            output = output + list(verify.values())
        else:
            verify[self.list[14]]=True
            output = output + list(verify.values())
            
        app_type = dic3
        if self.list[15] == "DIRECT_PAY":
            output = output + list(dic3.values())          
        else:
            app_type[self.list[15]] =True
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
        # print("last-two")
        # print(output)
        # print("length:",len(output))

        # Train dataset for scaling purpose
        dataf = pd.read_csv("/Users/akshayshendre/Desktop/Apploan/models/df1.csv")
        dataf = dataf.drop("Unnamed: 0", axis=1)
        X = dataf.values
        # print(X.shape)
        scaler = MinMaxScaler()
        scaled_array = scaler.fit_transform(X)

        # Converting output list into dataframe
        df = pd.DataFrame([output], columns=['loan_amnt', 'term', 'int_rate', 'installment', 'annual_inc', 'dti',
                                             'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc',
                                             'mort_acc', 'pub_rec_bankruptcies', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2',
                                             'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4',
                                             'D5', 'E1', 'E2', 'E3', 'E4', 'E5', 'F1', 'F2', 'F3', 'F4', 'F5', 'G1',
                                             'G2', 'G3', 'G4', 'G5', 'verification_status_Source Verified',
                                             'verification_status_Verified', 'application_type_INDIVIDUAL',
                                             'application_type_JOINT', 'initial_list_status_w',
                                             'purpose_credit_card', 'purpose_debt_consolidation',
                                             'purpose_educational', 'purpose_home_improvement', 'purpose_house',
                                             'purpose_major_purchase', 'purpose_medical', 'purpose_moving',
                                             'purpose_other', 'purpose_renewable_energy', 'purpose_small_business',
                                             'purpose_vacation', 'purpose_wedding', 'OTHER', 'OWN', 'RENT',
                                             'zipcode', 'earliest_cr_year'])
        # print(df, "\n")
        array = df.values

        # print(array)
        array = array.reshape(1,-1)
        scaled_array = scaler.transform(array)
        scaled_array = scaled_array.reshape(1,-1)
        # print("scaled",scaled_array)
        return scaled_array         

class Prediction:
    def __init__(self):
        # self.array = input_array
        pass
    
    def predict(self,input_array):
        model = load_model("models/model.h5")
        # print(model.summary())
        pred = model.predict(input_array)
        # print(pred, "\n")
        pred = np.where(pred[0][0] >0.5, 1,0)
        return pred
            
if __name__=="__main__":
    lis = [40000, 36, 11.44, 265.66, 31789.88,22.05, 17.0, 3., 20131., 53.3, 27., 3., 3., "A2", "Source Verified", "INDIVIDUAL", "w", "home_improvement", "OTHER", 22690, 2004]
    processed = Preprocess(lis)
    X_array = processed.out_array()
    Predictor = Prediction()
    pred = Predictor.predict(X_array)
    # print(pred[0][0])
    # print("\n", pred)
    # pred = np.where(pred[0][0] >0.5, 1,0)
    print("Predicited value",pred)