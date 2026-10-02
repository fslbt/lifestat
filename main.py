from fastapi import FastAPI,Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib


app=FastAPI()


templates=Jinja2Templates(directory="templates")
models=joblib.load('lifesat_model.pkl')

@app.get('/')
async def index():
    return f"Index Page"

# @app.get("/model/{x}")
# async def model(request:Request,x):
#     X=float(x)
#     output=models.predict([[X]])
#     return templates.TemplateResponse(request=request,name="index.html",context={"output":output})\\

@app.post("/model")
async def model(request:Request,gdp:float=Form(...)):
    output=models.predict([[gdp]])
    return templates.TemplateResponse(request=request,name="index.html",context={"output":output})

@app.get("/template",response_class=HTMLResponse)
async def template(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")
