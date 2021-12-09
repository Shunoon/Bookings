import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def main():
    # Choosing browser & connecting chrome driver
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    # Opening website and clicking screening 1 in a while loop every 5 seconds
    website = "https://www.cinema.mv/movie/spider-man-no-way-home"
    while True:
        try:
            driver.get(website)
            link = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[4]/ul/li[1]/a')
            link.click()
            break
        except NoSuchElementException:
            time.sleep(5)
    try:
        # Choosing the seats
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3890'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3899'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3908'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3917'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3926'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3931'))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '3944'))
        )
        element.click()

        # Filling the info        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )
        element.send_keys(sys.argv[1])

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        element.send_keys(sys.argv[2])

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'phone'))
        )
        element.send_keys(sys.argv[3])
        
        # Clicking book
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="scrolled-area"]/div[3]/div/div[4]/a[1]'))
        )
        element.click()

        # Confirming book
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="scrolled-area"]/div[2]/form/div/div[4]/input'))
        )
        element.click()

    except:
        driver.quit()

if __name__ == "__main__":
    main()











    # notes

    # *** website ***

    # one word movies capital first Letter
    # 2 worded movies simple and dashes
    # ex= https://www.cinema.mv/movie/resident-evil-welcome-to-raccoon-city
    # Resident Evil: Welcome to Raccoon City
    # hence spiderman would be;
    # https://www.cinema.mv/movie/spider-man-no-way-home
    # Spider-Man: No Way Home

    # *** Movie paths ***

    # //*[@id="container"]/div[2]/div/div[4]/ul/li[1]/a Sooryavanshi 1st screening path
    # //*[@id="container"]/div[2]/div/div[4]/ul/li[1]/a Eternals 1st screening path
    # //*[@id="container"]/div[2]/div/div[4]/ul/li[2]/a Encanto 1st screening disabled so 2nd screening path
    # //*[@id="container"]/div[2]/div/div[4]/ul/li[1]/a Resident evil racoon city 1st screening path
    # //*[@id="container"]/div[2]/div/div[4]/ul/li[2]/a satyameva jayate 2 1st screening disabled so 2nd screening path
    # hence spiderman would be;
    # //*[@id="container"]/div[2]/div/div[4]/ul/li[1]/a

    # *** book 7 seats ***

    # seats C12 to C6
    # C12 = 3890
    # C11 = 3899
    # C10 = 3908
    # C9 = 3917
    # C8 = 3926
    # C7 = 3931
    # C6 = 3944

    # *** fill info and book ***

    # name = shunan
    # email = shunanshareef1@gmail.com
    # number = 710191096
    # first book = //*[@id="scrolled-area"]/div[3]/div/div[4]/a[1]
    # confirm book = 



