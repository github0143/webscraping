from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os,sys
import pandas as pd
now = datetime.now()
os.environ["LANG"] = "en_US.UTF-8"
dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "medium")

def get_links():
    try:
        web_page = 'https://medium.com/'
        agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}
        page = requests.get(web_page, headers=agent)
        soup = BeautifulSoup(page.text, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            link_url = link.get('href')
            if "https:" not in link_url:
                links.append('https:' + link_url)
            else:
                links.append(link_url)
        write_to_sheet(links)
    except Exception as e:
        print("error", e.__str__())
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("error in line no", exc_tb.tb_lineno)
        write_to_sheet(links)
        return False
def write_to_sheet(links):
    try:
        file_name = "medium.xlsx"
        full_file_name = os.path.join(dir_path, file_name)
        key = ["Urls"]
        data_frame = pd.DataFrame(links)
        writer = pd.ExcelWriter(full_file_name, engine='xlsxwriter')
        data_frame.to_excel(writer, sheet_name='medium', index=False, header=key)
        print("file created")
        writer.save()
        return True
    except Exception as e:
        print("error occured", e.__str__())
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("error in line no", exc_tb.tb_lineno)

if __name__ == '__main__':
    try:
        get_links()
    except Exception as e:
        print("error", e.__str__())
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("error in line no", exc_tb.tb_lineno)
    exit(0)






