from mlProject.logging import logger
from mlProject.pipeline.step_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from mlProject.pipeline.step_02_data_validation_pipeline import DataValidationTrainingPipeline
from mlProject.pipeline.step_03_data_transformation_pipeline import DataTransformationTrainingPipeline
from mlProject.pipeline.step_04_model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation Statge"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} Start <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Compelete <<<<<<<\n\nx==========x\n")

    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Data Transformation Statge"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} Start <<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Compelete <<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model trainer Statge"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} Start <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Compelete <<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e