"""Cizsle server web service."""


from fastapi import FastAPI


web_service = FastAPI()


@web_service.get("/")
async def root():
    return {"message": "FastAPI web service is running."}
