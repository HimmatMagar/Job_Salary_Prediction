import joblib
from pathlib import Path
from jobSalaryPrediction import logger
from jobSalaryPrediction.utils import *
from jobSalaryPrediction.entity import ModelEvalConfig
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



class ModelEval:
      def __init__(self, config: ModelEvalConfig):
            self.config = config
      
      
      def eval_model(self) -> None:
            xVal = load_file(Path(self.config.xval_file))
            yVal = load_file(Path(self.config.yval_file))
            model = joblib.load(self.config.model)

            yPred = model.predict(xVal)

            Model_Performance = {
                  "r2": r2_score(yVal, yPred),
                  "MSE": mean_squared_error(yVal, yPred),
                  "MAE": mean_absolute_error(yVal, yPred)
            }

            save_json(Path(self.config.metric), Model_Performance)
            logger.info(f"Model evaluation completed and report saved on {self.config.metric}")

            return Model_Performance