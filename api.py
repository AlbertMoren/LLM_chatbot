from fastapi import FastAPI
from fast_zero.schemas import Message

app = FastAPI()

@app.post('/user/User_question',response_model=Message)
def question_user(user: Message):
    