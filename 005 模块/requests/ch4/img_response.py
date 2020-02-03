import requests


def download_image():
    """
    demo:下载图片，下载文件
    """
    url = 'http://www.imooc.com/static/img/aboutus/g1.jpg'
    response = requests.get(url, stream=True)
    # print(response.status_code, response.reason)
    # print(response.headers)
    with open('demo_new.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    """
    demo：下载图片
    """
    url = 'http://www.imooc.com/static/img/aboutus/g1.jpg'
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as response:
        with open('demo_new1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)


# download_image()
download_image_improved()