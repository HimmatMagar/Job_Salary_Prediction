import os
import joblib
from pathlib import Path
from sklearn.ensemble import GradientBoostingRegressor
from jobSalaryPrediction.utils import *
from jobSalaryPrediction import logger
from jobSalaryPrediction.entity import ModelBuilingConfig


class BuildModel:
      def __init__(self, config: ModelBuilingConfig):
            self.config = config

      
      def build_model_architecture(self):
            xtrain = load_file(Path(self.config.xtrain_data))
            ytrain = load_file(Path(self.config.ytrain_data))

            models = GradientBoostingRegressor(
                  n_estimators = self.config.n_estimators,
                  learning_rate = self.config.learning_rate,
                  max_depth = self.config.max_depth,
                  min_samples_split = self.config.min_samples_split,
                  min_samples_leaf = self.config.min_samples_leaf
            )
            models.fit(xtrain, ytrain)

            model_path = os.path.join(self.config.root_dir, self.config.model)
            with open(model_path, "wb") as f:
                  joblib.dump(models, f)
            
            logger.info(f"Model building successfully in: {model_path}")
            return models