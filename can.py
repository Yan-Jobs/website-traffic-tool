from playwright.sync_api import sync_playwright
import time
import random

def wvisit(wurl, vamount, delay):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for i in range(vamount):
            try:
                page.goto(wurl)
                time.sleep(delay)
                print(f"[+] Success! {i+1}")
            except Exception as e:
                print(f"[-] {i+1}. visit Error: {e}")
            time.sleep(random.randint(1, delay))

        browser.close()
        
wurl = input("URL: ")
vamount = int(input("Amount: "))
delay = int(input("Delay: "))
wvisit(wurl, vamount, delay)