try:
    from multiprocessing import Process, cpu_count
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from util.loginModule import login
    from util.proxyscraper import main
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import os
except:
    import os
    os.system("title Installing requirements")
    os.system("pip install colorama requests wget selenium loguru maxminddb PySocks")
    from multiprocessing import Process, cpu_count
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from util.loginModule import login
    from util.proxyscraper import main
    from colorama import Fore
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
inf = f"[{c}i{w}]"
err = f"[{r}-{w}]"


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


threads = []


processes = []
if __name__ == "__main__":
    os.system('mode 130,30')
    os.system("cls;clear")
    os.system(
        "title Roblox Account Gen   ^|    Installing Chromedriver    ^|   Made by TerrificTable55™#5297")
    download_chromedriver()
    os.system("cls;clear")

    os.system(
        "title Roblox Account Gen   ^|    Idle    ^|   Made by TerrificTable55™#5297")

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

    threadsInput = input(f"\n[{m}>{w}] Amount of threads: {c}")
    for i in range(int(threadsInput)):
        if proxy != None:
            p = Process(target=gen, args=(20, proxy, headless,))
        else:
            p = Process(target=gen, args=(20, proxyList, headless,))
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
