import csv
import os
from pathlib import Path

# Dictionary that maps Area Code to Area Name. 
# Data read from AreaNameEnum.csv
area_dict = {}
with (Path(__file__).resolve().parent / 'AreaNameEnum.csv').open() as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        area_dict[int(row[0])] = row[1]


#Url of API.
URL = os.getenv("RIDES_SERVICE_URL", "http://rides")

#Port number
PORT = os.getenv("RIDES_SERVICE_PORT", "80")

#API Url 
API_URL = URL + ":" + PORT

#Url of API3
API3_URL = '/api/v1/rides'

#Url of API4
API4_URL = '/api/v1/rides'

#Url of API5
API5_URL = '/api/v1/rides'

#Url of API6
API6_URL = '/api/v1/rides'

#Url of API7
API7_URL = '/api/v1/rides'

#Url of API8
API8_URL = os.getenv("RIDES_DB_WRITE_URL", "http://flask-orchestrator:5000/api/v1/db/write")

#Url of API9
API9_URL = os.getenv("RIDES_DB_READ_URL", "http://flask-orchestrator:5000/api/v1/db/read")

# Response message 400
MESSAGE_400 = "Bad Request."

API_LIST_USER = os.getenv("RIDES_USERS_URL", "http://users:80/api/v1/users")

trapping_methods_for_count=["POST","PUT","PATCH","COPY","HEAD","OPTIONS","LINK","UNLINK","PURGE","LOCK","UNLOCK","PROPFIND","VIEW"]