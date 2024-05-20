# Data Science in Production Project: Customer Bank Churn Prediction

## Project Description

Welcome to our Data Science project, where myself and 4 other EPITA students combine machine learning with advanced technologies to develop an application that predicts bank customer churn. Our solution integrates FastAPI, Streamlit, PostgreSQL, Apache Airflow, and Grafana to offer a full-stack application capable of processing, analyzing, and predicting churn with real-time capabilities.

## Explore My Data Science Work

For an in-depth look at the data scientist tasks, including data preparation, model training, and performance evaluation, please explore my dedicated Jupyter notebook: [best_model.pdf](/notebook/best_model.pdf). **IMPORTANT:** This is the outdated version.

To view the latest version of my work, please have a look at [new_model.pdf](/notebook/new_model.pdf). To give you an overview of what is updated, here are the changes:

1. Reorganized the notebook in a clear way for readers.
2. Updated modeling part, where I used more and with specific parameter models. *(The previous version, I didn't even put in anything for the parameter. For example, I used only XGBoost() and that was it. Now I put the objective, eval_metric, etc to get more out of the default models before tuning)*; I will also added the ensemble model where I combine multiple models using voting or bagging.

**UPCOMING**: 
1. The feature engineering section will have the testing of **OpenFE** feature geneartion library that I have been tested in different project, then I will use forward feature seletion to eliminate redundant features for optimal performance.
2. The final part of the notebook will be the evaluation of the best model, with the list of the most important features as well as using **SHAP** to explain more.


## Full Project Repository

For complete project details, including setup instructions, service integration, and additional documentation, visit the main project repository: [Main Project Repository](https://github.com/Safwan-ullah-khan/dsp-finalproject).

Thank you for your interest in my project. Feel free to contact me for further collaboration. 🤜🏻🤛🏻