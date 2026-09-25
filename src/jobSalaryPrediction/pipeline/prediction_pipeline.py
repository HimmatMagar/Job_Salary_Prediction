import mlflow
import joblib
from  mlflow import MlflowClient
from jobSalaryPrediction import logger
from jobSalaryPrediction.utils.mlflow_config import load_run_id


class PredictionPipeline:
      def __init__(self):
            """Initialize the prediction pipeline by loading trained model and vectorizer."""
            try:
                  client = MlflowClient()
                  champion = client.get_model_version_by_alias(
                        "jobPredictionGBR",
                        "champion"
                  )

                  run_id = champion.run_id
                  self.model = mlflow.pyfunc.load_model(
                        "models:/jobPredictionGBR@champion"
                  )

                  artifact_path = mlflow.artifacts.download_artifacts(
                        run_id=run_id,
                        artifact_path="pipeline/pipeline.pkl"
                  )

                  with open(artifact_path, "rb") as f:
                        self.pipeline = joblib.load(f)
                  logger.info("Model and pipeline loaded successfully")

            except FileNotFoundError as e:
                  logger.error(f"Error loading model: {e}")
                  raise

      def predict_salary(self, data):    
            try:
                  # Vectorizer pipeline handles both cleaning and vectorization
                  x_data = self.pipeline.transform(data)
                  
                  # Make prediction
                  prediction = self.model.predict(x_data)[0]
                  
                  return prediction
            except Exception as e:
                  raise Exception(f"Error during prediction: {e}")