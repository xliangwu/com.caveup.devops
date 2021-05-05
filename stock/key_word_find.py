import pandas as pd
import re


def search_by_keyword(pattern='', contents=[]):
    if len(contents) <= 0:
        return False

    for content in contents:
        if not content or len(str(content).strip()) <= 0:
            continue

        regex = re.compile(pattern, re.M | re.I)
        result = re.search(regex, content)
        if result:
            return True

    return False


def process():
    input_file = '公司简介.xlsx'
    df = pd.read_excel(input_file, header=0)
    print(df.head())

    # 空的表格填充为0
    df.fillna(0, inplace=True)
    total_row = len(df)

    keywords = ['石库门上海老酒', '海上大味道专卖店']
    matched = []
    keyword_line = "|".join(keywords)
    pattern_str = ".*({}).*".format(keyword_line)
    print("匹配模式：", pattern_str)

    for index, row in df.iterrows():
        company_desc = row['公司简介']
        company_product_type = row['主营产品类型']
        company_product_info = row['主营产品名称']
        code = row['证券代码']

        print("处理第{}/{}行 ==> {}".format(index, total_row, code))
        if search_by_keyword(pattern_str, [company_desc, company_product_type, company_product_info]):
            matched.append((code, row['证券名称']))

    print("\n\n\n-----------------------")
    print("匹配的证券代码\t证券名称")
    for item in matched:
        print(item[0], '\t', item[1])


def match(keyword=[], text=[]):
    return True


if __name__ == '__main__':
    process()
