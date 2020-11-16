from selenium import webdriver
import time
import sys
import time
import threading
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.cxldk.mongodb.net/"
                     "codes?retryWrites=true&w=majority")
db = client["moviedb"]
movies = db["movies"]


driver = webdriver.Firefox()
driver.get("https://reelgood.com/movies/source/netflix")
driver.maximize_window()
time.sleep(10)
for i in range(1, 150):
    print(i)
    time.sleep(3)
    imgofthemovie = driver.find_element_by_xpath(
        f"/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[1]/a/div/picture/img").get_attribute('src')
    print(imgofthemovie)
    nameofthemovie = driver.find_element_by_xpath(
        f"/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[2]/a").text
    print(nameofthemovie)
    yearofthemovie = driver.find_element_by_xpath(
        f"/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[4]").text
    print(yearofthemovie)
    ratingofthemovie = driver.find_element_by_xpath(
        f"/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[5]").text
    print(ratingofthemovie)
    imdbratingofthemovie = driver.find_element_by_xpath(
        f"/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[6]/b/div/span/b").text
    print(imdbratingofthemovie)
    driver.find_element_by_xpath(
        f'/html/body/div[1]/div[5]/main/div[5]/div/table/tbody/tr[{i}]/td[2]/a').click()
    time.sleep(2)

    genreofthemovie = driver.find_element_by_css_selector(
        f"span.css-ee2w7g:nth-child(3) > a:nth-child(1)").text
    print(genreofthemovie)
    driver.find_element_by_css_selector(
        'html body div#app_mountpoint div main div section.css-vzt30e.e14injhv0 nav.css-sfymjb.e14injhv1 a.css-mr066l').click()
    print("\n\n\n\n")
    movies.insert_one({"name": nameofthemovie, "age": float(ratingofthemovie), "yearpublished": float(yearofthemovie),
                       "imdbrating": imdbratingofthemovie, "genre": genreofthemovie, "img": imgofthemovie})
