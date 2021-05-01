import requests
import shutil


def generate_report():
    url = "https://slide.cdn.myslide.cn/ltWJzdn5EWetwBZBvt9BoxYBebBK/slide-{}.jpg"

    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    for i in range(1, 49):
        index = str(i)
        if i < 10:
            index = '0' + str(i)

        new_url = url.format(index)
        print(new_url)
        response = requests.get(new_url, headers=http_header, stream=True)
        response.raise_for_status()
        if response.status_code == 200:
            print("get response is success")
            with open(index + '.jpeg', 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
                f.close()
        else:
            print("Call sonar request has exception")
            break


if __name__ == '__main__':
    generate_report()
