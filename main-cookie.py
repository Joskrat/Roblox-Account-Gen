try:
    from selenium.webdriver.chrome.options import Options
    from util.loginModuleNotWorking import login
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from util.loginModule import checker
    from multiprocessing import Process
    from util.proxyscraper import main
    from pypresence import Presence
    from selenium import webdriver
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import time
    import os
except:
    import os
    os.system("title Installing requirements")
    os.system("python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks")
    from selenium.webdriver.chrome.options import Options
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from util.loginModule import checker
    from multiprocessing import Process
    from util.loginModule import login
    from util.proxyscraper import main
    from pypresence import Presence
    from selenium import webdriver
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import time
    import os

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
ml = Fore.LIGHTMAGENTA_EX
m = Fore.MAGENTA
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE
inf = f"[{c}i{w}]"
err = f"[{r}-{w}]"


def rpc(name: str, largeText: str, largeImage: str, smallText: str, smallImage: str, linkText, link: str, link2Text, link2: str):
    buttonList = [
        {
            "label": linkText,
            "url": link
        },
        {
            "label": link2Text,
            "url": link2
        }
    ]

    rpc = Presence("909446204029550605")
    rpc.connect()

    rpc.update(
        details=name,
        large_text=largeText,
        large_image=largeImage,
        small_text=smallText,
        small_image=smallImage,
        buttons=buttonList,
        start=time.time()
    )


def download_chromedriver():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + \
        version_number + "/chromedriver_win32.zip"

    latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
        print("Chromedriver Installed")
    os.remove(latest_driver_zip)


# def start(threadsAmt, timeout: int):
#     for i in range(int(threadsAmt)):
#         thread = threading.Thread(target=gen, args=(timeout,))
#         thread.start()
#         threads.append(thread)
#     print(f"{w}[{g}={w}] -> Threads Started")

#     for thread in threads:
#         thread.join()
#     print(f"[{g}={w}] -> Threads Finished, press [{y}ENTER{w}] to exit")
#     input()
#     exit()


def gen(timeout, proxy, cookie, headless=False):
    while 1:
        username = nameGen()
        password = passwordGen()
        flag = login(str(username), str(password),
                     int(timeout), proxy, bool(cookie), bool(headless))
        if flag == False:
            flag = login(str(username), str(password),
                         int(timeout), proxy, bool(cookie), bool(headless))
            if flag == False:
                print(f"{err} - Invalid Proxy")


def genMenu():
    print(f"""
        {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
        {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
        {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
        {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
        {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
        {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}\n
        {inf} I would recomend not using this program in headless mode cuz at the moment you need to fill out the captchas yourself
            (I'm still working on a bypass)\n\n\n""")

    proxyInput = input(
        f"{w}[{m}>{w}] Want to use proxies (doesnt work well) or manual proxy [y/n/m]: ")
    if proxyInput == "y":
        os.system(
            "title Roblox Account Gen   ^|    Getting Proxies    ^|   Made by TerrificTable55™#5297")
        proxies = main()
        proxyList = []
        for proxy in proxies:
            if str(proxy).__contains__(":"):
                proxyList.append(proxy)

    elif proxyInput == "m":
        proxy = input(f"{w}[{m}>{w}] Proxy (IP:Port): ")

    else:
        proxyList = None
        proxy = None

    os.system(
        "title Roblox Account Gen   ^|    Idle    ^|   Made by TerrificTable55™#5297")

    headless = input(f"{w}[{m}>{w}] Run chromedriver headless [y/n]: ")
    if headless == "y":
        headless = True
    else:
        headless = False

    cookie = input(f"{w}[{m}>{w}] Collect .ROBLOXSECURITY Cookie [y/n]: ")
    if cookie == "y":
        cookie = True
    else:
        cookie = False

    threadsInput = input(f"\n[{m}>{w}] Amount of threads: {c}")
    for i in range(int(threadsInput)):
        if proxy != None:
            p = Process(target=gen, args=(20, proxy, cookie, headless,))
        else:
            p = Process(target=gen, args=(20, proxyList, cookie, headless,))
        p.start()
        processes.append(p)
        os.system(
            f"title Roblox Account Gen   ^|  Threads: {threadsInput}  ^|   by TerrificTable55™#5297")
    print(f"{w}[{g}={w}] -> Threads Started")

    for pr in processes:
        pr.join()
        os.system(
            "title Roblox Account Gen   ^|  Finished  ^|   by TerrificTable55™#5297")
    print(f"[{g}={w}] -> Threads Finished, press [{y}ENTER{w}] to exit")
    input()
    exit()


threads = []
processes = []


def mainMenu():
    os.system('mode 130,30')
    os.system("cls;clear")

    os.system(
        "title Roblox Account Gen   ^|    Idle    ^|   Made by TerrificTable55™#5297")
    # rpc("Roblox Account Generator - Idle", largeText, largeKey, smallText,
    #     smallKey, link1Text, link1Url, link2Text, link2Url)

    print(f"""
        {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
        {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
        {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
        {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
        {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
        {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}\n\n\n\n""")
    print(f"""
                            [{ml}1{w}] Account Generator
                            [{ml}2{w}] Account Checker
                            [{ml}3{w}] Credits
                            [{ml}X{w}] Exit\n""")
    choise = str(input(f"{w}[{m}>>>{w}] Choise: "))

    if choise == "1":
        os.system("cls;clear")
        # rpc("Roblox Account Generator - Generator", largeText, largeKey, smallText,
        #     smallKey, link1Text, link1Url, link2Text, link2Url)
        genMenu()

    elif choise == "2":
        os.system("cls;clear")
        # rpc("Roblox Account Generator - Acc Checker", largeText, largeKey, smallText,
        #     smallKey, link1Text, link1Url, link2Text, link2Url)

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print(f"""
            {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
            {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
            {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
            {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
            {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
            {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}\n
            {inf} I would recomend not using this program in headless mode cuz at the moment you need to fill out the captchas yourself
                (I'm still working on a bypass)\n\n\n""")
        headless = input(f"{w}[{m}>{w}] Headless [y/n]: ")

        if headless == "y":
            headless = True
        else:
            headless = False

        username = input(f"\n{w}[{m}>{w}] Username: ")
        password = input(f"{w}[{m}>{w}] Password: ")

        options.headless = headless
        bot = webdriver.Chrome(chrome_options=options)
        checker(bot, username, password)
        input()
        mainMenu()

    elif choise == "3":
        os.system("cls;clear")
        # rpc("Roblox Account Generator - Credits", largeText, largeKey, smallText,
        #     smallKey, link1Text, link1Url, link2Text, link2Url)
        print("""
                [x]========[x]====================[x]
                 ║ Made By  ║ TerrificTable        ║
                [x]========[x]====================[x]
        """)
        input()
        mainMenu()

    elif choise == "4" or choise.lower() == "x":
        exit()


if __name__ == "__main__":
    global appid, largeText, largeKey, smallText, smallKey, link1Text, link1Url, link2Text, link2Url

    os.system(
        "title Roblox Account Gen   ^|    Starting RPC    ^|   Made by TerrificTable55™#5297")

    largeText = "RobloxGen"
    largeKey = "large"
    smallText = "by TerrificTable"
    smallKey = "small"

    link1Text = "Github"
    link1Url = "https://github.com/TerrificTable"
    link2Text = "This Program"
    link2Url = "https://github.com/TerrificTable/Roblox-Account-Gen"

    rpc("Roblox Account Generator", largeText, largeKey, smallText,
        smallKey, link1Text, link1Url, link2Text, link2Url)

    os.system("cls;clear")
    os.system(
        "title Roblox Account Gen   ^|    Installing Chromedriver    ^|   Made by TerrificTable55™#5297")
    download_chromedriver()
    os.system("cls;clear")
    mainMenu()
