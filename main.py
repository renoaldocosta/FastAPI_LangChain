from fastapi import FastAPI
from Parte2.routes.llms import llm_router


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message":"This is an API for LLMs"}

app.include_router(llm_router)