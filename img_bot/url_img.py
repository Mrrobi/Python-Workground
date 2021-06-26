import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# DRIVER_PATH = 'E:\Robiuddin-PC\PythonWorkbook\img_bot\chromedriver_win32\chromedriver.exe'
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
# driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
# driver.get("https://bloodlink.mrrobi.tech/Welcome/?url=https://www.instagram.com/p/CEekIGOpRk3/")
# driver.execute_script("document.getElementsByClassName('ibutton')[0].click()")
# driver.implicitly_wait(45)

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print(elem.get_attribute("href"))
#     img_name = random.randrange(1,500)
#     full_name = str(img_name)+".jpg"
#     urllib.request.urlretrieve(elem.get_attribute("href"),full_name)
# #driver.quit()


op = Options()
op.headless = True
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)

driver.get("https://bloodlink.mrrobi.tech/Welcome/?url=https://www.instagram.com/p/CEekIGOpRk3/")
driver.execute_script("document.getElementsByClassName('ibutton')[0].click()")
driver.implicitly_wait(45)
print(driver.page_source)
elems = driver.find_elements_by_xpath("//a[@href]")
print(elems)
for elem in elems:
    print(elem.get_attribute("href"))
    #img_name = random.randrange(1,500)
    #full_name = str(img_name)+".jpg"
    #urllib.request.urlretrieve(elem.get_attribute("href"),full_name)
 #driver.quit()