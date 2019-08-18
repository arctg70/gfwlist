import urllib.request
import base64
# import os


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
    print(gfwlist)
    return gfwlist


def personallist():
    f = open('personallist.txt', 'r')
    personallist = f.read()
    f.close()
    print(personallist)
    return personallist


fulllist = personallist() + gfwlist()
data = fulllist.encode('utf-8')

with open('fulllist.txt', 'w') as f:
    f.write(fulllist)

# with open('fulllist.txt', 'rb') as f:
#    data = f.read()

with open('fulllist_b64.txt', 'wb') as f:
    f.write(base64.encodebytes(data))


# encode64 = base64.b64encode(fulllist.encode('utf-8'))
# f = open('fulllist.txt', 'wb')
# f.write(encode64)
# f.close()
