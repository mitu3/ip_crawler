from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


proxy = Proxy(
    {
        'proxyType': ProxyType.MANUAL,
        'httpProxy': '218.94.255.11:8118'  # 代理ip和端口
    }
)
# 新建一个“期望的技能”，哈哈
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
# 把代理ip加入到技能中
proxy.add_to_capabilities(desired_capabilities)
driver = webdriver.PhantomJS(
    desired_capabilities=desired_capabilities
    )
driver.get('http://httpbin.org/ip')
print (driver.page_source)
driver.close()