from selenium import webdriver
import json

mobileEmulation = {'deviceName': 'iPhone 6/7/8'}  # 设置手机环境
options = webdriver.ChromeOptions()
options.add_argument('headless')  # 设置不显示页面
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

i = 109228
print("爬取第%d个" % i)
url = 'http://mobile.nmpa.gov.cn/QueryRecord?tableId=27&searchF=ID&searchK=60461'
driver.get(url)
xpath_drug = "//body"
data = driver.find_elements_by_xpath(xpath_drug)

info = ""
tag = True
for i2 in data:
    if i2.text == "[]":
        tag = False
    else:
        info += str(i2.text)
print(info)
driver.quit()
