from pydantic import BaseModel


class CustomerData(BaseModel):
    """
    A model representing customer data, used for
    predictions and analytics within the application.

    Attributes:
    CreditScore: The customer's credit score.
    Gender: The customer's gender.
    Age: The customer's age.
    Tenure: The number of years the customer has been with the bank.
    Balance: The customer's account balance.
    NumOfProducts: The number of products the customer has with the bank.
    HasCrCard: Whether the customer has a credit card (1) or not (0).
    IsActiveMember: Whether the customer is an active member (1) or not (0).
    EstimatedSalary: The customer's estimated salary.
    SatisfactionScore: The customer's satisfaction score with the bank.
    CardType: The type of card the customer holds.
    PointEarned: The number of points the customer has earned.
    PredictionSource: The source of the prediction data.
    """
    CreditScore: int
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    SatisfactionScore: int
    CardType: str
    PointEarned: int
    PredictionSource: str
