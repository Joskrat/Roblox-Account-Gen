from selenium.common.exceptions import NoSuchElementException
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
        checker(bot, username, password)
    except Exception as e:
        print("ERROR, " + e)
        bot.close()

# time.sleep(1)
# try:
#     invalid = bot.find_element_by_xpath(
#         '//*[@id="signup-usernameInputValidation"]')  # /text()

#     if invalid != None or str(invalid) != "":
#         print(invalid)
#         log(username, password, None)
#         # bot.close()
# except Exception as e:
#     print("unavailable " + e)
#     # log(username, password, True)
#     pass


def checker(bot, username: str, password: str):
    bot.get("https://www.roblox.com/login")
    time.sleep(3)

    try:
        usernameInput = bot.find_element_by_xpath('//*[@id="login-username"]')
        print("username")
        passwordInput = bot.find_element_by_xpath('//*[@id="login-password"]')
        print("password")
        login = bot.find_element_by_xpath('//button[@id="login-button"]')
        print("username")
        accept = bot.find_element_by_xpath(
            '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')
        print("accept")

        # Username
        usernameInput.clear()
        usernameInput.send_keys(username)
        print("Username filledout")

        # Password
        passwordInput.clear()
        passwordInput.send_keys(password)
        print("Password Filledout")

        # Login
        time.sleep(2)
        accept.click()
        print("accept clicked")
        time.slee(1)
        bot.execute_script("arguments[0].click();", login)
        print("login clicked")
        time.sleep(10)

        try:
            if str(bot.find_element_by_xpath('//p[@class="form-control-label xsmall text-error login-error ng-binding"]')) != "":
                log(username, password, False)
                bot.close()
            else:
                log(username, password, True)
                bot.close()
        except:
            log(username, password, True)
            bot.close()

    except:
        log(username, password, True)
        bot.close()


def log(username, password, valid):
    if valid == True:
        print(f"\n[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {g}Valid{w}\n")

        with open("./logins.txt", "a") as f:
            f.write(f"[Info] {username}:{password}\n")

    elif valid == False:
        print(f"\n[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {r}Invalid{w}\n")

    elif valid == None:
        print(f"\n[{r}Username Unavalable or Inapropreat{w}]")

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
        # checker(bot, username, password)
        return True
    except Exception as e:
        print(e)
        bot.close()
        return False
