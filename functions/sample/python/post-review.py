"""IBM Cloud Function that post review to a dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):

    review = {
        "id": dict["review"]["review_id"],
        "name": dict["review"]["name"],
        "dealership": dict["review"]["dealership"],
        "review": dict["review"]["review"],
        "purchase": dict["review"]["purchase"],
        "another": dict["review"]["another"],
        "purchase_date": dict["review"]["purchase_date"],
        "car_make": dict["review"]["car_make"],
        "car_model": dict["review"]["car_model"],
        "car_year": dict["review"]["car_year"]
    }

    try:
        client = Cloudant.iam(None,"HdyKq8n3jjkkvWgISvfi5x4cjYbJ-aapt3CB9r0joitf",
            url="https://apikey-v2-2nw8vsvk4u2eljbpggt8fud61i5dirj95nepoejtlco9:82b9dda303b3ab14dd02a015294eb506@1fca574f-7128-40f9-9b10-7857a6d31cd8-bluemix.cloudantnosqldb.appdomain.cloud",
            connect=True,
        )
        my_db = client['reviews']
        my_doc = my_db.create_document(review)
        
        return my_doc, 200
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}
    client.disconect()

if __name__=='__main__':
    main({"review": {"review_id": 1116, "name": "Upkar Lidder", "dealership": 15, "review": "Great service!", "purchase": False,
                 "another": "field", "purchase_date": "02/16/2021", "car_make": "Audi", "car_model": "Car", "car_year": 2021}})