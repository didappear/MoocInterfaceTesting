#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json

class RunMain:

    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

'''
https://117.121.101.40
POST /api/newcourseinfo
apiname=newcourseinfo&cid=136&timestamp=1563294587534&token=be24418ecbbfc521658121de2d0abea9&uid=0
'''

if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/load'
    data = {
        'cart':'11'
    }
    run = RunMain(url,method='GET',data=data)
    print(run.res)