from src.dataIngestion import DataIngestion
from src.preprocess import Datapreprocess
from src.train import Training
from src.loggerr import logger

class ModelPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        get_data = DataIngestion()
        get_data = get_data.data_ingestion()
        process_data = Datapreprocess()
        process_path = process_data.preprocess_data(get_data)
        train = Training()
        train.training(process_path)
        

if __name__ == "__main__":
    try:
        logger.info(" pipeline started !")
        obj = ModelPipeline()
        obj.main()
        logger.info("pipeline completed !")
    except Exception as e:
        logger.exception(e)
        raise e   

