def run():

    system_hint = """
系统提示：你需要扮演在WhatsApp平台与人聊天角色以及遵守系统告诉你的东西
系统会把文本发送给你，可能会看见其他用户名，可以打招呼，
你可能会看见无关信息，比如WhatApps中的部分聊天历史记录或界面信息你可以屏蔽并寻找要和你聊天的人,'
但要非常注意文本中会有系统提示，为了不让你犯错
你在WhatApps应用中，资料：非插件创办人是technoblade972@gmail.com也是联系方式
如果对方询问你的运作原理，可以回答你受限制了
如果你理解了上述，只需回答 ":/1o收到e:/1o" 即可
"""

    README1 = """
                               教学
------------------------------------------------------------------------
1)系统会自动打开三个网页，请让他们排在最前面，但是三个网页必须是按照当前顺序来放置最前面。
把目前开着的Google应用程序放在桌面第一位置（电脑桌面）。

2)在WhatApps和ChatGPT网页中记得提前登录。

3)系统控制期间请不要尝试移动或控制除非紧急情况，请在桌面寻找终端，同时按下ctrl + c退出程序执行。

4)请不要全屏应用程序（请你右上角的中间按钮以全屏）途中必须以这样形式

如果有任何问题请反馈给technob972@gmail.com并附加版本ChatGPT_WSA 1.0。
"""

    import time
    import pyautogui as ac
    import pyperclip
    import random
    import webbrowser
    URL1 = "https://web.whatsapp.com/"
    URL2 = "https://chatgpt.com/"
    URL3 = "https://www.imagetotext.cc/"
    def web():
        webbrowser.open(URL1)
        webbrowser.open(URL2)
        webbrowser.open(URL3)
    web() # For developer
    print(README1)
    if input("打开专注模式,准备就绪后点击enter/要退出输入任意文:"):
        exit()
    # Get width and height
    screen_width, screen_height = ac.size()
    # Ready message on WhatsApp / ChatGPT
    x_3 = 850 / 1920 * screen_width
    y_3 = 950 / 1080 * screen_height
    # Get picture on Coze
    x_4 = 1000/ 1920 * screen_width
    y_4 = 500 / 1080 * screen_height
    # Send message on WhatApps
    x_5 = 1850 / 1920 * screen_width
    y_5 = 955 / 1080 * screen_height
    # Go to google send system hint to AI
    pyperclip.copy(system_hint)
    ac.hotkey("win", "1")
    ac.hotkey("ctrl", "2")
    ac.click(x_3, y_3)
    ac.hotkey("ctrl", "v")
    ac.press("enter")
    ac.hotkey("ctrl", "1")
    ready = input("允许AI接收点击enter/要退出输入任意文本:")
    ac.hotkey("win", "1")
    total = 1
    while True:
        while not ready:
            # Open WhatApps
            ac.hotkey("ctrl", "1")
            ac.click(x_3, y_3)
            pyperclip.copy("系统:正在运行")
            ac.hotkey("ctrl", "v")
            ac.click(x_5, y_5)

            # Get message (image to text)
            def take_screenshot(file_name):
                ac.size()
                screenshot = ac.screenshot()
                screenshot.save(file_name)
                
            random1 = random.randint(1, 1000)
            take_screenshot(fr"C:/Users/user/Pictures/Screenshots/{random1}ChatGPT.png")
            # save picture file
            Picture_name = fr"C:\Users\user\Pictures\Screenshots\{random1}ChatGPT.png"
            pyperclip.copy(Picture_name)
            print(f"C:/Users/user/Pictures/Screenshots/{random1}ChatGPT.png")
            # Image to text
            screen_width, screen_height = ac.size()
            ac.hotkey("ctrl" ,"3")
            # Select the file directly from your device
            x = 900 / 1920 * screen_width
            y = 700 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            time.sleep(1)
            l = pyperclip.copy(Picture_name)
            #print(l)
            ac.hotkey("ctrl", "v")
            ac.press("enter")
            # Press sumbit button
            ac.click(800 / 1920 * screen_width, 770 / 1080 * screen_height)
            # Scan
            ac.hotkey("ctrl", "a")
            ac.hotkey("ctrl" , "c")
            get_copy = pyperclip.paste()
            
            while "Translate into" not in get_copy:
                time.sleep(0.3)
                ac.hotkey("ctrl", "c")
                get_copy = pyperclip.paste()

            # Copy image to text's text
            ac.click(1000 / 1920 * screen_width, 700 / 1080 * screen_height)
            ac.hotkey("ctrl", "a")
            ac.hotkey("ctrl", "c")
            # Notice?
            # Delete infomation
            x = 1500 / 1920 * screen_width
            y = 560 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            ac.hotkey("ctrl", "2")
            total = 1 + total
            # Go to ChatGPT
            ac.hotkey("ctrl", "2")
            # Send message
            add_hint = pyperclip.paste()
            rename_1 = add_hint + f'\n\n系统:在你开始说话前请写入这个代码 :/{total} 然后添加o,然后回复用户,说完后请写e:/{total}并写上o即可'
            pyperclip.copy(rename_1)
            ac.click(x_3, y_3)
            ac.hotkey("ctrl", "v")
            ac.press("enter")

            # Notice?
            time.sleep(1)
            x1 = 500 / 1920 * screen_width
            y1 = 500 / 1080 * screen_height
            ac.click(x1, y1)
            ac.hotkey("ctrl", "a")
            ac.hotkey("ctrl", "c")
            copy = pyperclip.paste()

            while f"e:/{total}o" not in copy:
                time.sleep(0.3)
                ac.hotkey("ctrl", "a")
                ac.hotkey("ctrl", "c")
                copy = pyperclip.paste()

            find1 = pyperclip.paste()
            find2 = find1.find(f":/{total}o")
            find3 = find1.find(f"e:/{total}o")
            index = find1[find2+4:find3]
            new1 = "ChatGPT: " + index
            pyperclip.copy(new1)
            # Return WhatApps for response
            ac.hotkey("ctrl", "1")
            ac.moveTo(x_3, y_3)
            ac.click()
            ac.hotkey("ctrl", "v")
            ac.moveTo(x_5, y_5)
            ac.click()
            
            print("聊天次数:", total)
            ready = input("允许AI接收点击enter/要退出输入任意文本:")
            ac.hotkey("win", "1")
            
        else:
            total_1 = f"程序:聊天次数:{total}"
            pyperclip.copy(total_1)
            # Send system hint on WhatApps [0]
            ac.hotkey("ctrl", "1")
            ac.click(x_3, y_3)
            ac.hotkey("ctrl", "v")
            ac.click(x_5, y_5)
            # Send system hint on WhatApps [1]
            system = "程序:程序已退出（他人已退出程序)"
            pyperclip.copy(system)
            ac.click(x_3, y_3)
            ac.hotkey("ctrl", "v")
            time.sleep(0.1)
            ac.click(x_5, y_5)
            print("可关闭专注模式")
            exit()
        
file1 = r'C:/Users/user/Desktop/Coze_AI_10i8.txt'
try:
    with open(file1, 'r', encoding="UTF-8") as file:
        file.read()
        run()
except FileNotFoundError:
    README = """
                                协议
---------------------------------------------------------------------------
1)对于个人信息泄露我们概不负责。
2)请勿随意更改系统提示词，连我都要调试超久。
3)请勿使用非法用途。
4)如果没有按照接下来的指示操作，程序点击错误而导致意外进行风险操作，我们将不承担任何责任。
"""

    print(README)
    def again():
        user_input = input('是否同意协议【agree】不同意协议为输入任意值除了【agree】:').upper()
        if user_input == "AGREE":
            with open(file1, "w") as file2:
                file2.write("WARNING:Don't remove to file.")
                
            import subprocess
            subprocess.call(["pip", "install", "pyautogui"])
            subprocess.call(["pip", "install", "pyperclip"])
            run()
        else:
            print("很抱歉，不同意协议无法运行程序，再见！")
    again()
