from jobSalaryPrediction import logger
from jobSalaryPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from jobSalaryPrediction.pipeline.data_validation_pipeline import DataValidationPipeline
from jobSalaryPrediction.pipeline.data_transformation_pipeline import DataTransformPipeline
from jobSalaryPrediction.pipeline.model_building_pipeline import BuildModelPipeline

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


STAGE_NAME = "Data Transformation Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataTransformPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Model Building Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = BuildModelPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e