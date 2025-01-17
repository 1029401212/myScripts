import os,sys
import json,time,re,traceback,random,datetime,logging,importlib,urllib,string
import requests
import chardet


def ua():
    uuid = ''.join(random.sample('123456789abcdef123456789abcdef123456789abcdef123456789abcdef', 40))
    addressid = ''.join(random.sample('1234567898647', 10))
    iosVer = ''.join(random.sample(["14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1", "13.7", "13.1.2", "13.1.1"], 1))
    iosV = iosVer.replace('.', '_')
    iPhone = ''.join(random.sample(["8", "9", "10", "11", "12", "13"], 1))
    ADID = ''.join(random.sample('0987654321ABCDEF', 8)) + '-' + ''.join(
        random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(
        random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 12))
    return f'jdapp;iPhone;10.0.4;{iosVer};{uuid};network/wifi;ADID/{ADID};model/iPhone{iPhone},1;addressid/{addressid};appBuild/167707;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS {iosV} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/null;supportJDSHWK/1'


def cxkv2_xyz():
    global session
    session.headers={
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'sec-fetch-mode': 'navigate',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'none',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    session.get('https://www.cxkv2.xyz/')


def get_auth_register():
    global session
    session.headers.update({
        'sec-fetch-user': '?1',
        'referer': 'https://www.cxkv2.xyz/',
    })
    session.get("https://www.cxkv2.xyz/auth/register")


def post_auth_register():
    global session
    session.headers.update({
        'content-length': '238',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-mode': 'cors',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-fetch-site': 'same-origin',
        'origin': 'https://www.cxkv2.xyz',
        'referer': 'https://www.cxkv2.xyz/auth/register',
    })
    session.cookies.update({
        '_ga': 'GA1.2.1998347726.1639264201',
        '_gid': 'GA1.2.205577023.1639264201',
        '_gat': '1'
    })

    email_str=''.join(random.sample(string.ascii_letters + string.digits, random.randint(7, 14)))
    email_suffix=random.choice(
        ['hotmail.com','msn.com','yahoo.com','gmail.com','aim.com','aol.com','mail.com','walla.com','inbox.com','126.com','163.com','sina.com','21cn.com','sohu.com','yahoo.com.cn','tom.com','qq.com','etang.com','citiz.com','sogou.com','chinaren.com','x.cn','56.com','eyou.com']
    )
    email=f"{email_str}%40{email_suffix}"
    name=email_str
    passwd=''.join(random.sample(string.ascii_letters + string.digits, random.choice([6, 8])))
    repasswd=passwd
    wechat=email_str
    imtype=random.choice(range(1,5))

    data=f"email={email}&name={name}&passwd={passwd}&repasswd={repasswd}&wechat={wechat}&imtype=4&code=0&geetest_challenge=54229abfcfa5649e7003b83dd475529432&geetest_validate=aaa9960_da9_eaadf0&geetest_seccode=aaa9960_da9_eaadf0%7Cjordan"

    res=session.post("https://www.cxkv2.xyz/auth/register",data=data)
    # print(chardet.detect(res.content))
    # print(res.content)
    res.encoding = 'utf-8'
    print(res.text)
    # print(res.encoding)
    # res.encoding = 'utf-8'
    # print(res.text)
    # if res.get('ret',False):
    #     print('注册成功')
    #     print(f"邮箱: {email}")
    #     print(f"密码: {repasswd}")
    #     return email,repasswd
    # else:
    #     print('注册失败')
    print(f"邮箱: {re.sub(r'%40','@',email)}")
    print(f"密码: {repasswd}")
    return email,repasswd


def auth_login(email,repasswd):
    global session
    session.headers.update({
        'referer': 'https://www.cxkv2.xyz/auth/login'
    })
    data=f"email={email}&passwd={repasswd}&code="
    res=session.post("https://www.cxkv2.xyz/auth/login",data=data)
    # print(chardet.detect(res.content))
    # print(res.content)
    # print(res.text)
    # print(res.text)
    # if res.get('ret',False):
    #     print('登录成功')
    # else:
    #     print('登录失败')


def user():
    global session
    session.headers={
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'same-origin',
        'referer': 'https://www.cxkv2.xyz/auth/login',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    res=session.get("https://www.cxkv2.xyz/user")
    # print(chardet.detect(res.content))
    # print(res.content)
    res.encoding = 'utf-8'
    print(res.text)
    # subscription=re.findall(r'data-clipboard-text="(.*?mu=2)">', res.text)
    # if subscription:
    #     print(f"v2订阅地址: {subscription[0]}")
    # else:
    #     print('获取订阅地址失败')


def main_handler(event, context):
    global session,ua
    ua="Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/46.01.4.5140"
    session=requests.session()
# try:
    cxkv2_xyz()
    get_auth_register()
    email,repasswd=post_auth_register()
    auth_login(email,repasswd)
    user()
# except Exception as e:
#     print(f"错误\n{e}")



if __name__ == '__main__':
    main_handler('','')


