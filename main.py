from jobSalaryPrediction import logger
from jobSalaryPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from jobSalaryPrediction.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Validation Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataValidationPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e