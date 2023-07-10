import os
import sys
from fastapi import FastAPI
from collections import defaultdict
from typing import List
from pydantic import BaseModel

from transformers import pipeline
import json
import re
import requests



class AllTexts(BaseModel):
    items: List[str]

app = FastAPI()
sentiment_pipeline = None
translation_map = {'POS': 'positive', 'NEG': 'negative', 'NEU': 'neutral'}


@app.on_event("startup")
async def init_encoder():
    print("App Starting.....")
    global sentiment_pipeline
    print("Model Loading....")
    sentiment_pipeline = pipeline(model = "finiteautomata/bertweet-base-sentiment-analysis") 
    print("Model Loaded.....")


@app.post("/predict")
def summarize(texts: AllTexts):
        '''
            the entry point for the 
            Returns: the summary of the text based on sentences ranked for importance
        '''
        global sentiment_pipeline
        global translation_map
        reqs = texts.items
        resps = sentiment_pipeline(reqs)
        assert len(reqs) == len(resps)
  
        # # post process
        final_resp = []
        for idx, txt in enumerate(reqs):
             trans = {}
             rr = resps[idx]
             lab = ''
             score = 0.0
             trans['label'] = translation_map[ rr['label'] ]
             trans['text'] = txt
             trans['score'] = rr['score']
             final_resp.append(trans)
        return({"predictions": final_resp})




