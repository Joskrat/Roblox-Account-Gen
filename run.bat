@echo off
title Installing Requirements
python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks psutil bs4 tqdm
python main.py
pause