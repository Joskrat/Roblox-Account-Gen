try:
    from util.updateModule import github_version, updateMain
    from selenium.webdriver.chrome.options import Options
    from util.passwordGen import passwordGen
    from util.plugin import title, clear
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
except Exception as e:
    import os
    from util.plugin import title
    title("Installing requirements")
    os.system("python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks psutil bs4 tqdm")
    from util.updateModule import github_version, updateMain
    from selenium.webdriver.chrome.options import Options
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from util.loginModule import checker
    from multiprocessing import Process
    from util.loginModule import login
    from util.proxyscraper import main
    from pypresence import Presence
    from selenium import webdriver
    from util.plugin import clear
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import time

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
cpath = str(os.getcwd()).replace("\\", "/")

try:
    with open(f"{cpath}/VERSION", "r") as f:
        versions = f.readlines()
        pLocalVer = versions[0].replace("\n", "")
        localVer = versions[0]
except:
    for f in os.listdir('.'):
        if not os.path.isfile(f):
            path = os.path.join('.', f)
            try:
                with open(f"{path}/VERSION", "r") as f:
                    versions = f.readlines()
                    pLocalVer = versions[0].replace("\n", "")
                    localVer = versions[0]
            except:
                pass


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
    if not os.path.isfile(f"{os.getcwd()}/chromedriver.exe"):
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


def gen(timeout, proxy, headless=False):
    while 1:
        username = nameGen()
        password = passwordGen()
        flag = login(str(username), str(password),
                     int(timeout), proxy, bool(headless))
        if flag == False:
            flag = login(str(username), str(password),
                         int(timeout), proxy, bool(headless))
            if flag == False:
                print(f"{err} - Invalid Proxy")


def genMenu():
    print(f"""
        {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
        {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
        {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
        {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
        {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
        {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}
        {w}\n
        {inf} I would recomend not using this program in headless mode cuz at the moment you need to fill out the captchas yourself
            (I'm still working on a bypass)\n\n\n""")

    proxyInput = input(
        f"{w}[{m}>{w}] Want to use proxies (doesnt work well) or manual proxy [y/n/m]: ")
    if proxyInput == "y":
        title("Getting Proxies")
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

    title("Idle")

    headless = input(f"{w}[{m}>{w}] Run chromedriver headless [y/n]: ")
    if headless == "y":
        headless = True
    else:
        headless = False

    threadsInput = input(f"\n[{m}>{w}] Amount of threads: {c}")
    for i in range(int(threadsInput)):
        if proxy != None:
            p = Process(target=gen, args=(10, proxy, headless,))
        else:
            p = Process(target=gen, args=(10, proxyList, headless,))
        p.start()
        processes.append(p)
        title(f"Threads: {threadsInput}")
    print(f"{w}[{g}={w}] -> Threads Started")

    for pr in processes:
        pr.join()
        title("Finished")

    print(f"[{g}={w}] -> Threads Finished, press [{y}ENTER{w}] to exit")
    input()
    exit()


threads = []
processes = []


def mainMenu():
    os.system('mode 130,30')
    title("Idle")
    clear()

    print(f"""
        {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
        {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
        {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
        {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
        {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
        {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}
                                            {w}[{m}DEV{w}]               {c}TerrificTable{w}
                                            {w}[{m}LOCAL-VERSION{w}]     {g}{str(pLocalVer)}{w}
                                            {w}[{m}LASTEST-VERSION{w}]   {g}{str(github_version())}{w}\n\n\n
        """)
    print(f"""
                        [{ml}1{w}] Account Generator
                        [{ml}2{w}] Account Checker
                        [{ml}3{w}] Credits
                        [{ml}X{w}] Exit\n""")
    choise = str(input(f"{w}[{m}>>>{w}] Choise: "))

    if choise == "1":
        clear()
        genMenu()

    elif choise == "2":
        clear()
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print(f"""
            {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
            {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
            {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
            {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
            {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
            {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n
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
        clear()
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

    title("Starting RPC")

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

    clear()
    title("Checking For Updates")
    offVer = github_version()
    updateMain(localVer)

    title("Installing Chromedriver")
    download_chromedriver()
    clear()
    mainMenu()
