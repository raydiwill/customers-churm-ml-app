from datetime import datetime
from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import and_
from db_setup import *
from models import Base, Customer
from schema import CustomerData
import pandas as pd
import joblib
import uvicorn


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME,
                          version=settings.PROJECT_VERSION)
    create_tables()
    return application


app = start_application()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('../notebook/boosting_model.joblib')


@app.post("/predict/")
async def predict(data: List[CustomerData],
                  db: SessionLocal = Depends(get_db)):
    # Convert the list of Pydantic models to a list of dictionaries
    data_dicts = [item.dict() for item in data]

    # Create a DataFrame from the list of dictionaries
    input_data = pd.DataFrame(data_dicts)
    input_data.drop(
        columns=["PredictionSource"], inplace=True, errors="ignore")

    # Perform prediction
    prediction_results = model.predict(input_data)

    results = []
    for idx, prediction in enumerate(prediction_results):
        customer_data = data_dicts[idx]
        customer_data.update({"PredictionResult": int(prediction)})
        # Create and add CustomerModel instance to database
        customer = Customer(**customer_data)
        db.add(customer)
        results.append(customer_data)

    db.commit()
    return {"prediction": results}


@app.get('/past-predictions/')
def get_predict(dates: dict, db: SessionLocal = Depends(get_db)):
    start_date = dates["start_date"]
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = dates["end_date"]
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    prediction_source = dates["pred_source"]
    print(f"Prediction Source: {prediction_source}")

    if prediction_source == "webpage":
        predictions = db.query(Customer).filter(
            and_(Customer.PredictionDate >= start_date,
                 Customer.PredictionDate < end_date,
                 Customer.PredictionSource == prediction_source)
        ).all()

    if prediction_source == "scheduled":
        predictions = db.query(Customer).filter(
            and_(Customer.PredictionDate >= start_date,
                 Customer.PredictionDate < end_date,
                 Customer.PredictionSource == prediction_source)
        ).all()

    if prediction_source == "all":
        predictions = db.query(Customer).filter(
            and_(Customer.PredictionDate >= start_date,
                 Customer.PredictionDate < end_date)
        ).all()

    return predictions


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8050, reload=True)
