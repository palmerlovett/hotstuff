
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
    chrome_options.add_argument("--headless=new")  # Run in headless mode (no UI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1200,800")  # Larger size for better quality
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--hide-scrollbars")
    
    # Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to the URL
    driver.get(url)
    
    # Wait for page to load completely
    time.sleep(3)
    
    # Execute JavaScript to make sure everything is rendered
    driver.execute_script("document.body.style.overflow = 'hidden';")
    
    # Take screenshot
    driver.save_screenshot(output_file)
    print(f"Screenshot saved to {output_file}")
    
    # Close the browser
    driver.quit()
    return True

  except Exception as e:
    print(f"Error taking screenshot: {e}")
    return False
