# EoDP Assignment 2 Data Server
A basic server to fetch and store data
## Usage
```python
import requests
import json
import pandas as pd

id = 'exampleid'
server = '0.0.0.0'

# get original data with dataset id, replace server to our server ip
res = requests.get(f"http://{server}:5000/datasets/original/{id})
data = res.json()['data']

# get all datasets' id and fields
res = requests.get(f"http://{server}:5000/datasets/original/)
data = res.json()['data']

# get entries of existing custom data
res = requests.get(f"http://{server}:5000/datasets/modified/)
data = res.json()['data']

# get an custom object using title
title = 'some-title'
res = requests.get(f"http://{server}:5000/datasets/modified/{title})
data = res.json()['data']

# load an custom dataset using title
title = 'some-title'
res = requests.get(f"http://{server}:5000/datasets/modified/{title})
data = res.json()['data']
df = pd.DataFrame.from_records(data)

# upload custom object
obj = {'some': 'object'}
requests.post('https://{server}:5000/datasets/modified', data={'title':'some-title', 'data': obj})

# upload custom pandas DataFrame
result = df.to_json(orient="records")
parsed = json.loads(result)
requests.post('https://{server}:5000/datasets/modified', data={'title':'some-title', 'data': parsed})
```
