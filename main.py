import random
import requests
import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool
import time
from selenium.webdriver.common.by import By
from mailtm import Email
from password import password_list
import re


class Selenium:
    def __init__(self, mnemonic, profile_name) -> None:
        split = re.split('@', mnemonic)
        self.mnemonicc = split[0]
        self.proxyy = f"--proxy-server={split[-1]}"
        self.profile_name = str(profile_name)
        pass

    def start_driver(self, mnemonic, profile_name):
        # time.sleep(random.randint(1,10))
        options = uc.ChromeOptions()
        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun')
        options.add_argument('--password-store=basic')
        options.add_argument('--load-extension=C:\\myria\\BI,C:\\myria\\MM')
        if len(re.split('@', mnemonic)) > 1:
            proxy = f"--proxy-server={re.split('@', mnemonic)[1]}"
            options.add_argument(proxy)

        driver = uc.Chrome(
            options=options,
            executable_path = f'undetected_chromedriver/{str(profile_name)}.exe'
        )
        self.driver = driver
        return driver

    def send_key(self, key):
        ac = ActionChains(self.driver)
        ac.send_keys(key).perform()

    def take_seed(self, path, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            seed = self.driver.find_element(By.XPATH, path).text
            f = open('text.txt', 'a')
            f.write(f'{seed}\n')

        except Exception as e:
            print(f"No seed phase after {timeout} seconds of waiting!!!")
            self.driver.quit()

            return None
        if element is not None:
            time.sleep(delay)
            return element
        else:
            print(f"NO SUCH ELEMENT!\n Path: {path}")
        self.driver.execute_script("""document.body.style.backgroundColor = 'green'""")
        input()

    def send_text(self, path, text, timeout=20, delay=0):
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            self.driver.find_element(By.XPATH, path).send_keys(text)

        except Exception as e:
            print(f"No input after {timeout} seconds of waiting!!!\n{path}")
            return None
        if element is not None:
            time.sleep(delay)
            return element
        else:
            print(f"NO SUCH ELEMENT!\n Path: {path}")
        self.driver.execute_script("""document.body.style.backgroundColor = 'green'""")
        input()

    def take_element(self, path, timeout=20, delay=0):
        element = ""
        try:
            time.sleep(delay)
            element = WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
            self.driver.find_element(By.XPATH, path).click()

        except Exception as e:
            print(f"No element after {timeout} seconds of waiting!!!\n{path}")
            return None

    def refresh(self):
        self.driver.refresh()

    def check_element(self, path):
        element = self.driver.find_elements_by_xpath(path)
        if len(element) > 0:
            random.choice(122, 223, 334)

    def del_extra_element(self, path):
        self.driver.execute_script(f'document.querySelector("{path}").remove();')

    def send_keys_delay(element, string, delay=0):
        for character in string:
            element.send_keys(character)
            time.sleep(delay)


class Metamask(Selenium):
    def __init__(self, mnemonic, password, driver) -> None:
        split = re.split('@',mnemonic)
        self.mnemonic = split[0]
        self.proxy = f"--proxy-server={split[-1]}"
        self.password = password
        self.driver = driver

    def installMM(self, path_mm):
        while True:
            if len(self.driver.window_handles) > 1:
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.close()
                print('MM installed')
                break
            else:
                time.sleep(1)

    def create_wallet(self):
        while True:
            try:
                # time.sleep(random.randint(0, 30))
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
                break
            except Exception as e:
                self.driver.get('chrome-extension://fmjndhhjmmobaohljigkcecddiadjpia/home.html')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]')
        self.send_text('//*[@id="create-password"]', '12345678')
        self.send_text('//*[@id="confirm-password"]', '12345678')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/div[3]/div')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button', delay=5)
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div[2]')
        self.take_seed('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div')
        self.take_element('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div[2]/button[1]')
        self.take_element('//*[@id="popover-content"]/div/div/section/header/div/button')

    def go_to_site(self):
        self.driver.get(str(self.mnemonic))
        return self



class Myria(Metamask):
    def __init__(self, driver, profile_name) -> None:
        self.driver = driver
        self.profile_name = str(profile_name)

    def login(self):
        ex = 0
        print("Login")
        self.take_element('//*[@id="radix-7"]/div/div/button', timeout=60, delay=3)
        while True:
            try:
                self.take_element('//*[@id="radix-7"]/div/div/button', timeout=3)
                self.take_element('//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/button', 3)
                time.sleep(5)
                if len(self.driver.window_handles) > 1:
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]', 3)
                    self.take_element('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]', 3)
                    time.sleep(3)
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.take_element('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]', 3)
                    time.sleep(3)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                button = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div[5]/button')

                ac = ActionChains(self.driver)
                for i in range(20):
                    ac.move_to_element(button).perform()
                    time.sleep(0.1)
                    ac.click().perform()
                self.take_element('//*[@id="radix-30"]/div/div/div/div/div[1]/button', 3)
                break
            except Exception as e:
                time.sleep(10)
                ex += 1
                if ex == 3:
                    break

    def sign_up(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/a').click()
        find = 0
        test = Email()
        test.register()
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[1]/div[1]/div/div/input', 'firstname')
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[1]/div[2]/div/div/input', 'lastname')
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[2]/div[1]/div/div/input', f'{random.choice(password_list)}{random.randint(0,999)}')
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[2]/div[2]/div/div/input', str(test.address))
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[2]/div[3]/div/div/input', 'Password@12')
        self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[2]/div[4]/div/div/input', 'Password@12')
        self.send_key(u'\ue007')
        # self.take_element('//*[@id="radix-1"]/div/div[2]/form/button')
        while True:
            try:
                time.sleep(5)
                self.driver.maximize_window()
                username_input = self.driver.find_elements(By.XPATH, '//*[@id="radix-1"]/div/div[2]/form/div[2]/div[1]/div/div/input')
                if len(username_input) == 1:
                    self.driver.find_element(By.XPATH, '//*[@id="radix-1"]/div/div[2]/form/div[2]/div[1]/div/div/input').clear()
                    self.send_text('//*[@id="radix-1"]/div/div[2]/form/div[2]/div[1]/div/div/input',
                                   f'{random.choice(password_list)}{random.randint(0, 999)}', 3)
                    # self.take_element('//*[@id="radix-1"]/div/div[2]/form/button')
                    self.send_key(u'\ue007')
                else:
                    self.driver.minimize_window()
                    break
            except Exception as e:
                self.send_key(u'\ue007')
                print(' ')
        def listener(message):
            link = str(message['text'])
            print(link)
            link = (link.split('    ')[1])
            self.driver.get(link)
            time.sleep(1)
            self.driver.quit()
            test.stop()

        # Start listening
        test.start(listener, interval=1)
        print("\nWaiting for new emails...")

def make_list_from_file(file):
    with open(file, 'r') as f:
        return [x for x in f.read().split("\n") if x]


def worker(account):
    acc = 1
    while True:
        try:
            profile_name, mnemonic, password = account
            driver = ''
            while True:
                try:
                    driver_session = Selenium(mnemonic, profile_name)
                    driver = driver_session.start_driver(mnemonic, profile_name)
                    metamask = Metamask(mnemonic, password, driver)
                    while True:
                        time.sleep(1)
                        if len(driver.window_handles) > 1:
                            driver.switch_to.window(driver.window_handles[0])
                            driver.close()
                            break
                    driver.switch_to.window(driver.window_handles[0])  # switch to mm window
                    print("MetaMask was started")
                    metamask.create_wallet()
                    break
                except Exception as e:
                    print(e)
                    driver.quit()

            myria = Myria(driver, profile_name)

            metamask.go_to_site()
            myria.login()
            myria.sign_up()
            f = open(f'{profile_name}.txt', 'w')
            f.write(f'{acc}')
            f.close()
            acc += 1
        except Exception as e:
            print(e)
            driver.quit()

if __name__ == "__main__":
    mnemonics = make_list_from_file("accounts.txt")
    accounts = [(str(i + 1), mnemonics[i], "vegotchi" + str(i + 1)) for i in range(len(mnemonics))]
    p = Pool(processes=len(accounts))
    p.map(worker, accounts)
