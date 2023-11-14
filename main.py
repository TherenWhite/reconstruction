from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
import keyboard  # Import the keyboard library

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    global oldURL, titles, paragraphs, title_index, paragraph_index
    oldURL = driver.current_url
    titles, paragraphs = [], []
    title_index, paragraph_index = 0, 0

    print("URL:", oldURL)
    titles, paragraphs = get_page_content(driver)
    
    keyboard.add_hotkey('shift+t', print_next_title)
    keyboard.add_hotkey('shift+p', print_next_paragraph)

    try:
        while True:
            time.sleep(1)
            if driver.current_url != oldURL:
                oldURL = driver.current_url
                print("URL:", oldURL)
                titles, paragraphs = get_page_content(driver)
                title_index, paragraph_index = 0, 0
    except WebDriverException:
        print("Browser was closed by the user.")
    finally:
        driver.quit()

def get_page_content(driver):
    try:
        titles = [title.text for title in driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")]
        paragraphs = [paragraph.text for paragraph in driver.find_elements(By.TAG_NAME, "p")]
        return titles, paragraphs
    except Exception as e:
        print("error:", e)
        return [], []

def print_next_title():
    global title_index, titles
    if title_index < len(titles):
        print("Title:", titles[title_index])
        title_index += 1
    else:
        print("No more titles.")

def print_next_paragraph():
    global paragraph_index, paragraphs
    if paragraph_index < len(paragraphs):
        print("Paragraph:", paragraphs[paragraph_index])
        paragraph_index += 1
    else:
        print("No more paragraphs.")

if __name__ == "__main__":
    main()
