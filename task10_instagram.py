from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up Chrome WebDriver (ensure you have chromedriver installed and in your PATH)
driver = webdriver.Chrome()

# Navigate to the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")

try:
    # Wait for the follower count element to be visible
    followers_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Followers")]/span'))
    )

    # Wait for the following count element to be visible
    following_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Following")]/span'))
    )

    # Extract follower and following counts
    followers_count = followers_element.text
    following_count = following_element.text

    print("Followers:", followers_count)
    print("Following:", following_count)

except TimeoutException:
    print("TimeoutException: Could not find follower or following count elements")

# Close the WebDriver
driver.quit()
