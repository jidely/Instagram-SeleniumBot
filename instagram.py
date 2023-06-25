from instagramUserInfo import username ,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def sigIn(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(1)
        self.browser.maximize_window()
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        
    def getFollowers(self):
        self.browser.get(f'https://www.instagram.com/{self.username}/followers/')
        time.sleep(5)

        Instagram.scrollDown(self)
        
        dialog = self.browser.find_element(By.CSS_SELECTOR, 'div[role=dialog]')
        followers = dialog.find_elements(By.CSS_SELECTOR, 'div[aria-labelledby]')
        
        followersList = []
        sayi = 0
        for users in followers:
            link = users.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            followersList.append(link)
            sayi += 1
            print(f'{sayi}- {link}')         

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followersList:
                file.write(item+"\n")

    def getFollowing(self):
        self.browser.get(f'https://www.instagram.com/{self.username}/following/')
        time.sleep(5)

        Instagram.scrollDown(self)

        dialog = self.browser.find_element(By.CSS_SELECTOR, 'div[role=dialog]')
        following = dialog.find_elements(By.CSS_SELECTOR, 'div[aria-labelledby]')
        
        followingList = []
        sayi = 0
        for users in following:
            link = users.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            followingList.append(link)
            sayi += 1
            print(f'{sayi}- {link}')  
        
        with open("following.txt","w",encoding="UTF-8") as file:
            for item in followingList:
                file.write(item+"\n")

    


    def scrollDown(self):
        jsKomut = """
        sayfa = document.querySelector('._aano');
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            time.sleep(2)
            sayfaSonu = self.browser.execute_script(jsKomut)
            if son == sayfaSonu:
                break

        


        

instagram = Instagram(username,password)
instagram.sigIn()
instagram.getFollowers()
instagram.getFollowing()

