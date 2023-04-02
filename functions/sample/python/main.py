"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
import json
import os
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def main():
    current_path = os.getcwd()
    print(current_path)
    with open('/.creds-sample.json', 'r') as file:
        config = json.load(file)
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
