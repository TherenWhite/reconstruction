from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import time
isBrowserOpen = False
driver = webdriver.Chrome(ChromeDriverManager().install())

# async def browserTracking():
#     try:
#         while True:
#             time.sleep(1)
#             driver.current_url
#             if driver.current_url != oldURL:
#                 oldURL = driver.current_url
#                 print(oldURL)
#     except WebDriverException:
#         isBrowserOpen = False
#         print("Browser was closed by the user.")



def main(): 
    driver.get("https://www.google.com/")
    isBrowserOpen = True
    oldURL = driver.current_url
    print(oldURL)
    
    try:
        while True:
            time.sleep(1)
            driver.current_url
            if driver.current_url != oldURL:
                oldURL = driver.current_url
                print(oldURL)
    except WebDriverException:
        isBrowserOpen = False
        print("Browser was closed by the user.")

    

main()