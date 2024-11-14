import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("https://doc-dio-fraude-easteus-dev-oo1-cognitiveservices.azure.com")
    SUBSCRIPTION_KEY = os.getenv("159ca0ab2b0246fa8ff1853053eaaf10")
    STORAGE_CONNECTION_STRING = os.getenv("DefaultEndpointsProtocol=https;AccountName=strafaelsus2365133445350;AccountKey=wwEsOOtpT+mwR/w/psr7LUd1dzCCFetkWAlpq3GEjXwhVIfvjTsjskcgRbxd+IGanysw+nrJ0SI3+AStbjF2QA==;EndpointSuffix=core.windows.net ")
    CONTAINER_NAME = os.getenv("cartôes")
