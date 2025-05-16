from chicken_disease_prediction import logger 
from chicken_disease_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_prediction.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chicken_disease_prediction.pipeline.stage_03_training import ModelTrainingPipeline
from chicken_disease_prediction.pipeline.stage_04_evaluation import EvaluationPipeline
import traceback


STAGE_NAME= " Data Ingestion Stage"

try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME= "Prepare Base Model "
try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e    



STAGE_NAME = "Training"
try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print("An error occurred:", str(e))
        traceback.print_exc()
        raise


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        print("An error occurred:", str(e))
        traceback.print_exc()
        raise
        