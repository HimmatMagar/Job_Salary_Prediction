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

            with mlflow.start_run(run_name="GBR-Model") as run:
                  try:
                        mlflow.log_params({
                              "n_estimators": model_build_config.n_estimators,
                              "learning_rate": model_build_config.learning_rate,
                              "max_depth": model_build_config.max_depth,
                              "min_samples_split": model_build_config.min_samples_split,
                              "min_samples_leaf": model_build_config.min_samples_leaf
                        })
                        model = BuildModel(model_build_config)
                        model_gbr = model.build_model_architecture()
                        print(f"model built: {model_gbr}")
                        
                        logged_model = mlflow.sklearn.log_model(
                              sk_model=model_gbr,
                              artifact_path="model",
                              skops_trusted_types=["sklearn.tree._tree.Tree"]
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