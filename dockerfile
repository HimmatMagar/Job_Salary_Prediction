FROM python:3.12-slim

WORKDIR /app


ENV MLFLOW_TRACKING_URI=https://dagshub.com/HimmatMagar/Job_Salary_Prediction.mlflow
ENV MLFLOW_EXPERIMENT_NAME=JobSalaryPrediction

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5000" ]