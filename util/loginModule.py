from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from colorama import Fore
import random
import time


months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


def login(username: str, password: str, timeout: int, headless: bool = True):
    options = Options()
    options.headless = headless
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    bot = webdriver.Chrome(chrome_options=options)
    bot.get("https://roblox.com")
    time.sleep(3)

    if len(username) > 20:
        username = str(username[:20])

    day = Select(bot.find_element_by_xpath('//*[@id="DayDropdown"]'))
    month = Select(bot.find_element_by_xpath('//*[@id="MonthDropdown"]'))
    year = Select(bot.find_element_by_xpath('//*[@id="YearDropdown"]'))
    usernameInput = bot.find_element_by_xpath('//*[@id="signup-username"]')
    passwordInput = bot.find_element_by_xpath('//*[@id="signup-password"]')
    register = bot.find_element_by_xpath('//*[@id="signup-button"]')
    accept = bot.find_element_by_xpath(
        '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')

    # Dob - Day Selector
    dayVal = random.randint(1, 27)
    if dayVal < 10:
        dayVal = "0" + str(dayVal)
    day.select_by_value(str(dayVal))
    # time.sleep(1)

    # Dob - Month Selector
    monthVal = random.choice(months)
    month.select_by_visible_text(str(monthVal))
    # time.sleep(1)

    # Dob - Year Selector
    yearVal = random.randint(1960, 2010)
    year.select_by_visible_text(str(yearVal))
    # time.sleep(1)

    # Username
    usernameInput.clear()
    usernameInput.send_keys(username)

    # Password
    passwordInput.clear()
    passwordInput.send_keys(password)

    # Register
    try:
        accept.click()
        time.sleep(1)
        register.click()
        time.sleep(timeout)
        # Log
        print(f"[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w}\n[{c}Day{w}]      {m}{dayVal}{w} \n[{c}Month{w}]    {m}{monthVal}{w} \n[{c}Year{w}]     {m}{yearVal}{w}\n\n")
        with open("./logins.txt", "a") as f:
            f.write(f"[Username] {username} \n[Password] {password}\n\n\n")
        bot.close()
    except:
        print("ERROR")
        pass
