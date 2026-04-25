from jobSalaryPrediction import logger
from jobSalaryPrediction.config import ConfigurationManager
from jobSalaryPrediction.components.data_transformation import DataTransform

STAGE_NAME = "Data Transformation Config"

class DataTransformPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_transform_config = config.get_data_transformation_config()
            data_transform = DataTransform(data_transform_config)
            data_transform.split_data()

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataTransformPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 