import time, requests
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.myrealtrip.com/offers/30162');

html = driver.page_source

time.sleep(2)

x_botton = driver.find_element_by_css_selector('body > div.ab-iam-root.v3.ab-animate-in.ab-animate-out.ab-effect-modal.ab-show > div.ab-in-app-message.ab-background.ab-modal-interactions.ab-modal.ab-centered > button > svg > path').click()

time.sleep(2)



scoop0 = driver.find_element_by_css_selector('#course > div > div > h4').text

time.sleep(2)

scoop2 = driver.find_element_by_css_selector('#course > div > div > div:nth-child(2) > div > div > div.offer-course__introduce--parent > div > div > p').text

time.sleep(2)





courseintro = []
courseintro.append(scoop0)
# print(courseintro)

courses = []
for i in range(1,5):
    title1 = driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[{}]/div/div/div[2]/div/div/div[2]/h5'.format(i)).text
    desc1 = driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[{}]/div/div/div[2]/div/div/p'.format(i)).text
    
    courses.append(
        {
            'title' : title1,
            'desc' : desc1 
        }
    )

    # if '\n' in courses:
        


data = pd.DataFrame(courses)
# print(data)
data.to_csv('courseintro.csv')
    
    # print(title1, desc1)

# print(scoop2)


# driver.quit()

#-----------------------------------

time.sleep(2)

guide_scoop0 = driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/a/h5').text

guide_scoop1 = driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div[1]').text

guideintro = []
guideintro.append(
    {
        'title': guide_scoop0,
        'desc': guide_scoop1
    }
)

data1 = pd.DataFrame(guideintro)
data1.to_csv('guideintro.csv')

driver.quit()

