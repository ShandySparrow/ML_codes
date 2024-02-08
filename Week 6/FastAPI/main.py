# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request
from functions import predict_user_input

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Chatgpt tweet sentiment analysis'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/name/{names}')
def get_name(name: str, request: Request):
    names = request.client.host
    return {'Welcome To Chatgpt tweet sentiment analysis': f'{names}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_tweet(text):
    result = predict_user_input(text)
    return {'Sentiment' : f'{result}'}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
    pass
#uvicorn app:app --reload