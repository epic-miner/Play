__all__ = []
import asyncio
from playwright.async_api import async_playwright
import nest_asyncio
import random
import sys
from faker import Faker
import requests as re

O0OO000OOO0OO0O00 = "https://UmanSheikh.github.io/portfolio/static/allow2.txt"
O00O0O0OO0OOO0OO0 = re.get(O0OO000OOO0OO0O00).text.strip()
nest_asyncio.apply()

O0O0O00O0O000OO0O = True

async def OOO0000OO00000OOO(OO000O0O00OOOOOO0, O00O0OO00OOOO0O0O, OOO00000O00OOOOOO, OO0000OO000000O0O, O0O0O00OO000OOOOO):
    print(f"{OO000O0O00OOOOOO0} started!")
    async with async_playwright() as OOOO00O000OOOOOO0:
        O0OO00O0O00OO0000 = await OOOO00O000OOOOOO0.chromium.launch(headless=True, args=['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'])
        OOOOO0O00O0OOOO00 = await O0OO00O0O00OO0000.new_context(permissions=['microphone'])
        OOO0OO0O0OOOO000O = await OOOOO0O00O0OOOO00.new_page()
        await OOO0OO0O0OOOO000O.goto(f'http://www.zoom.us/wc/join/{OO0000OO000000O0O}', timeout=200000)
        try:
            await OOO0OO0O0OOOO000O.click('//button[@id="onetrust-accept-btn-handler"]', timeout=5000)
        except Exception as O0O00OO0000O0OO00:
            pass
        try:
            await OOO0OO0O0OOOO000O.click('//button[@id="wc_agree1"]', timeout=5000)
        except Exception as O0O00OO0000O0OO00:
            pass
        try:
            await OOO0OO0O0OOOO000O.wait_for_selector('input[type="text"]', timeout=200000)
            await OOO0OO0O0OOOO000O.fill('input[type="text"]', O00O0OO00OOOO0O0O)
            await OOO0OO0O0OOOO000O.fill('input[type="password"]', O0O0O00OO000OOOOO)
            O00O0OO00O00000O0 = await OOO0OO0O0OOOO000O.wait_for_selector('button.preview-join-button', timeout=200000)
            await O00O0OO00O00000O0.click()
            await OOO0OO0O0OOOO000O.wait_for_selector('button#preview-audio-control-button', timeout=200000)
            await OOO0OO0O0OOOO000O.click('button#preview-audio-control-button')
            await OOO0OO0O0OOOO000O.wait_for_selector('button#join-audio-by-computer', timeout=200000)
            await OOO0OO0O0OOOO000O.click('button#join-audio-by-computer')
        except Exception as O0O00OO0000O0OO00:
            pass
        try:
            OO0O0OOO0OO00O000 = await OOO0OO0O0OOOO000O.wait_for_selector('//button[text()="Join Audio by Computer"]', timeout=350000)
            await OO0O0OOO0OO00O000.click()
            await OOO0OO0O0OOOO000O.wait_for_selector('//button[text()="Join with Computer Audio"]', timeout=350000)
            await OOO0OO0O0OOOO000O.click('//button[text()="Join with Computer Audio"]')
            await OOO0OO0O0OOOO000O.evaluate('() => { navigator.mediaDevices.getUserMedia({ audio: true }); }')
            print(f"{OO000O0O00OOOOOO0} mic aayenge.")
        except Exception as O0O00OO0000O0OO00:
            print(f"{OO000O0O00OOOOOO0} mic nahe aayenge. ", O0O00OO0000O0OO00)
        print(f"{OO000O0O00OOOOOO0} sleep for {OOO00000O00OOOOOO} seconds ...")
        while O0O0O00O0O000OO0O and OOO00000O00OOOOOO > 0:
            await asyncio.sleep(1)
            OOO00000O00OOOOOO -= 1
        print(f"{OO000O0O00OOOOOO0} ended!")
        await O0OO00O0O00OO0000.close()

async def OO0OO00OOOOOOOOOO(OO000OO0OOO000OOO, O0O0000OOOOOO00OO, O0OOO00OOOO0O0O0O):
    global O0O0O00O0O000OO0O
    O000O00O0OO000OOO = 90
    OO0O0O0000OOO0OO0 = O000O00O0OO000OOO * 60
    OOO0O0O00OO0O0O00 = []
    for O00000OO000OOO00O in range(OO000OO0OOO000OOO):
        try:
            O000O0OOOO000O000 = Faker(('en_IN')).name()
        except IndexError:
            break
        OO0O0000O00O00OOO = OOO0000OO00000OOO(f'[Thread{O00000OO000OOO00O}]', O000O0OOOO000O000, OO0O0O0000OOO0OO0, O0O0000OOOOOO00OO, O0OOO00OOOO0O0O0O)
        OOO0O0O00OO0O0O00.append(OO0O0000O00O00OOO)
    try:
        await asyncio.gather(*OOO0O0O00OO0O0O00)
    except KeyboardInterrupt:
        O0O0O00O0O000OO0O = False
        await asyncio.gather(*OOO0O0O00OO0O0O00, return_exceptions=True)

if __name__ == '__main__':
    try:
        if O00O0O0OO0OOO0OO0 == "true":
            OOO00OOO0000O0O0O = int(sys.argv[1])
            OOOO00O00O00OO0OO = sys.argv[2]
            OOO
