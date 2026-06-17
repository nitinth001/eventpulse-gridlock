from fastapi import FastAPI
from api.utils import predict_event_plan

app = FastAPI(
    title="EventPulse API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message":"EventPulse API Running"}


@app.get("/predict")
def predict(
        event_cause:str,
        hour:int,
        day:str
):

    result = predict_event_plan(
        event_cause,
        hour,
        day
    )

    return result