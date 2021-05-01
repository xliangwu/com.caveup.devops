import csv


def process():
    rows = []
    with open('个股营收区域结构.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                (matched_keyword, val) = parse_content(row[2])
                print("#{} {} {}=>{}".format(line_count, row[2], matched_keyword, val))
                rows.append([row[0], row[1], row[2], matched_keyword, val])

    print("Process {} rows".format(line_count))

    with open('个股营收区域结构-v2.csv', mode='w', newline='') as output_file:
        output_file_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output_file_writer.writerow(['证券代码', '证券简称', '营收区域结构', '关键词', '提取值'])
        for r in rows:
            output_file_writer.writerow(r)

        print("新的文件已经生成")


def parse_content(content):
    key_words = ["海外", "境外", "国外", '出口', '外销']
    fields = str(content).split(";")
    for f in fields:
        matched = match(key_words, f)
        if matched[0]:
            kv = f.split(":")
            return matched[1], kv[1]

    return "N/A", "N/A"


def match(keywords, content):
    for keyword in keywords:
        if keyword in content:
            return True, keyword

    return False, "N/A"


if __name__ == '__main__':
    process()
