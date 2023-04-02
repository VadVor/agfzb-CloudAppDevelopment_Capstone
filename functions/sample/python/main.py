"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
import json
import os


def main():
   current_path = os.getcwd()
   print(current_path)
   with open('/.creds-sample.json', 'r') as f:
    config = json.load(f)
    try:
        client = Cloudant.iam(None,config['IAM_API_KEY'],
            url=config["COUCH_URL"],connect=True,)
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}

if __name__=='__main__':
    main()