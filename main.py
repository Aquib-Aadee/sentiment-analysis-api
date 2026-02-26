from fastapi import FastAPI
from pydantic import BaseModel
from src.analyzer import analyze_sentiment
import uvicorn

# Initialize the API
app = FastAPI(
    title="Sentiment Analysis API", 
    description="A Natural Language Processing API for analyzing text sentiment."
)

# Define the exact data structure we expect users to send us
class TextRequest(BaseModel):
    text: str

    # Create a welcome message for the root URL
@app.get("/")
def welcome():
    return {"message": "Welcome to the Sentiment Analysis API! Please add '/docs' to the URL to interact with the model."}

# Create the endpoint (the URL path where users will send their text)
@app.post("/predict")
def predict_sentiment(request: TextRequest):
    # Pass the incoming text to our NLP brain
    result = analyze_sentiment(request.text)
    return result

# Run the server locally
if __name__ == "__main__":
    print("Starting API server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)