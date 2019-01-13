import requests, base64, time
from random import choice
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# url = 'http://222.204.3.221'

da = {
    1:'login_ok', 
    'E2553': 'Password is error', 
    'E2531': 'User not found', 
    'E2616': 'Arrearage users qianfei',
    'E2532': 'The two authentication interval cannot be less than 10 seconds',
    }

url_list = ['https://www.baidu.com','https://zhidao.baidu.com','https://hanyu.baidu.com', 'http://www.kugou.com','https://www.sina.com.cn/','https://weibo.com/','http://www.sohu.com/','http://site.baidu.com/','https://www.guazi.com','https://open.163.com/','https://www.autohome.com.cn','https://www.imooc.com/','https://modao.cc/','https://jusp.tmall.com','http://www.4399.com/','http://www.tuniu.com/','https://mobile.pconline.com.cn/','http://www.rayli.com.cn/','http://www.hao123.com/zxfy','http://cp.iciba.com/']

t1 = time.time()
def ncuwlan():
    t1 = time.time()
    url = 'http://222.204.3.221:804/include/auth_action.php'
    a = base64.b64encode('187233'.encode(encoding='utf-8')).decode()
    # print(a,type(a))
    data = {
        'action': 'login',
        'username': 'xg153',
        'password': '{B}' + a,
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'save_me': 1,
        'ajax': 1,
    }
    try:
        res = requests.post(url,data=data,timeout=5).text
        if 'login_ok' in res:
            print("connect!")
        elif 'E2532' in res:
            print('rest some time')
            time.sleep(12)
        else:
            print('something wrong')
            print(res[0:5] + str(da))
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        print('ncuwlan can not be connected becuuse timeout')
    finally:
        pass
        return t1


while True:
    aurl = choice(url_list)
    try:
        now_res = requests.get(aurl,timeout=10)
        # print(now_res.status_code)
        time.sleep(5)
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        t1 = ncuwlan()
        t2 = time.time()
        t3 = time.ctime()
        print('{}s connected with{},now time is {}'.format(str(round(t2-t1,2)),t3,aurl))