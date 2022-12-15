from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #for local execution

service = Service('G:\\Meu Drive\\Cursos\\Scrape-Simple-Text-with-Selenium\\chromedriver.exe')

def get_driver():
  # Set option to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage") #This option is to avoid some issues with Linux
  options.add_argument("no-sandbox") #disabled the security
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disabled-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())