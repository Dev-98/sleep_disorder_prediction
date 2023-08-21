import pandas as pd
from logger import logger

STAGE_NAME  = "Data Ingestion Stage"

class DataIngestion:
    def __init__(self) -> None:
        pass
    def main(self):

        df = pd.read_csv("data/sleep-dataset.csv")
        
        return df
        
# if __name__ == "__main__":
    
try:
    logger.info(f" >>>> stage {STAGE_NAME} <<<< started !")
    obj = DataIngestion()
    data = obj.main()
    logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
    
except Exception as e:
    logger.exception(e)
    raise e