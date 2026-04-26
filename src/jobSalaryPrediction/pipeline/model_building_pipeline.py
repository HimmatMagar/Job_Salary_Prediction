import os
import mlflow
import mlflow.sklearn
from jobSalaryPrediction import logger
from jobSalaryPrediction.config import ConfigurationManager
from jobSalaryPrediction.components.model_building import BuildModel
from jobSalaryPrediction.utils.mlflow_config import configure_mlflow, save_run_id

STAGE_NAME = "Model Building Stage"

class BuildModelPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_build_config = config.get_model_building_config()

            configure_mlflow(experiment_name="JobSalaryPrediction")

            with mlflow.start_run(run_name="XGB-Model") as run:
                  try:
                        mlflow.log_params({
                              "n_estimators": model_build_config.n_estimators,
                              "max_depth": model_build_config.max_depth, 
                              "subsample": model_build_config.subsample,
                              "colsample_bytree":  model_build_config.colsample_bytree,
                              "reg_alpha": model_build_config.reg_alpha,
                              "reg_lambda": model_build_config.reg_lambda
                        })
                        model = BuildModel(model_build_config)
                        model_xgb = model.build_model_architecture()
                        print(f"model built: {model_xgb}")
                        
                        logged_model = mlflow.sklearn.log_model(
                              sk_model=model_xgb,
                              artifact_path="model"
                        )
                        with open("artifact/model_id.txt", "w") as f:
                              f.write(logged_model.model_id)
                        logger.info(f"Model logged successfully and id saved in artifact/model_id")

                        vecPath = "artifact/data_transformation/pipeline.pkl"
                        print(f"vectorizer exists: {os.path.exists(vecPath)}")
                        mlflow.log_artifact(
                              local_path    = vecPath,
                              artifact_path = "pipeline"
                        )

                        save_run_id(run.info.run_id)
                  except Exception as e:
                        print(f"Training Failed {e}")
                        raise e




if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = BuildModelPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 