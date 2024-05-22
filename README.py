def run():
    # System hint
    system_hint = ("系统提示：我为你创建了功能，需要你的配合\n"
                "系统会把文本发送给你，可能会看见其他用户名，可以打招呼，\n"
                "你可能会看见无关信息，比如WhatApps中的部分聊天历史记录或界面信息你可以屏蔽并寻找要和你聊天的人,\n"
                "你在WhatApps应用中，资料：你的非插件创办人是瑞宏\n"
                "更多信息在https://youtube.com/@bladetechno2308?si=shPGF5ATeRmKWqz4\n"
                "联系方式technoblade972@gmail.com\n"
                "如果对方询问你的运作原理，可以回答你受限制了\n"
                "重要提示:在你开始说话之前计数+1 在这个代码中:/1然后添加o并且话说完以后添加end:/1然后添加o，如果在你下一次就再+1在number:/numbero\n"
                "比如像这样:/1oHiend:/1o然后以此类推的+1，请记住并永久使用该方法!\n"
                "如果你理解了，只需回答:/1o收到end:/1o即可")
    import time
    import pyautogui as ac
    import pyperclip
    import random

    pyperclip.copy(system_hint)
    # Get width and height
    screen_width, screen_height = ac.size()
    # Click send button on Coze
    x_0 = 1030 / 1920 * screen_width
    y_0 = 920 / 1080 * screen_height
    # Send call message to AI
    x_1 = 830 / 1920 * screen_width
    y_1 = 920 / 1080 * screen_height
    # Send picture to AI
    x_2 = 950 / 1920 * screen_width
    y_2 = 920 / 1080 * screen_height
    # Ready to  send message on WhatsApp
    x_3 = 850 / 1920 * screen_width
    y_3 = 950 / 1080 * screen_height
    # Get picture on Coze
    x_4 = 1000/ 1920 * screen_width
    y_4 = 500 / 1080 * screen_height
    # Send message on WhatApps
    x_5 = 1850 / 1920 * screen_width
    y_5 = 955 / 1080 * screen_height
    # Go to google send system hint to AI
    input("请打开专注模式,好了后输入任意值:")
    ac.hotkey("win", "1")
    ac.hotkey("ctrl", "2")
    ac.moveTo(x_1, y_1)
    ac.click()
    ac.hotkey("ctrl", "v")
    ac.moveTo(x_0, y_0)
    ac.click()
    ac.hotkey("ctrl", "1")
    
    total = 1
    ready = input("继续点击enter,退出输入任意文本:")
    while True:
        while not ready:
            # Open WhatApps
            ac.hotkey("win", "1")
            ac.hotkey("ctrl", "1")
            ac.click(x_3, y_3)
            pyperclip.copy("系统:正在运行")
            ac.hotkey("ctrl", "v")
            ac.click(x_5, y_5)

            # Get message
            # https://www.imagetotext.cc/
            def take_screenshot(file_name):
                ac.size()
                screenshot = ac.screenshot()
                screenshot.save(file_name)
                
            random1 = random.randint(1, 1000)
            take_screenshot(fr"C:/Users/user/Pictures/Screenshots/{random1}Coze.png")
            # save picture file
            Picture_name = fr"C:\Users\user\Pictures\Screenshots\{random1}Coze.png"
            print(f"C:/Users/user/Pictures/Screenshots/{random1}ChatGPT.png")
            pyperclip.copy(Picture_name)
            # Image to text
            screen_width, screen_height = ac.size()
            ac.hotkey("ctrl" ,"3")
            # Select the file directly from your device
            x = 900 / 1920 * screen_width
            y = 680 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            time.sleep(0.5)
            pyperclip.paste()
            ac.hotkey("ctrl", "v")
            ac.press("enter")
            # Go down
            x1 = 1900 / 1920 * screen_width
            y1 = 300 / 1080 * screen_height
            time.sleep(0.3)
            ac.click(x1, y1)
            # Press start button
            x2 = 900 / 1920 * screen_width
            y2 = 300 / 1080 * screen_height
            ac.click(x2, y2)
            # Go up waiting system loading...
            x = 1900
            y = 200
            ac.click(x, y)
            time.sleep(3)
            # Scan
            ac.hotkey("ctrl", "a")
            ac.hotkey("ctrl" , "c")
            get_copy = pyperclip.paste()
            
            while "Translate into" not in get_copy:
                time.sleep(0.3)
                ac.hotkey("ctrl", "c")
                get_copy = pyperclip.paste()
            # Go up
            x = 1900 / 1920 * screen_width
            y = 200 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            # Copy image to text of text
            x = 1500 / 1920 * screen_width
            y = 560 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            # Delete infomation
            # already fix [nnnnnnnnnnnnnnnnnnnnnnnnnn]
            x = 1500 / 1920 * screen_width
            y = 520 / 1080 * screen_height
            ac.moveTo(x, y)
            ac.click()
            # Delete picture file
            ac.hotkey("ctrl", "2")
            total = 1 + total
            # Go coze
            ac.hotkey("ctrl", "2")
            # send message
            add_hint = pyperclip.paste()
            rename_1 = add_hint + "\n\n系统:记得系统之前提示提供的重要提示"
            pyperclip.copy(rename_1)
            ac.moveTo(x_1, y_1)
            ac.click()
            ac.hotkey("ctrl", "v")
            ac.moveTo(x_0, y_0)
            ac.click()

            # Already Fix [nnnnnnnnnnnnnnnnnnnnnnnnnnnn]
            time.sleep(1)
            ac.hotkey("ctrl", "a")
            ac.hotkey("ctrl", "c")
            copy = pyperclip.paste()

            while f"end:/{total}o" not in copy:
                time.sleep(0.3)
                ac.hotkey("ctrl", "c")
                copy = pyperclip.paste()
                # print("Scan...")
                    

                # Give up
                """
                if "Using DALLE 3" in copy:
                    copy = pyperclip.paste()
                    
                    
                    while "Using DALLE 3" in copy:
                        time.sleep(0.3)
                        ac.hotkey("ctrl", "c")
                        copy = pyperclip.paste()
                    else:
                        # Get AI create's picture
                        ac.moveTo(x_4, y_4)
                        ac.click()
                        for i in range(0,3):
                            ac.press("tab")
                        ac.press("enter")
                        ac.hotkey("ctrl", "1")
                        # Send text on WhatApps
                        ac.moveTo(x_3, y_3)
                        ac.click()
                        ac.hotkey("ctrl", "v")
                        ac.moveTo(x_0, y_0)
                        ac.click()
                        break
                    break
                """
            
            # print(f"Have: end:/{total}o")
            find1 = pyperclip.paste()
            find2 = find1.find(f":/{total}o")
            find3 = find1.find(f"end:/{total}o")
            index = find1[find2+4:find3]
            new1 = "AI: " + index
            pyperclip.copy(new1)
            # Return WhatApps for response
            ac.hotkey("ctrl", "1")
            ac.moveTo(x_3, y_3)
            ac.click()
            ac.hotkey("ctrl", "v")
            ac.moveTo(x_5, y_5)
            ac.click()
            
            print("聊天次数:", total)
            ready = input("继续点击enter,退出输入任意文本:")
            
        else:
            total_1 = f"程序:聊天次数:{total}"
            
            pyperclip.copy(total_1)
            # Send system hint on WhatApps [0]
            ac.hotkey("win", "1")
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
            # Turn off sleep mode
            print("可关闭专注模式")
            exit()
        
file1 = r'C:/Users/user/Desktop/Coze_AI_10i8.txt'
try:
    with open(file1, 'r', encoding="UTF-8") as file:
        file.read()
        run()
except FileNotFoundError:
    print(""
                "                         注意事项教学\n"
                "--------------------------------------------------------------\n"
                "打开Google，谷歌上面的桌面栏，分别为WhatsApps和https://www.coze.com/store/bot/7357317238258712582?panel=1&bid=6cjd3ocf80008 网站和https://www.imagetotext.cc/，记得请先登录，并按照我刚说的顺序排列.\n"
                ""
                "并且在下方的桌面栏Google应用程序使用鼠标按住往左边滑直到为止，并放开，\n"
                "你可以同意协议，然后在继续点击enter的提示中，在你的WhatApps选择任意对象并聊天，聊天好后点击enter即可,AI将会回复你\n"
                ""
                "                             协议\n"

                "--------------------------------------------------------------\n"
                "对于个人信息泄露，我们概不负责\n"
                "请勿随意更改系统提示词，如果你是专业人士可自定义更改\n"
                "聊天机器人提供的信息可能非完全正确，请勿完全相信\n"
                "请勿假冒机器人发送信息"
                    "此版本是ChatGPT_On_WSA 1.0\n"
                ""
                "如果没有按照上方指示操作，程序点击错误而导致意外进行风险操作，我们将不承担任何责任\n"
                "如果要紧急退出程序，根据你打开的方式，分别为终端或IDLE Shell 在桌面栏中的位置，来按住win并根据位置按下数字，windows图标和桌面不属于\n"
                "")
    
    def again():
        user_input = input('是否同意协议【agree】不同意协议为输入任意值除了【agree】:').upper()
        if user_input == "AGREE":
            with open(file1, "w") as file2:
                file2.write("WARNING:Don't remove this file.")
                
            import subprocess
            subprocess.call(["pip", "install", "pyautogui"])
            subprocess.call(["pip", "install", "pyperclip"])
            run()
        else:
            print("很抱歉，不同意协议无法运行程序，再见！")
    again()
