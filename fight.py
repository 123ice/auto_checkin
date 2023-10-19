import requests
import json
import os

requests.packages.urllib3.disable_warnings()



def checkin(username=os.environ.get('FIGHT_USERNAME'), password=os.environ.get('FIGHT_PASSWORD'),
            base_url=os.environ.get('FIGHT_BASE_URL'), ):

    session = requests.session()
    # session.get(base_url, verify=False)
    login_url = base_url + '/wp-admin/admin-ajax.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'action=user_login&username=' + username + '&password=' + password   
    post_data = post_data.encode()
    try:
        response = session.post(login_url, post_data, headers=headers, verify=False)
    except Exception as e:
        print(e)

    print(response)
    print(response.text)

    data = 'action=user_qiandao'
    data = data.encode()
    try:
        response = session.post(login_url, data, headers=headers, verify=False)
    except Exception as e:
        print(e)
    print(response)
    print(response.text)
    return 0


result = checkin()