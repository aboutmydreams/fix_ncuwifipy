import requests, base64, time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# url = 'http://222.204.3.221'


da = {
    1:'login_ok', 
    'E2553': 'Password is error', 
    'E2531': 'User not found', 
    'E2616': 'Arrearage users qianfei',
    'E2532': 'The two authentication interval cannot be less than 10 seconds',
    }

t1 = time.time()
def ncuwlan():
    t1 = time.time()
    url = 'http://222.204.3.221:804/include/auth_action.php'
    a = base64.b64encode('187233')
    data = {
        'action': 'login',
        'username': 'xg153',
        'password': '{B}' + str(a),
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'save_me': 1,
        'ajax': 1,
    }
    res = requests.post(url,data=data,timeout=5).text
    if 'login_ok' in res:
        print("connect!")
    elif 'E2532' in res:
        print('rest some time')
        time.sleep(12)
    else:
        print('something wrong')
        print(res[0:5] + str(da))
    return t1



# now_res = requests.get('https://common.cnblogs.com/scripts/jquery-2.2.0.min.js')
# t22 = time.time()
# print(t22-t1)

while True:
    try:
        now_res = requests.get('https://www.hao123.com',timeout=3)
        # print(now_res.status_code)
        time.sleep(3)
    except requests.exceptions.ConnectTimeout:
        t1 = ncuwlan()
        t2 = time.time()
        t3 = time.ctime()
        print(t2-t1,'s connected',t3)