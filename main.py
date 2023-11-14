from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    oldURL = driver.current_url
    print("URL:", oldURL)
    print_page_content(driver)

    try:
        while True:
            time.sleep(1)
            if driver.current_url != oldURL:
                oldURL = driver.current_url
                print("URL:", oldURL)
                print_page_content(driver)
    except WebDriverException:
        print("Browser was closed by the user.")
    finally:
        driver.quit()

def print_page_content(driver):
    try:
        titles = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
        for title in titles:
            print("Title:", title.text)

        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print("Paragraph:", paragraph.text)
    except Exception as e:
        print("An error occurred while trying to read the page content:", e)

if __name__ == "__main__":
    main()
