from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #for local execution
from selenium.webdriver.common.keys import Keys

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
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  #time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  #time.sleep(2)
  driver.find_element(by="xpath", value="html/body/nav/div/a").click()
  #time.sleep(2)
  userElement = driver.find_element(by="xpath", value="/html/body/nav/div/div/div[2]/div")
  time.sleep(2)
  temperatureElement = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  temperatureElement = clean_text(temperatureElement.text)

  print("The user is " + userElement.text + ", and the temperature world is " + str(temperatureElement))
  print(driver.current_url)

print(main())