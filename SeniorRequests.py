#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : SeniorRequests.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/10
# @Desc  :


import requests

#跨请求保持一些 cookie
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

#会话也可用来为请求方法提供缺省数据
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

#请求与响应对象
r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
#如果想访问服务器返回给我们的响应头部信息
print(r.headers)
print(r.status_code)
#如果想得到发送到服务器的请求的头部，我们可以简单地访问该请求
print(r.request.headers)

#准备的请求（Prepared Request）
#要获取一个带有状态的 PreparedRequest，
# 请用 Session.prepare_request() 取代 Request.prepare() 的调用，如下所示：
url = ''
data = {}
headers = {}
from requests import Request, Session

s = Session()
req = Request('GET',  url,
    data=data,
    headers=headers
)
prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    # stream=stream,
    # verify=verify,
    # proxies=proxies,
    # cert=cert,
    timeout=0.01
)

print(resp.status_code)


#SSL 证书验证
r = requests.get('https://github.com', verify=True)
print(r)
#你可以为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径：
requests.get('https://github.com', verify='/path/to/certfile')
#或者将其保持在会话中：
s = requests.Session()
s.verify = '/path/to/certfile'
#注:如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理。
#你还可以通过 REQUESTS_CA_BUNDLE 环境变量定义可信任 CA 列表。

#如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。

#客户端证书
#你也可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：
requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
#或者保持在会话中：
s = requests.Session()
s.cert = '/path/client.cert'

#警告:本地证书的私有 key 必须是解密状态。目前，Requests 不支持使用加密的 key。

#代理
#如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求:
import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)

#你也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理。
#>>$ export HTTP_PROXY="http://10.10.1.10:3128"
#>>$ export HTTPS_PROXY="http://10.10.1.10:1080"
#>>$ python
#>>> import requests
#>>> requests.get("http://example.org")

#要为某个特定的连接方式或者主机设置代理，
# 使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'} # 为128设置代理
#注意，代理 URL 必须包含连接方式。




