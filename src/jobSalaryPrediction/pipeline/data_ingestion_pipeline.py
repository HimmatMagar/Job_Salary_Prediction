from jobSalaryPrediction import logger
from jobSalaryPrediction.config import ConfigurationManager
from jobSalaryPrediction.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Config"

class DataIngestionPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 