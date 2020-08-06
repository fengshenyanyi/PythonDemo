import pandas as pd
from requests_html import HTMLSession

URL = 'https://www.jianshu.com/p/85f4624485b9'
SEL = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'


def extract_html():
    session = HTMLSession()
    request = session.get(URL)
    return request.html


def get_text_link_from_html(html):
    requests = html.find(SEL)
    content_list = []
    try:
        for request in requests:
            title = request.text
            link = list(result.absolute_links)[0]
            content_list.append((title, link))
        return content_list
    except:
        None


def convert_results_to_cvg(name):
    df = pd.DataFrame(get_text_link_from_html(extract_html()))
    df.columns = ['text', 'link']
    df.to_csv(name + '.csv', encoding='gbk', index=False)
