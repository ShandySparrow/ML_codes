import json
import requests
data = json.dumps({"signature_name": "serving_default", "instances": [[   0  ,  0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0 ,   0, 0  ,  0 ,   0  ,  0  ,702 ,2344],
 [4613, 3937, 4024, 1470 ,1807, 1752, 1596 ,1190, 4307, 3145,  851,  680 ,2842 , 961, 1358, 2242, 3221, 4849, 1357, 2159],
 [   0  ,  0   , 0  ,  0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0  ,  0 ,   0, 0  ,  0 , 220 ,4471 ,2124, 3887],
 [   0  ,  0  ,  0 ,   0 ,   0 ,   0  ,  0 ,   0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0 ,0  ,  0  ,  0 , 702 ,3682 ,2589]]})

headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/models:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

print(predictions)