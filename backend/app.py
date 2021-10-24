import os
from fastapi import FastAPI,status
from controllers import convert_currency_controller
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
	allow_headers=["*"],
)

app.include_router(convert_currency_controller.route, prefix='/api')

@app.get('/',status_code=status.HTTP_200_OK,response_model=str)
def index():
    app_name = os.getenv("APP_NAME")
    return JSONResponse(content="{f'API {app_name} DISPONIVEL!'}")
