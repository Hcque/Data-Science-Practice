import requests
import threading
from time import time

base_url = 'http://192.168.127.134:8089'

def sign_thread(start_user, end_user):
    for i in range(start_user, end_user):
        datas = {'eid':i, "phone":12800000000+i}
        r = requests.post(base_url+'/api/user_sign/', data=datas)
        result = r.json()
        try:
            assert 'success' in result['message']
        except AssertionError as e:
            print('fail: ' + str(i))

threads = []
for i in range(1, 30):
    start = i * 100
    end = i * 1000
    t = threading.Thread(target=sign_thread, args=(start, end))
    threads.append(t)

if __name__ == '__main__':
    s = time()

    for i in range(len(threads)):
        print(i)
        threads[i].start()
    for i in threads:
        i.join()

    e = time()
    print('elapse time: '+str(e-s))

