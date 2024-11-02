# app.py
from flask import Flask, render_template, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# Define the function to run Selenium
def run_selenium_script():
    # Set up Chrome options (optional but recommended for headless execution or faster page loading)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    # Uncomment for headless execution
    # chrome_options.add_argument("--headless")

    # Specify the Chrome driver path
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://google.com")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("Selenium WebDriver")
        search_box.submit()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        titles = driver.find_elements(By.XPATH, "//h3")
        for title in titles[:5]:  # Print the top 5 titles
            print(title.text)
    except TimeoutException:
        print("Loading took too much time or the element was not found.")
    finally:
        driver.quit()

# Route to the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to trigger Selenium script
@app.route('/run-script')
def run_script():
    run_selenium_script()  # Run the Selenium code here
    return redirect(url_for('index'))  # Redirect to the home page after running

if __name__ == '__main__':
    app.run(debug=True)
