import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from fastapi.middleware.cors import CORSMiddleware
from src.jobSalaryPrediction.pipeline.prediction_pipeline import PredictionPipeline


app = FastAPI(title="Job Salary Prediction")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
      job_title: Annotated[object, Field(..., description="Job title you want to work")]
      experience_years: Annotated[float, Field(..., description="Experience you have")]
      education_level: Annotated[Literal["High School", "Diploma", "Bachelor", "Master", "PhD"],
                                 Field(..., description="Your Educations level")]
      skills_count: Annotated[int, Field(..., description="How many skills do you have")]
      industry: Annotated[object, Field(..., description="Which industry you want to work")]
      company_size: Annotated[Literal["Startup", "Small", "Medium", "Large", "Enterprise"],
                              Field(..., description="How much company size do you want to work with")]
      location: Annotated[object, Field(..., description="Where do you want to work")]
      remote_work: Annotated[Literal["Yes", "No", "Hybrid"], Field(..., description="Do you want to work remote")]
      certifications: Annotated[int, Field(..., description="How many certificate you can achieve")]

predict_pipe = PredictionPipeline()

@app.get("/")
async def home():
      return {'message': "Welcome to  job Salary prediction"}

@app.get("/train")
async def train_model():
      pass


@app.post("/predict")
async def predict_salary(Input: UserInput):
      data = pd.DataFrame([{
            'job_title': Input.job_title,
            'experience_years': Input.experience_years,
            'education_level': Input.education_level,
            'skills_count': Input.skills_count,
            'industry': Input.industry,
            'company_size': Input.company_size,
            'location': Input.location,
            'remote_work': Input.remote_work,
            'certifications': Input.certifications
      }])
      prediction = predict_pipe.predict_salary(data)

      return {
            "prediction": float(prediction),
            "status": 200
      }
