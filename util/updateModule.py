from zipfile import ZipFile
import requests
import shutil
import time
import os


def github_version():
    try:
        version = requests.get(
            "https://raw.githubusercontent.com/TerrificTable/Roblox-Account-Gen/main/VERSION").text
        return version
    except Exception as e:
        return 'error'


def update():
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    os.system(
        "title Roblox Account Gen   ^|    Updating    ^|   Made by TerrificTable55™#5297")
    try:
        new_version = requests.get(
            "https://github.com/TerrificTable/Roblox-Account-Gen/archive/refs/heads/main.zip")
        with open("Roblox-Account-Gen-main.zip", 'wb')as zipfile:
            zipfile.write(new_version.content)
        with ZipFile("Roblox-Account-Gen-main.zip", 'r') as filezip:
            filezip.extractall()
        os.remove("Roblox-Account-Gen-main.zip")
        cwd = os.getcwd()+'\\Roblox-Account-Gen-main'
        shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
        shutil.rmtree(cwd)
        os.system(
            "title Roblox Account Gen   ^|    Finished Updating    ^|   Made by TerrificTable55™#5297")
        time.sleep(1)
        os.startfile("run.bat")
        exit()
    except Exception as err:
        os.system("cls;clear")
        time.sleep(7)


def updateChecker(local, offical):
    if str(local) == str(offical):
        return
    elif str(local) < str(offical):
        update()


def updateMain(localVer):
    updateChecker(localVer, github_version())
