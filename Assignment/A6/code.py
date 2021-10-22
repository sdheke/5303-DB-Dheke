import pymongo
import pprint
import random
import json
from typing import Optional,List
from fastapi import FastAPI
from turfpy.transformation import circle
from turfpy.measurement import points_within_polygon
from fastapi.responses import RedirectResponse,HTMLResponse
import shutil 
from bson.objectid import ObjectId
from geojson import Feature, Point
from pydantic import BaseModel,Field
import uvicorn


app = FastAPI()
cnx = pymongo.MongoClient('localhost:27017',username='root',password='root')
db = cnx["restaurants"]
coll = db['restaurantlist']

class mymodel(BaseModel):
    restaurant_id: str 
    name: str 
    address: dict
    cuisine: str  
    borough: str 
    grades: list 

@app.get("/categories")
async def allcats():
    res = list(coll.distinct('cuisine'))
    return {"count":len(res),"data":res}

@app.get("/resturants")
async def resturentsall():
    response_list = []
    res = list(coll.find().skip(100).limit(1000))
    for r in res:
            response_list.append(mymodel(**r))
    return {"count is ":len(res),"data":response_list}

@app.get("/rating/{rate}")
async def allrtings(rate:int):
    response_list = []
    stuff ={"grades.score":{"$gte":rate}}
    res= coll.find(stuff)
    for r in res:
        response_list.append(mymodel(**r))
    return response_list

@app.get("/categories/{cuisine}")
async def bycuisine(cuisine:str):
    dbq ={'cuisine':cuisine}
    res = coll.find(dbq)
    count = res.count()
    response_list = []
    toadd = f'<a href= /categories> click for cuisine list</a>'
    if(count ==0):
        note =f"{cuisine} is not in the list of genre.<br> " + toadd
        return HTMLResponse(content=note, status_code=200)
    else:
        for r in res:
            response_list.append(mymodel(**r))
        return response_list

@app.get("/location")
async def loc(latlong:list):
    stuff ={"address.coord": {"$near":latlong}, "$maxDistance": 10}
    res = coll.find(stuff)
    return res.count()

@app.get("/zipcode")
async def zipsall(Zips:list):
    zipcodes_arr =[]
    for zip in Zips:
        zipcodes_arr.append(str(zip))
    stuff = { "address.zipcode": {"$in":zipcodes_arr}}
    res = coll.find(stuff)
    response_list = []
    for z in res:
        response_list.append(mymodel(**z))
    return response_list




