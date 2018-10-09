########################
# urllib
########################
# urllib的request模块可以非常方便地抓取URL的内容

'''
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    # 读取数据
    data = f.read()
    # status 状态码 
    print(f.status, f.reason)
    # 响应头
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
        # 响应数据
    print('Data', data.decode('utf-8'))


# GET
# 模拟浏览器发送GET请求，需要使用Request对象，通过往Request对象添加HTTP头，可以把请求伪装成浏览器，例如模拟iphone6 去请求豆瓣首页
req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# POST
# 以POST发送一个请求，需要把参数data以bytes形式传入
# 模拟一个微博登陆，先得去登陆的邮箱和口令，然后按照weibo.cn的登陆页格式以username=xxxx&password=xxx的编码传入
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')

login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('cliend_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res= wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

#########################
# requests
#########################
import requests
import os
from os import path
d = path.dirname(__file__) if '__file__' in locals() else os.getcwd()
r = requests.get('https://www.douban.com/')
print(r.status_code)    # 返回状态码
# print(r.text)           # html

# 对于带参数的URL，传入一个dict作为params参数
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url) # 返回真实请求的url https://www.douban.com/search?q=python&cat=1001
print(r.encoding) # requests自动检测编码
# print(r.content) # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
print(r.headers) # 获取响应头

# requests 对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取置顶的Cookie：
print(r.cookies['ts'])

# 如果需要在请求中传入Cookie，只需要准备一个dict传入cookies参数
cs = {'token': '12345', 'status': 'working'}
r = requests.get('https://www.douban.com/search', cookies=cs)

# 如果要指定超时传入以秒为单位的timeout参数
r = requests.get('https://www.douban.com/search', timeout=2.5) # 2.5s后超时
# requests的方便之处在于，对于特定类型的响应，例如JSON，可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# 需要传入HTTP Header时，传入一个dict座位headers参数
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# 发送POST 请求，只需要把get()方法变成post(),然后传入data参数作为POST请求的数据
# 默认使用application/x-www-form-urlencoded 对POST数据编码
r = requests.post('https://account.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# 如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
r = requests.post('https://account.douban.com/login', json=params)

# 上传文件需要更复杂的编码格式，requests把它简化成files参数
url = 'https://account.douban.com/login'
# 在读取文件时，务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
upload_files = {'file': open(path.join(d, 'test.txt'), 'rb')}
r = requests.post(url, files=upload_files)



