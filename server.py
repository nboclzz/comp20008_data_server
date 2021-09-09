from flask import Flask
import requests
import json
import os
import pandas as pd

app = Flask(__name__)

@app.route('/datasets/original/<id>')
def index(id):
    path = f'data/original/{id}.json'
    if not os.path.exists(path):
        try:
            # the government database only returns 100 entries each request
            records = []
            offset = 0
            r = fetch_data(id, offset)
            while r:
                records.append(r)
                offset += 100
                r = fetch_data(id, offset)
            with open(path, 'w') as f:
                json.dump(records, f)
        except:
            print('Error fetching original data')
    with open(path) as f:
        data = json.load(f)
    return {'data': data}

def fetch_data(id, offset):
    r = requests.get(f'https://discover.data.vic.gov.au/api/3/action/datastore_search?offset={offset}&resource_id={id}')
    r = r.json()['result']['records']
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0')
