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

except:
    print("Failed!")
else:
    print("Success! Printed All lists")

    #<a class="FPmhX notranslate _0imsa " title="leonkkkkk" href="/leonkkkkk/">leonkkkkk</a>
    #<a class="FPmhX notranslate _0imsa " title="ah___young_b" href="/ah___young_b/">ah___young_b</a>
    # /html/body/div[3]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/a
    # /html/body/div[3]/div/div/div[2]/ul/div/li/div/div/div/div/div/a
    # /html/body/div[3]/div/div/div[2]/ul/div/li/div/div[2]/div[1]/div/div/a

# 인스타 팔로워 수/팔로잉 수 많을 경우 제대로 프린트 안 되는 문제!
# 스크롤 해야만 더 볼 수 있기 때문으로 확인.
# 셀레니움으로 스크롤하면서 긁어올 수 있는 방법 확인해야 함.
