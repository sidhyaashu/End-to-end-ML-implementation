from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path
from mlProject.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model evaluation Statge"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()