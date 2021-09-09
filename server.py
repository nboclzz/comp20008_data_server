from flask import Flask
import requests
import json
import os

app = Flask(__name__)

@app.route('/datasets/original/<id>')
def get_original_dataset(id):
    path = f'data/original/{id}.json'
    if not os.path.exists(path):
        try:
            # the government database only returns 100 entries each request
            records = []
            offset = 0
            res = fetch_data(id, offset)
            fields = res['fields']
            r = res['records']
            while r:
                records.append(r)
                offset += 100
                r = fetch_data(id, offset)['records']
            with open(path, 'w') as f:
                json.dump({'fields': fields, 'records': records}, f)
        except:
            print('Error fetching original data')
    with open(path) as f:
        data = json.load(f)
    return {'data': data}

@app.route('/datasets/original/')
def get_original_datasets():
    files = os.listdir('data/original')
    fields = {}
    for file in files:
        with open(os.path.join('data/original', file)) as f:
            fields[file[:-5]] = json.load(f)['fields']
    return {'data': fields}

def fetch_data(id, offset):
    r = requests.get(f'https://discover.data.vic.gov.au/api/3/action/datastore_search?offset={offset}&resource_id={id}')
    r = r.json()['result']
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0')
