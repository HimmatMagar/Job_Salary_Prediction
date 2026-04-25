import os
import joblib
import pandas as pd
from jobSalaryPrediction import logger
from jobSalaryPrediction.utils import *
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from jobSalaryPrediction.entity import DataTransformationConfig


class DataTransform:
      def __init__(self, config: DataTransformationConfig):
            self.config = config

      def pipeline(self):
            return Pipeline([
                  ("processor", ColumnTransformer(
                        transformers=[
                              ("numeric", StandardScaler(), [1, 3, 8]),
                              ("ordinal encoder", OrdinalEncoder(
                                    categories=[
                                          ["High School", "Diploma", "Bachelor", "Master", 'PhD'],
                                          ["Startup", "Small", "Medium", "Large", "Enterprise"],
                                          ["Yes", "No", "Hybrid"]
                                    ]
                              ), [2, 5, 7]),
                              ("OHE encoder", OneHotEncoder(drop='first', handle_unknown='ignore'), [0, 4, 6])
                        ],
                        remainder="passthrough"
                  ))
            ])

      def split_data(self) -> None:
            df = pd.read_csv(self.config.data_path)

            x = df.drop(columns="salary")
            y = df['salary']
            X_train, X_val, y_train, y_val = train_test_split(
                  x, y,
                  test_size=0.3,
                  random_state=42
            )

            processor = self.pipeline()


            xTrain = processor.fit_transform(X_train)
            xTest = processor.transform(X_val)

            # Save the vectorizer to pkl file
            pipeline_path = os.path.join(self.config.root_dir, "pipeline.pkl")
            joblib.dump(processor, pipeline_path)
            logger.info(f"Vectorizer saved to {pipeline_path}")

            joblib.dump(xTrain, os.path.join(self.config.root_dir, "x_train.pkl"))
            joblib.dump(xTest, os.path.join(self.config.root_dir, "x_val.pkl"))
            joblib.dump(y_train, os.path.join(self.config.root_dir, "y_train.pkl"))
            joblib.dump(y_val, os.path.join(self.config.root_dir, "y_val.pkl"))

            logger.info("Splitted data into train test split")