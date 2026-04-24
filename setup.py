from setuptools import setup, find_packages

__version__ = '0.0.0.1'

REPO_NAME = "Job_Salary_Prediction"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "jobSalaryPrediction"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setup(
      name="jobSalaryPrediction",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End Job Salary prediction Project implementation",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls = {
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue",
      },
      package_dir = {"": "src"},
      packages=find_packages(where='src')
)