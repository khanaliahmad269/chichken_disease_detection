from chicken_disease_prediction.config.configuration import ConfigurationManager
from chicken_disease_prediction.components.evaluation import Evaluation
from chicken_disease_prediction import logger
from pathlib import Path
import traceback

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        print("An error occurred:", str(e))
        traceback.print_exc()
        raise
    
            