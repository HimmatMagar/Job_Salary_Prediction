from jobSalaryPrediction import logger
from jobSalaryPrediction.entity import *
from jobSalaryPrediction.utils import read_yaml, create_directory
from jobSalaryPrediction.constants import __config__, __params__, __schema__



class ConfigurationManager:

      def __init__(self, config = __config__, params = __params__, schema = __schema__):
            self.config = read_yaml(config)
            self.params = read_yaml(params)
            self.schema = read_yaml(schema)

            create_directory([self.config.artifact_dir])
            logger.info("Artifact directory created")


      def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_directory([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                  root_dir=config.root_dir,
                  data_source=config.data_source,
                  zip_file=config.zip_file,
                  unzip_file=config.unzip_file
            )

            return data_ingestion_config


      def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            create_directory([config.root_dir])

            schema = self.schema.COLUMNS

            data_validation_config = DataValidationConfig(
                  root_dir= config.root_dir,
                  data_path=config.data_path,
                  status_file=config.status_file,
                  schema=schema
            )

            return data_validation_config
      
      def get_data_transformation_config(self) -> DataTransformationConfig:
            config = self.config.data_transformation
            create_directory([config.root_dir])

            data_transformation_config = DataTransformationConfig(
                  root_dir=config.root_dir,
                  data_path=config.data_path
            )

            return data_transformation_config
      

      def get_model_building_config(self) -> ModelBuilingConfig:
            config = self.config.model_building

            create_directory([config.root_dir])
            params = self.params.model_params

            model_building_config = ModelBuilingConfig(
                  root_dir = config.root_dir,
                  xtrain_data = config.xtrain_data,
                  ytrain_data = config.ytrain_data,
                  model = config.model,
                  n_estimators = params.n_estimators,
                  max_depth = params.max_depth, 
                  subsample = params.subsample,
                  colsample_bytree =  params.colsample_bytree,
                  reg_alpha = params.reg_alpha,
                  reg_lambda = params.reg_lambda
            )

            return model_building_config
      

      def get_model_eval_config(self) -> ModelEvalConfig:
            config = self.config.model_evaluation
            create_directory([config.root_dir])

            model_eval_config = ModelEvalConfig(
                  root_dir = config.root_dir,
                  xval_file = config.xval_data,
                  yval_file = config.yval_data,
                  model = config.model,
                  metric = config.metric_file,
            )

            return model_eval_config