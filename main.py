from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import time

def main():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        oldURL = driver.current_url
        print(oldURL)

        while True:
            time.sleep(1)
            current_url = driver.current_url
            if current_url != oldURL:
                oldURL = current_url
                print(oldURL)
    except WebDriverException as e:
        print("error:", e)
    finally:
        driver.quit()
        print("Browser was closed by user.")

if __name__ == "__main__":
    main()
