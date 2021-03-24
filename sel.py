from selenium.webdriver import Chrome
import pandas as pd
webdriver = "D:/chromedriver.exe"
driver = Chrome(webdriver)
pages = 4
total = []
for page in range(0,pages):
    url = "https://www.energy.gov/listings/energy-news?page=" + str(page) + "/"
    driver.get(url)
    article_date = driver.find_elements_by_class_name('date')
    article_title = driver.find_elements_by_class_name('title-link')
    article_description=driver.find_elements_by_xpath('.//div[@class="field-item odd"]')
    article_url=driver.find_elements_by_class_name('title-link')
    num_page_items = len(article_date)
    for i in range(num_page_items):
        print(article_date[i].text + " : " + article_title[i].text + ":" + article_description[i].text + ":" + article_url[i].get_attribute('href'))
        new = ((article_date[i].text,article_title[i].text,article_description[i].text,article_url[i].get_attribute('href')))
        total.append(new)
driver.close()
df = pd.DataFrame(total,columns=['article_date','article_title','article_description','article_url'])
df.to_excel('energygov_selenium.xlsx')
