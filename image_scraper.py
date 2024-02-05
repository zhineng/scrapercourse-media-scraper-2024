import sys,time,os,requests
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://pixabay.com/images/search/car/')

for i in range(4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)


soup = BeautifulSoup(driver.page_source,'lxml')
images = soup.find_all('a',{'class':'link--WHWzm'})
image_links = [image.find('img').get('src') for image in images]

for index,link in enumerate(image_links):

    if not os.path.exists('image'):
        os.mkdir('image')

    img = requests.get(link)


    with open(f'image\\{index+1}.jpg','wb') as file:
        file.write(img.content)