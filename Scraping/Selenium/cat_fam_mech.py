# the text fields, category, mechanism, and family, were not completely captured by the credit spider
# Selenium is used because it is able to pull the final rendered information

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
import numpy as np


url_df = pd.read_csv('browse_clean.csv')

url_df = url_df.dropna()

# the script was locking up my machine and timing out after ~200 urls
# splitting the URLs into smaller buckets alleviated this and allowed for incremental output
url_s = url_df.full_game_url
url_split = np.array_split(url_s, 160)

n = 0

for array in url_split:
    urls = array.tolist()
    cmf_df = pd.DataFrame(columns = ['url', 'category', 'mechanic', 'family'])
    
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path= r'C:\Users\Sam\Desktop\Capstone\Selenium\geckodriver.exe')
    driver.implicitly_wait(5) # implement 5 second wait per robots.txt
    print ("Headless Firefox Initialized")
    

    for url in urls:        
        driver.get(url)
        print('current url is: ' + str(url))
    
        url_list = []
        url_list.append(url)
    
        category_list = []
        board_game_category = driver.find_elements_by_xpath('//a[contains(@href, "/boardgamecategory/")]')
        for category in board_game_category:
            category_list.append(category.text)
    
        mechanic_list = []
        board_game_mechanic = driver.find_elements_by_xpath('//a[contains(@href, "/boardgamemechanic/")]')
        for mechanic in board_game_mechanic:
            mechanic_list.append(mechanic.text)
    
        family_list = []
        board_game_family = driver.find_elements_by_xpath('//a[contains(@href, "/boardgamefamily/")]')
        for family in board_game_family:
            family_list.append(family.text)
    
        cmf_df = cmf_df.append({'url':url_list, 'category':category_list, 'mechanic':mechanic_list, 'family':family_list}, ignore_index=True)
    cmf_df.to_csv('cmf' + str(n) + '.csv')
    n += 1

    driver.close()

# run this from command line like regular .py script
