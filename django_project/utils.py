
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def take_screenshot(url, output_file):
    """
    Take a screenshot of a webpage using Selenium and Chrome in headless mode.
    
    Args:
        url (str): URL to capture
        output_file (str): Path to save the screenshot
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")  # Set window size
        
        # Initialize the Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Navigate to the URL
        driver.get(url)
        
        # Wait for page to load completely
        time.sleep(2)
        
        # Take screenshot
        driver.save_screenshot(output_file)
        print(f"Screenshot saved to {output_file}")
        
        # Close the browser
        driver.quit()
        return True
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False
