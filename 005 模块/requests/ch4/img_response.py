# -*- coding: utf-8 -*-

import requests


def download_image():
    """demo: 下载图片
    """
    # headers = {}
    url = "http://www.molecularecologist.com/wp-content/uploads/2013/11/github-logo.jpg"
    response = requests.get(url, stream=True)
    print response.status_code, response.reason
    print response.headers
    with open('demo.jpg', 'wb') as f:
        for chunk in response.iter_content(128):
            f.write(chunk)
    
def download_image_improved():
    """demo: 下载图片
    """
    # 伪造headers信息
    # headers = {}
    
    # 限定url
    url = "http://www.molecularecologist.com/wp-content/uploads/2013/11/github-logo.jpg"
    response = requests.get(url, stream=True)
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as f:
            # 每128写入一次
            for chunk in response.iter_content(128):
                f.write(chunk)

download_image_improved()
