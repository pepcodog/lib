#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 00:10:18 2021

@author: pc
"""
import pickle
with open('JSON.pkl', 'rb') as f:
    x1 = pickle.load(f)
c1 = list(x1.columns)
exists = "0a1f3922-d632-4237-bac3-c97461ce3d3a" in x1.StudyID

#%%
with open('JSON_anon.pkl', 'rb') as f:
    x2 = pickle.load(f)
c2 = list(x2.columns)
#%%

x.tolist()

'''
import pandas as pd
from lib.print import Error
from lib.dataframe import DataFrameHandler
from lib.print import Work,Alert

class PickleHandler(DataFrameHandler):
    """Receives the location of a .pkl file and allows for dataframe manipulation and visualisation from the DataFrameHandler class."""
    def __init__(self,pkl:str,*args,**kwargs):
        super().__init__()
        self.load(pkl)
        if not 'reset' in kwargs or kwargs.get('reset',True):
            self.ResetIndex()

    def load(self,pkl):
        self.location = pkl
        try:
            pklFileArray = self.location.split('/')
            pklFileArrayLen = len(pklFileArray)
            self.fileName = pklFileArray[pklFileArrayLen-1]
            Alert("Loading dataframe: "+self.fileName)
            self.pkl = pd.read_pickle(self.location)
            self.dataframe = pd.DataFrame(self.pkl)
            self.loaded()
        except:
            Error("The provided pkl file destination ("+self.location+") does not exist")
            '''