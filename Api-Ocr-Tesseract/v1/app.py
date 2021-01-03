from fastapi import FastAPI
from v1.services.extractor import Extractor

app = FastAPI(debug=True)
app.add_api_route(path='/home', endpoint=Extractor().run, methods=['POST'])
