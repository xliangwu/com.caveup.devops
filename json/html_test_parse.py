from bs4 import BeautifulSoup


def process():
    with open('a.html', "r", encoding="utf-8") as f:
        content = f.readlines()
        doc_ele = BeautifulSoup(str(content), "html.parser")

        li_eles = doc_ele.find_all("li")
        for ele in li_eles:
            # row_text = ele.text
            # row_text = str(row_text).replace("\\n', '", "").strip()
            # print(row_text)
            content = []
            for child in ele.children:
                try:
                    content.append(child.get_text())
                except AttributeError:
                    pass
            # fields = row_text.split(" ")
            fields = str(content[0]).replace("\\n', '", "").strip().split("|");
            print(fields[0].strip(), "\t", fields[1].strip(), "\t", content[1])


if __name__ == '__main__':
    process()
