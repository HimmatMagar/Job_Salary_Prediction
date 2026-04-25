# Job Salary Prediction

A machine learning pipeline for predicting job salaries based on various factors. This project implements a complete MLOps workflow with data ingestion, validation, model training, and API serving capabilities.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tech Stack](#tech-stack)

## Introduction

This project builds an end-to-end machine learning system for job salary prediction. It follows a modular pipeline architecture inspired by MLOps best practices, making it easy to extend and maintain. The system uses MLflow for experiment tracking and is designed to be deployed as a FastAPI web service.

## Features

- **Modular Pipeline Architecture** - Separated stages for data ingestion, validation, and model training
- **Data Ingestion** - Automatic download and extraction of dataset from Google Drive
- **Data Validation** - Schema validation to ensure data quality before processing
- **Experiment Tracking** - MLflow integration for tracking metrics, parameters, and artifacts
- **API Ready** - FastAPI-based API for model inference (in development)
- **Version Control** - DVC for data versioning and DagsHub integration

## Project Structure

```
Job_Salary_Prediction/
├── api/                        # FastAPI application
│   └── app.py                  # Main API server
├── artifact/                   # Generated artifacts (auto-created)
│   ├── data_ingestion/         # Downloaded and extracted data
│   └── data_validation/        # Validation outputs and status
├── config/                     # Configuration files
│   ├── config.yaml             # Main configuration
│   ├── params.yaml             # Model parameters
│   └── schema.yaml             # Data schema definitions
├── logging/                    # Log files
├── notebooks/                  # Jupyter notebooks for exploration
├── src/
│   └── jobSalaryPrediction/    # Main source code
│       ├── components/         # Pipeline components
│       │   ├── data_ingestion.py
│       │   └── data_validation.py
│       ├── config/             # Configuration management
│       ├── constants/          # Constant values
│       ├── entity/             # Data models/entities
│       ├── pipeline/           # Pipeline orchestration
│       │   ├── data_ingestion_pipeline.py
│       │   └── data_validation_pipeline.py
│       ├── utils/              # Utility functions
│       │   └── mlflow_config.py
│       └── __init__.py
├── templates/                  # HTML templates for web UI
├── venv/                       # Virtual environment (do not commit)
├── .env                        # Environment variables
├── .gitignore
├── main.py                     # Entry point for running pipelines
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup configuration
└── template.py                 # Project template generator
```

## Installation

### Prerequisites

- Python 3.12+
- Conda (recommended) or pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Job_Salary_Prediction
   ```

2. **Create and activate conda environment**
   ```bash
   conda create -p venv python==3.12 -y
   conda activate venv/
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file with the following variables:
   ```
   MLFLOW_TRACKING_URI=<your-mlflow-uri>
   DAGSHUB_TOKEN=<your-dagsHub-token>
   ```

## Usage

### Running the Pipeline

Execute the main pipeline stages sequentially:

```bash
python main.py
```

This runs:
1. **Data Ingestion Stage** - Downloads and extracts the dataset
2. **Data Validation Stage** - Validates data schema and columns

### Running Individual Stages

You can modify `main.py` to run specific stages only.

### Starting the API Server

```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

## Configuration

Configuration is managed through YAML files in the `config/` directory:

### config.yaml

Defines paths and settings for each pipeline stage:

```yaml
artifact_dir: artifact

data_ingestion:
  root_dir: artifact/data_ingestion
  data_source: <google-drive-url>
  zip_file: artifact/data_ingestion/data.zip
  unzip_file: artifact/data_ingestion

data_validation:
  root_dir: artifact/data_validation
  data_path: artifact/data_ingestion/job_salary_prediction_dataset.csv
  status_file: artifact/data_validation/status.txt
```

### params.yaml

Contains model hyperparameters and training settings.

### schema.yaml

Defines the expected data schema for validation.

## Tech Stack

| Category       | Technologies                              |
|----------------|-------------------------------------------|
| ML Framework   | scikit-learn, PyTorch                     |
| Experiment     | MLflow, DagsHub                           |
| Data           | pandas, numpy, matplotlib, seaborn        |
| API            | FastAPI, uvicorn, pydantic                |
| Data Version   | DVC (Data Version Control)                |
| Environment    | Conda                                     |

## Dataset

The dataset is automatically downloaded from Google Drive during the data ingestion stage. It contains job-related features for salary prediction.

## License

This project is licensed under the Apache 2.0 License.
