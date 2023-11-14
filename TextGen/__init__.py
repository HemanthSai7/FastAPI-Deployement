from fastapi import FastAPI

app = FastAPI(title="Deploying FastAPI Apps on Huggingface")

from TextGen import router


