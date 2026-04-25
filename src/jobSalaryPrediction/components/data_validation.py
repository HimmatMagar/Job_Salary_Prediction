import pandas as pd
from jobSalaryPrediction.entity import DataValidationConfig

class DataValidation:
      def __init__(self, config: DataValidationConfig):
            self.config = config
      
      def validate_column(self) -> bool:
            try:
                  validation_status = None

                  data = pd.read_csv(self.config.data_path)
                  all_cols = list(data.columns)

                  all_schema = self.config.schema.keys()
                  for col in all_cols:
                        if col not in all_schema:
                              validation_status = False
                              with open(self.config.status_file, 'w') as f:
                                    f.write(f"Validation status: {validation_status}")
                        else:
                              validation_status = True
                              with open(self.config.status_file, 'w') as f:
                                    f.write(f"Validation status: {validation_status}")
            except Exception as e:
                  raise e