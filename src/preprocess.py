from dataIngestion import data
from logger import logger
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


STAGE_NAME  = "Data Preprocessing"

class Datapreprocess:
    def __init__(self) -> None:
        pass
    def main(self):
        data['Sleep Disorder'].fillna('None', inplace=True)
        data.drop('Person ID', axis=1, inplace=True)
                #spliting the blood pressure into two columns
        data['systolic_bp'] = data['Blood Pressure'].apply(lambda x: x.split('/')[0])
        data['diastolic_bp'] = data['Blood Pressure'].apply(lambda x: x.split('/')[1])
        #droping the blood pressure column
        data.drop('Blood Pressure', axis=1, inplace=True)
        data['BMI Category'] = data['BMI Category'].replace('Normal Weight', 'Normal')
              
        label_encoder = preprocessing.LabelEncoder()
        data["Gender"] = label_encoder.fit_transform(data["Gender"])
        data["Occupation"] = label_encoder.fit_transform(data["Occupation"])
        data["BMI Category"] = label_encoder.fit_transform(data["BMI Category"])
        data["Sleep Disorder"] = label_encoder.fit_transform(data["Sleep Disorder"])
        
        preprocess_data = data
        
        return preprocess_data
        

    
try:
    logger.info(f" >>>> stage {STAGE_NAME} <<<< started !")
    obj = Datapreprocess()
    preprocess_data = obj.main()
    logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
    
except Exception as e:
    logger.exception(e)
    raise e