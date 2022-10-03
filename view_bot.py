from selenium import webdriver
import time
import random

randomOne = random.randint(1, 5)
postList = "postList.txt"
viewFileCount = "viewCount.txt"
postFile = open(postList)
ListPost = postFile.readlines()

NUMBER_OF_TAB = int(input("Mời bạn nhập số tab muốn bật:"))
NUMBER_OF_URL = len(ListPost)
LOOP_TIME = int(input("Bao lâu thì chạy vòng lặp này một lần(nhập số giây):"))

# bằng 1 thì bật, 0 là tắt
ModeList = int(input("Có muốn chạy tự động click vào các bài bên dưới ko(bằng 1 thì bật, 0 là tắt):"))

postIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0

# browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser = webdriver.Firefox(executable_path='./geckodriver.exe')

# => tabIndex = 0
browser.get(ListPost[postIndex])


# Hành động của một người đọc bài
# lăn xuống
# random toạ độ từ 982 đến 13500
# chạy liên tục đồng thời random thời gian từ 1s đến 5s
def my_Actor():
    time.sleep(randomOne)
    for num in range(1, randomOne):
        browser.execute_script("window.scrollTo(0, Math.floor(Math.random() * 13500) + 982)");
        time.sleep(randomOne)
        browser.execute_script("console.log('test ne')")
    browser.execute_script("console.log('end')")


my_Actor()

while True:
    postIndex = (postIndex + 1) % NUMBER_OF_URL
    tabIndex = (tabIndex + 1) % NUMBER_OF_TAB
    if tabCount < NUMBER_OF_TAB:
        tabCount = tabCount + 1
        browser.execute_script("window.open('" + ListPost[postIndex].strip() + "')")
        my_Actor()
    else:
        handle = browser.window_handles[tabIndex]
        browser.switch_to.window(handle)
        time.sleep(0.5)
        if ModeList == 0:
            browser.get(ListPost[postIndex])
            my_Actor()
        else:
            time.sleep(randomOne)
            browser.execute_script("window.scrollTo(0, Math.floor(Math.random() * 8334) + 7806)");
            randomClick = str(random.randint(0, 2))
            time.sleep(randomOne)
            print(randomClick)
            browser.execute_script("document.querySelectorAll('.rp-item-title')[" + randomClick + "].click()")
            my_Actor()

    viewCount = viewCount + 1
    saveFile = open(viewFileCount, 'w')
    saveFile.write(str(viewCount))
    saveFile.close()

    time.sleep(LOOP_TIME)
