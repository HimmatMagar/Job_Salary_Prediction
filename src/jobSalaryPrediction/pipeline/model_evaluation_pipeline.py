import mlflow
from jobSalaryPrediction import logger
from jobSalaryPrediction.config import ConfigurationManager
from jobSalaryPrediction.components.model_evaluation import ModelEval
from jobSalaryPrediction.utils.mlflow_config import configure_mlflow, load_run_id

STAGE_NAME = "Model Eval Stage"

class ModelEvalPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_eval_config = config.get_model_eval_config()

            run_id = load_run_id()

            try:
                  with open("artifact/model_id.txt", 'r') as f:
                        model_id = f.read()
            except FileNotFoundError as e:
                  raise

            configure_mlflow(experiment_name="JobSalaryPrediction")
            with mlflow.start_run(run_id=run_id):
                  model_eval = ModelEval(model_eval_config)
                  metrics = model_eval.eval_model()

                  mlflow.log_metrics({
                        "r2": metrics['r2'],
                        "MSE": metrics['MSE'],
                        "MAE": metrics['MAE']
                  })

                  r2_Threshold = 0.92
                  if metrics["r2"] >= r2_Threshold:
                        model = mlflow.register_model(
                              model_uri=f"models:/{model_id}",
                              name = "jobPredictionXGB"
                        )
                        logger.info(f"Registered — accuracy: {metrics['r2']}")

                        client = mlflow.tracking.MlflowClient()
                        client.transition_model_version_stage(
                              name="jobPredictionXGB",
                              version=model.version,
                              stage="Staging"
                        )
                  else:
                        logger.warning(f"Not registered — accuracy: {metrics['r2']} below threshold")
                  

if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvalPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e 