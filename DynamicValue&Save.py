from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #for local execution
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt

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
  output = text.split(": ")[1]
  return output

def write_file(text):
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(text)

def main():
  driver = get_driver()

  while True:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element.text))
    write_file(text)

print(main())