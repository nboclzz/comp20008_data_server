# EoDP Assignment 2 Data Server
A basic server to fetch and store data
## Usage
```python
import requests

# get original data with dataset id
id = 'exampleid'
server = '0.0.0.0'
res = requests.get(f"http://{server}:5000/datasets/original/{id})
data = res.json()['data']
```
