from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def main(dict):
  
    try:
        client = Cloudant.iam(None,"HdyKq8n3jjkkvWgISvfi5x4cjYbJ-aapt3CB9r0joitf",
            url="https://apikey-v2-2nw8vsvk4u2eljbpggt8fud61i5dirj95nepoejtlco9:82b9dda303b3ab14dd02a015294eb506@1fca574f-7128-40f9-9b10-7857a6d31cd8-bluemix.cloudantnosqldb.appdomain.cloud",
            connect=True,
        )
        my_db = client['reviews']
        my_doc = my_db.get_query_result(selector = {'dealership':{'$eq':int(dict["dealerId"])}})
        for doc in my_doc:
            print(doc)
        return my_doc, 200
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

if __name__=='__main__':
    main({"dealerId": 15})