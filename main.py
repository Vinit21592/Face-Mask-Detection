from maskDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from maskDetection import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> satge {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e