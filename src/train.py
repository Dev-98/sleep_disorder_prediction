from logger import logger
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

STAGE_NAME  = "Training"

class Training:
    def _init_(self) -> None:
        pass
    def main(self):
        X_train, X_test, y_train, y_test = train_test_split(preprocess_data.drop('Sleep Disorder',axis=1), preprocess_data['Sleep Disorder'], test_size=0.2, random_state=42)
        dtree = DecisionTreeClassifier()
        dtree.fit(X_train, y_train)
        print("Training Accuracy:",dtree.score(X_train,y_train))
        y_pred = dtree.predict(X_test)
        print("Testing Accuracy:", accuracy_score(y_pred, y_test))
        print("classification report:", classification_report(y_test, y_pred))
        
        
# if _name_ == "_main_":

try:
    logger.info(f" >>>> stage {STAGE_NAME} <<<< started !")
    obj3 = Training()
    obj3.main()
    logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
    
except Exception as e:
    logger.exception(e)
    raise e