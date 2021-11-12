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


def main(bot, username, password, timeout):
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
        bot.close()
    except:
        print("ERROR")
        pass


def checker(bot, username: str, password: str):
    bot.get("https://www.roblox.com/login")

    usernameInput = bot.find_element_by_xpath('//*[@id="login-username"]')
    passwordInput = bot.find_element_by_xpath('//*[@id="login-password"]')
    login = bot.find_element_by_xpath('//button[@id="login-button"]')

    # Username
    usernameInput.clear()
    usernameInput.send_keys(username)

    # Password
    passwordInput.clear()
    passwordInput.send_keys(password)

    # Login
    bot.execute_script("arguments[0].click();", login)
    time.sleep(20)

    try:
        if str(bot.find_element_by_xpath('//p[@class="form-control-label xsmall text-error login-error ng-binding"]')) != "":
            log(username, password, False)
            return False
        else:
            log(username, password, True)
            return True
    except:
        log(username, password, True)
        return True


def log(username, password, valid):
    if valid == True:
        print(f"[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {g}Valid{w}\n\n")

        with open("./logins.txt", "a") as f:
            f.write(f"[Info] {username}:{password}\n")

    elif valid == False:
        print(f"[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {r}Invalid{w}\n\n")

    else:
        pass


def login(username: str, password: str, timeout: int, proxyList, headless: bool = True):
    options = Options()
    options.headless = headless
    if proxyList != None:
        proxy = random.choice(proxyList)
        options.add_argument(f'--proxy-server={proxy}')
        time.sleep(12)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    bot = webdriver.Chrome(chrome_options=options)
    bot.get("https://roblox.com")
    time.sleep(3)

    if len(username) > 20:
        username = str(username[:20])

    try:
        main(bot, username, password, timeout)
        checker(bot, username, password)
        return True
    except:
        bot.close()
        return False
