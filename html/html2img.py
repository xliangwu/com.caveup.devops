import imgkit
from bs4 import BeautifulSoup


def html_to_img():
    path_wk = r'E:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config = imgkit.config(wkhtmltoimage=path_wk)
    soup = BeautifulSoup(open(r'20201102汽车数据月度跟踪.htm'), 'html.parser')
    index = 0
    for table in soup.find_all('table'):
        # 读取表格的内容
        table_html_content = table.decode_contents()
        content = str(table_html_content)
        content = r'''<html>
                    <head>
                    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                    </head>
                     <body><div align="center"><table border="0" cellspacing="0" cellpadding="0" width="100%">
                    ''' + content + "</table></div></body>"
        output_path = "t_{}.png".format(index)
        print(content)
        imgkit.from_string(content, output_path=output_path, config=config, cover="test", cover_first=True)
        index = index + 1
        break


def html_file_to_img():
    path_wk = r'E:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config = imgkit.config(wkhtmltoimage=path_wk)
    # imgkit.from_file(open('20201102汽车数据月度跟踪.htm',encoding="gbk"), config=config, output_path="output.png")
    imgkit.from_url('www.baidu.com', config=config, output_path='output.png')


if __name__ == '__main__':
    html_to_img()
