from django.db import models

# Create your models here.

import urllib
import json

def getAll():
  url = "https://data.boston.gov/datastore/odata3.0/12cb3883-56f5-47de-afa5-3b1cf61b257b?$top=1000&$format=json"
  fileobj = urllib.urlopen(url)
  return json.loads(fileobj.read())
