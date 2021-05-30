import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import date

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def process(keyword=''):
    if not keyword:
        print("parameter keyword can't be empty")
        return

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
    })

    driver.get(r'http://app1.nmpa.gov.cn/data_nmpa/face3/dir.html')
    time.sleep(30)
    category_links = driver.find_elements_by_tag_name("a")
    for link in category_links:
        title = link.get_attribute("title")
        print(">>>", title)
        if title != '国产一、二、三类注册器械信息' and title != '进口一、二、三类注册器械信息':
            continue

        print("start to crawl for keyword:{}=>{}".format(keyword, title))
        link.click()
        driver.refresh()
        time.sleep(30)
        try:

            keyword_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "keyword"))
            )

            keyword_input.send_keys(keyword)
            query_btn = driver.find_element_by_xpath("//input[@type='submit' and @name='Submit']")
            time.sleep(3)
            query_btn.click()
            contents = []
            try:
                content_div = driver.find_element_by_id('content')
                table_elements = content_div.find_elements_by_tag_name('table')

                total_label = table_elements[0].txt
                total = "".join(filter(str.isdigit, total_label))
                print("Total pages:", total)

                index = 0
                page_size = math.ceil(total / 15)

                for page_index in range(1, page_size):
                    all_links = table_elements[1].find_elements_by_tag_name("a")
                    for link in all_links:
                        print("process link:", link.text)
                        process_one_page(driver, index, keyword, contents)
                        time.sleep(5)

                    content_div = driver.find_element_by_id('content')
                    table_elements = content_div.find_elements_by_tag_name('table')
                    next_page = table_elements[3].find_elements_by_tag_name('img')[2]
                    if page_index < page_size:
                        next_page.click()
                print("end to crawl for keyword:", keyword)
            except Exception as ex:
                print(ex)

            save_data(contents)
            contents.clear()
        except Exception as e:
            print(e)
            print("crawl failed for keyword:", keyword)


def process_one_page(driver: webdriver.Chrome, index='', keyword='', contents=[]):
    main_tables = driver.find_elements_by_css_selector('.listmain>table')
    if not main_tables:
        print("没有找到分页，可能是没有数据")
        return

    data_table = main_tables[0]
    back_btn = data_table.find_element_by_tag_name('img')
    # get all of the rows in the table
    rows = data_table.find_elements_by_tag_name("tr")
    product_name = get_element_text(rows[5])
    register_code = get_element_text(rows[1])
    register_name = get_element_text(rows[2])
    approve_date = get_element_text(rows[15])
    effective_date = get_element_text(rows[16])
    print("item {}=>{},{},{},{},{}".format(index, keyword, product_name, register_code, register_name, approve_date,
                                           effective_date))
    if product_name:
        contents.append([index, keyword, product_name, register_name, register_code, approve_date, effective_date])

    back_btn.click()


def get_element_text(row: WebElement):
    cols = row.find_elements_by_tag_name("td")
    if not cols or len(cols) < 2:
        return ''

    return cols[1].text


def find_element(driver: webdriver.Chrome, byType, selector):
    try:
        element = driver.find_element(byType, selector)
        return True, element
    except NoSuchElementException:
        return False, None


def save_data(contents: [], keyword=''):
    today = date.today()
    today_label = today.strftime("%yy%m%d")
    output = "nmpa_data_{}_{}.csv".format(keyword, today_label)
    with open(output, 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['产品名称', '注册证编号', '注册人名称', '批准日期 ', '有效期'])
        for content in contents:
            writer.writerow(content)

    print("save data is done =>", output)


if __name__ == '__main__':
    # keywords = ['吻合器', '切割闭合器', '超声刀', '超声', '高级能量', '穿刺器']
    keywords = ['高级能量']
    process("高级能量")
