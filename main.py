from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
isBrowserOpen = False



def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    isBrowserOpen = True
    oldURL = driver.current_url
    print(oldURL)
    
    title = driver.find_element(By.TAG_NAME, "title").get_attribute('textContent')
    print(f"Title: {title}")

    try:
        while True:
            time.sleep(1)
            driver.current_url
            if driver.current_url != oldURL:
                oldURL = driver.current_url
                print(oldURL)
                title = driver.find_element(By.TAG_NAME, "title").get_attribute('textContent')
                print(f"Title: {title}")

        try:
            main_article = driver.find_element(By.TAG_NAME, "article").get_attribute('outerHTML')
            print(f"Main Article: {main_article}")
        except:
            print("Main article element not found.")
        driver.quit()

    except WebDriverException:
        isBrowserOpen = False
        print("Browser was closed by the user.")



main()
