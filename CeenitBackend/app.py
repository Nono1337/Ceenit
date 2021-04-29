from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import FileResponse
import logging
import json
from time import sleep
from datetime import datetime
from threading import Thread
from xml.dom import minidom
import yaml

# globale Varibalen
VERSION = '1.0'
app = FastAPI()

# Einstellung für das Logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO, datefmt='%H:%M:%S')

#Logging einlesen
with open('logging.yaml', 'r') as f:
    config_log = yaml.safe_load(f.read())
    logging.config.dictConfig(config_log)

@app.get("/versionsinfo",  status_code=status.HTTP_200_OK)
def version():
    return {'version': VERSION}


@app.post("/CreateUser", status_code=status.HTTP_200_OK)
def createUser( file: UploadFile = File(...)):
    pass

@app.post("/LoginUser", status_code=status.HTTP_200_OK)
def getSession(file: UploadFile = File(...)):
    pass

@app.get("/movie/getFiveHottest")
def getFiveHottest():
    pass



