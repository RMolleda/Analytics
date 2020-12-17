def impData():
    import pandas as pd 
    import requests
    import json

def impPlot():
    import pandas as pd 
    import matplotlib as plt

def impNP():
    import pandas as pd 
    import numpy as np 
    import requests 

def readCSV(url, delim):
    import pandas as pd 
    readed = pd.read_csv(url, delimiter=delim)
    return readed
    import json

def impScraping():
    from bs4 import BeautifulSoup
    import pandas as pd 
    import selenium as sl

def fix_date(x):
    import datetime
    #change the "1989" for the .max()/.min() value.
    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year,x.month,x.day)