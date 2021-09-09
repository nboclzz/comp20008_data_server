# EoDP Assignment 2 Data Server
A basic server to fetch and store data
## Usage
```python
import requests

id = 'exampleid'
server = '0.0.0.0'

# get original data with dataset id, replace server to our server ip
res = requests.get(f"http://{server}:5000/datasets/original/{id})
data = res.json()['data']

# get all datasets' id and fields
res = requests.get(f"http://{server}:5000/datasets/original/)
data = res.json()['data']
```
