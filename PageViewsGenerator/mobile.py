import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#import warnings
#warnings.filterwarnings("ignore")

mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

scroll = webdriver.Chrome("C:\\DRIVER\\chromedriver.exe",chrome_options=chrome_options)
wait = WebDriverWait(scroll,10)

if __name__ == '__main__':
    def scroll_to_bottom():
        print('SCROLL TO BOTTOM MOBILE')    
        time.sleep(random.randint(1, 3))
        time.sleep(random.randint(10, 25))
        scroll.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        print('HACE SCROLL HASTA EL FINAL')
        time.sleep(random.randint(1, 6))
        scroll.close()
        print('DONE')

    def click_on_link():
        link_list = ['RECIPES', 'BUNDLES', 'SUPERFOODS']
        i = randrange(len(link_list))
        link = link_list[i]
        print('TAP ON LINK '+link)
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        url = "https://shopkarenberrios.com/"

        time.sleep(random.randint(3, 5))
        scroll.get(url)
        nav_bar = 'm-menu-btn'
        print('INICIA ESPERA DEL WAIT')
        print('TERMINA ESPERA DEL WAIT')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"m-menu-btn"))).click()
        print('CLICK EN NAV BAR')
        #time.sleep(random.randint(2, 5))
        #scroll.find_element_by_class_name(nav_bar).click()
        #time.sleep(random.randint(1, 3))
        #scroll.find_element_by_partial_link_text(link).click()
        time.sleep(random.randint(10, 100))
        scroll.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.randint(1, 3))
        print('DONE')

    function_list = [click_on_link]
    random.choice(function_list)()
    scroll.close()
