from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to FitPeo Homepage
    driver.get("https://www.fitpeo.com/")
    print("Navigated to FitPeo Homepage")

    # Wait for the "Revenue Calculator" link to be clickable and then click it
    try:
        revenue_calculator_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))
        )
        revenue_calculator_link.click()
        print("Clicked on Revenue Calculator link")
    except TimeoutException:
        print("Timeout while waiting for Revenue Calculator link")
        driver.quit()
        exit()

    # Wait for the Revenue Calculator page to load
    try:
        page_loaded_indicator = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )
        print("Revenue Calculator page loaded")
    except TimeoutException:
        print("Timeout while waiting for Revenue Calculator page to load")
        driver.quit()
        exit()

    # Scroll down to the Slider section using JavaScript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(2)

    # Locate the slider element and adjust its value
    try:
        slider = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".slider-handle"))  # Update the selector if needed
        )
        ActionChains(driver).click_and_hold(slider).move_by_offset(100, 0).release().perform()  # Adjust the offset as needed
        time.sleep(2)
        print("Adjusted the slider")

        # Validate that the text field value is updated
        text_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".slider-input"))  # Update the selector if needed
        )
        text_field_value = text_field.get_attribute('value')
        print(f"Text field value after slider adjustment: {text_field_value}")
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
        print(f"Error adjusting and validating the slider: {e}")
        driver.quit()
        exit()

    print("Script executed successfully.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Closed the browser")
