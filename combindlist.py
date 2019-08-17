import urllib.request
import base64
import os


def base64_decode(base64_encode_str):
    """ 利用 base64.urlsafe_b64decode 对字符串解码 """

    if base64_encode_str:
        need_padding = len(base64_encode_str) % 4
        if need_padding != 0:
            missing_padding = 4 - need_padding
            base64_encode_str += '=' * missing_padding
        return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')
    return base64_encode_str


def gfwlist():
    url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    f = urllib.request.Request(url, headers=headers)
    gfwlist = base64_decode(urllib.request.urlopen(f).read().decode('utf-8'))
    return gfwlist


    
