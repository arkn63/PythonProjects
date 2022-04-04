import random
import time
import os 
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange

#import warnings
#warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())
url = 'https://'+os.getenv('PAGE')+'.com'
print(url)
if __name__ == '__main__':

    def scroll_to_bottom():
        scroll = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        scroll.maximize_window()
        time.sleep(random.randint(2, 5))
        scroll.get('url')
        time.sleep(random.randint(10,25))
        scroll.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.randint(3,6))
        scroll.close()
        print('DONE')

    def google_traffic():
        #CLASS FROM INPUT FROM GOOGLE.COM
        searchBarInputClass = 'q'
        #CLASS FROM SEARCH BUTTON
        btnClass = 'btnK'
        #LINK FROM WEBSITE TO SEARCH
        link = 'https://'+url+'.com/collections/superfoods'
        scroll = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #scroll = webdriver.Chrome("C:\\DRIVER\\chromedriver.exe")
        scroll.maximize_window()
        time.sleep(random.randint(1, 3))
        scroll.get('https://www.google.com')
        time.sleep(random.randint(2,3))
        scroll.find_element_by_name(searchBarInputClass).send_keys(os.getenv('GOOGLE_SEARCH'))
        time.sleep(random.randint(2, 3))
        scroll.find_element_by_name(btnClass).click()
        time.sleep(random.randint(1, 3))
        scroll.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.randint(4, 6))
        scroll.close()
        print('DONE')

    def click_on_link():
        link_list = ['BLOG', 'BUNDLES', 'SUPERFOODS']
        i = randrange(len(link_list))
        link = link_list[i]
        scroll = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        scroll.maximize_window()
        print('MAXIMIZA VENTANA')
        time.sleep(random.randint(1, 3))
        print('CARGA PÁGINA')
        scroll.get(url)
        print('CLIC EN LINK')
        time.sleep(random.randint(5, 10))
        scroll.find_element_by_partial_link_text(link).click()
        print('ESPERA')
        time.sleep(random.randint(10,100))
        scroll.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.randint(1,3))
        scroll.close()
        print('DONE')

#LIST OF FUNCTION
function_list = [click_on_link, scroll_to_bottom,google_traffic]
#CALLS RANDOM FUNCTION FROM LIST
random.choice(function_list)()
