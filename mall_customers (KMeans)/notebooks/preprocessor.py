
import numpy as np
import pandas as pd 

class Preprocessor : 
    def __init__ (self, df):
        self.df = df.copy()

    def replacement(self):
        self.df['Gender'].replace({'Male' : 1 , 'Female' : 0},inplace = True)

    def delete(self):
        self.df.drop(columns = ['CustomerID'])
        
    def transform (self) : 
        self.replacement()
        self.delete()
        return self.df
