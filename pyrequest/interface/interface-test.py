import requests
url = 'http://127.0.0.1:8000/api/get_event_list/'
r = requests.get(url, params={'eid':'3'})
print(r.status_code)
result = r.json()
assert result['status'] == 200
assert result['message'] == 'success'
assert 'MAX' in result['data']['name']
o
