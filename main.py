from util.passwordGen import passwordGen
from util.usernameGen import nameGen
from util.loginModule import login
from colorama import Fore
import threading
import requests
import zipfile
import wget
import os

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
ml = Fore.LIGHTMAGENTA_EX
m = Fore.MAGENTA
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


def download_chromedriver():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + \
        version_number + "/chromedriver_win32.zip"

    latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(latest_driver_zip)


def gen():
    username = nameGen()
    password = passwordGen()
    login(str(username), str(password))


threads = []
if __name__ == "__main__":
    os.system('mode 110,25')
    os.system("cls;clear")
    os.system(
        "title Roblox Account Gen ^|    Idle    ^| Made by TerrificTable55™#5297")
    download_chromedriver()
    threadsInput = input(f"[{m}>{w}] Amount of threads: {c}")

    for i in range(int(threadsInput)):
        os.system(
            f"title Roblox Account Gen ^|  Threads: {threadsInput}  ^| by TerrificTable55™#5297")
        thread = threading.Thread(target=gen)
        thread.start()
        threads.append(thread)
    print(f"{w}[{g}={w}] -> Threads Started")

    for thread in threads:
        thread.join()
        os.system(
            "title Roblox Account Gen ^|  Finished  ^| by TerrificTable55™#5297")
    print(f"[{g}={w}] -> Threads Finished, press [{y}ENTER{w}] to exit")
    input()
    exit()
