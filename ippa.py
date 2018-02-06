import urllib.request
from lxml import etree
import time
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('data')


def get_url(url):     # 国内高匿代理的链接
    url_list = []
    for i in range(1,2):
        url_new = url + str(i)
        url_list.append(url_new)
    return url_list


def get_content(url):     # 获取网页内容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    content = res.read()
    return content.decode('utf-8')


def xlwtadd(x,y,z):
    worksheet.write(x,y,label=z)
    workbook.save('datas.xls')


def get_info(content):      # 提取网页信息
    #  / ip 端口
    datas_ip = etree.HTML(content).xpath('//*[@id="ip_list"]/tr/td[2]/text()')
    datas_port = etree.HTML(content).xpath('//*[@id="ip_list"]/tr/td[3]/text()')
    datas_address = etree.HTML(content).xpath('//*[@id="ip_list"]/tr/td[4]/text()')
    datas_isgao = etree.HTML(content).xpath('//*[@id="ip_list"]/tr/td[5]/text()')
    datas_type = etree.HTML(content).xpath('//*[@id="ip_list"]/tr/td[6]/text()')
    xlwtadd(0, 1, 'ip')
    xlwtadd(0, 2, 'port')
    xlwtadd(0, 3, '地区')
    xlwtadd(0, 4, '是否匿名')
    xlwtadd(0, 0, '类型')
    print(datas_address)
    for i in range(0,len(datas_ip)):
        xlwtadd(i + 1, 0, datas_type[i])
        xlwtadd(i + 1, 1, datas_ip[i])
        xlwtadd(i + 1, 2, datas_port[i])
        xlwtadd(i + 1, 3, datas_address[i])
        xlwtadd(i + 1, 4, datas_isgao[i])



    with open("data.txt", "w") as fd:
        for i in range(0,len(datas_ip)):
            out = u""
            out += u"" + datas_ip[i]
            out += u":" + datas_port[i]
            fd.write(out + u"\n")     # 所有ip和端口号写入data文件
            print(out)

def verif_ip(ip, port):  # 验证ip有效性
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
                 ' (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    proxy = {'http': 'http://%s:%s' % (ip, port)}
    print(proxy)

    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    test_url = "https://www.baidu.com/"
    req = urllib.request.Request(url=test_url, headers=headers)
    time.sleep(6)
    try:
        res = urllib.request.urlopen(req)
        time.sleep(3)
        content = res.read()
        if content:
            print('that is ok')
            with open("data2.txt", "a") as fd:  # 有效ip保存到data2文件夹
                fd.write(ip + u":" + port)
                fd.write("\n")
        else:
            print('its not ok')
    except urllib.request.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    url_list = get_url(url)
    for i in url_list:
        print(i)
        content = get_content(i)
        time.sleep(3)
        get_info(content)

    with open("data.txt", "r") as fd:
        datas = fd.readlines()
        for data in datas:
            print(data.split(u":")[0])
            verif_ip(data.split(u":")[0],data.split(u":")[1])
