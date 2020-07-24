import requests
r = requests.get('https://api.github.com/user', auth=('Hcque', '278696369db!'))
print(r.status_code)