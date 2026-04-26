import os
import joblib
from pathlib import Path
from xgboost import XGBRegressor
from jobSalaryPrediction.utils import *
from jobSalaryPrediction import logger
from jobSalaryPrediction.entity import ModelBuilingConfig


class BuildModel:
      def __init__(self, config: ModelBuilingConfig):
            self.config = config

      
      def build_model_architecture(self):
            xtrain = load_file(Path(self.config.xtrain_data))
            ytrain = load_file(Path(self.config.ytrain_data))

            models = XGBRegressor(
                  n_estimators = self.config.n_estimators,
                  max_depth = self.config.max_depth,
                  subsample = self.config.subsample,
                  colsample_bytree = self.config.colsample_bytree,
                  reg_alpha = self.config.reg_alpha,
                  reg_lambda = self.config.reg_lambda
            )
            models.fit(xtrain, ytrain)

            model_path = os.path.join(self.config.root_dir, self.config.model)
            with open(model_path, "wb") as f:
                  joblib.dump(models, f)
            
            logger.info(f"Model building successfully in: {model_path}")
            return models