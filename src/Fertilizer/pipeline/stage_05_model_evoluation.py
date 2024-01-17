from Fertilizer.config.configuration import ConfigurationManager
from Fertilizer.components.model_evoluation import ModelEvaluation
from Fertilizer import logger


STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config2 = ConfigurationManager()
        model_evaluation_config = config2.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config2=model_evaluation_config)
        model_evaluation_config.save_results()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
