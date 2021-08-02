
'''A collection of Data Science Helper Function'''
import numpy
import pandas


def null_count(df):
    return df.isnull().sum().sum()

def randomize(df):
    return df.sample(frac = 1)