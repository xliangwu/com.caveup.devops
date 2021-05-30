import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import date

from selenium.common.exceptions import NoSuchElementException


def process(keywords=[]):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument(
        'User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')

    driver = webdriver.Chrome(options=chrome_options)

    contents = []
    for keyword in keywords:
        if not keyword:
            continue

        url = "https://db.yaozh.com/jinkoujixie?name={}&zczbh=&scsz=&jgzc=&pzrqstr=&pzrqend=&syfw=&yxqstr=&yxqend=&bmdh=%E5%85%A8%E9%83%A8&type=%E5%85%A8%E9%83%A8&lyd=%E5%85%A8%E9%83%A8" \
            .format(keyword)
        print("start to crawl for keyword:{}=>{}".format(keyword, url))
        driver.get(url)

        time.sleep(5)
        exist, tip_dialog = find_element(driver, By.ID, 'closeTipsDialog')
        if exist:
            tip_dialog.click()

        try:
            login_exist, elem = find_element(driver, By.CLASS_NAME, 'cl-red')
            if login_exist:
                all_links = elem.find_elements_by_tag_name("a")
                login_ele = all_links[0];
                login_ele.click()

                user_input = driver.find_element_by_id('username')
                user_password = driver.find_element_by_id('pwd')
                user_input.send_keys("wuxueliang4596")
                user_password.send_keys("57T@dT57yMz..Ya")
                login_btn = driver.find_element_by_id('button')
                login_btn.click()

            time.sleep(5)
            process_one_page(driver, keyword, contents)
            time.sleep(5)
            print("end to crawl for keyword:", keyword)
        except:
            print("driver element has problem")

        save_data(contents, keyword)
        contents.clear()

    driver.close()


def find_element(driver: webdriver.Chrome, byType, selector):
    try:
        element = driver.find_element(byType, selector)
        return True, element
    except NoSuchElementException:
        return False, None


def save_data(contents: [], keyword=''):
    today = date.today()
    today_label = today.strftime("%y%m%d")
    output = "yaozhi_data_{}_{}.csv".format(keyword, today_label)
    with open(output, 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['产品名称', '注册证编号', '注册人名称', '批准日期 ', '有效期'])
        for content in contents:
            writer.writerow(content)

    print("save data is done =>", output)


def process_one_page(driver: webdriver.Chrome, keyword='', contents=[]):
    pages = driver.find_elements_by_class_name('page')
    if not pages:
        print("没有找到分页，可能是没有数据")
        return

    last_page = pages[-2]
    page_size = last_page.text
    print("total page size:", page_size)

    count = 0
    for i in range(int(page_size)):
        page_url = "https://db.yaozh.com/jinkoujixie?name={}&p={}&pageSize=20".format(keyword, i + 1)
        print("current page:", page_url)
        driver.get(page_url)

        tip_dialog = driver.find_element_by_id('closeTipsDialog')
        if tip_dialog:
            tip_dialog.click()

        responsive_table = driver.find_element_by_css_selector('.responsive-table>table')
        # get all of the rows in the table
        rows = responsive_table.find_elements_by_tag_name("tr")
        for row in rows:
            cols = row.find_elements_by_tag_name("td")
            product_name = get_element_text(cols, 0)
            register_code = get_element_text(cols, 1)
            register_name = get_element_text(cols, 2)
            approve_date = get_element_text(cols, 3)
            effective_date = get_element_text(cols, 4)
            count = count + 1
            print("item {}=>{},{},{},{},{}".format(count, product_name, register_code, register_name, approve_date,
                                                   effective_date))
            if product_name:
                contents.append([i, product_name, register_name, register_code, approve_date, effective_date])

        time.sleep(5)


def get_element_text(elements: [], index=0):
    if index >= len(elements):
        return ""

    if elements[index]:
        return elements[index].text

    return ''


if __name__ == '__main__':
    keywords = ['吻合器', '切割闭合器', '超声刀', '超声', '高级能量', '穿刺器']
    process(keywords)
