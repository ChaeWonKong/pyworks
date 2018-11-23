from selenium import webdriver
import json
import time

with open("./secretkeys.json") as f:
    data = json.load(f)

ID = data["id"]
PASSWORD = data["password"]

try:
    driver = webdriver.Chrome("../../chromedriver")
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys(ID)
    driver.find_element_by_name("password").send_keys(PASSWORD)
    time.sleep(1)
    driver.find_elements_by_class_name("L3NKy")[0].click()
    time.sleep(2)
    driver.get("https://www.instagram.com/hacking_deal/")
    time.sleep(2)
    # Get Followers
    driver.find_element_by_partial_link_text("팔로워").click()
    time.sleep(3)
    followers_sel = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div/li/div/div/div/div/div/a")
    followers = [f.text for f in followers_sel]

    # Go back to Personal page
    driver.get("https://www.instagram.com/hacking_deal/")
    time.sleep(3)

    # Get Followings
    driver.find_element_by_partial_link_text("팔로우").click()
    time.sleep(3)
    followings_sel = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div/li/div/div/div/div/div/a")
    followings = [f.text for f in followings_sel]

    for person in followings:
        if person not in followers:
            print(person)
            break
        else:
            print("Okay")

except:
    print("Failed!")
else:
    print("Success!")

    #<a class="FPmhX notranslate _0imsa " title="leonkkkkk" href="/leonkkkkk/">leonkkkkk</a>
    #<a class="FPmhX notranslate _0imsa " title="ah___young_b" href="/ah___young_b/">ah___young_b</a>
    # /html/body/div[3]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/a
    # /html/body/div[3]/div/div/div[2]/ul/div/li/div/div/div/div/div/a
    # /html/body/div[3]/div/div/div[2]/ul/div/li/div/div[2]/div[1]/div/div/a
