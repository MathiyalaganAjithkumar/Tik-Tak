from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

# Set up Chrome options (optional but recommended for headless execution or faster page loading)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start maximized for full-page interaction
chrome_options.add_argument("--disable-gpu")      # Disable GPU for compatibility
# chrome_options.add_argument("--headless")       # Uncomment for headless execution (no GUI)

# Specify the Chrome driver path
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to Google
    driver.get("https://google.com")
    
    # Wait for the search box to load and be interactive
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    # Input a search term and submit
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()
    
    # Wait for the results page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    
    # Extract and print titles of the search results
    titles = driver.find_elements(By.XPATH, "//h3")
    for title in titles[:5]:  # Print the top 5 titles
        print(title.text)

except TimeoutException:
    print("Loading took too much time or the element was not found.")

finally:
    # Close the browser
   driver.quit()
