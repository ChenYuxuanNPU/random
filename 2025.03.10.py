import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 1. 从剪贴板获取内容
text_to_input = pyperclip.paste()  # 获取剪贴板内容
if not text_to_input:
    print("剪贴板为空，请先复制内容！")
    exit()

# 2. 设置 Edge 浏览器驱动
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))  # 自动下载并安装 Edge 驱动
driver.maximize_window()  # 最大化窗口

# 3. 打开 DeepSeek 网页
driver.get("https://chat.deepseek.com/")  # 替换为 DeepSeek 的实际网址
time.sleep(1)  # 等待页面加载

# 移动鼠标到指定位置
pyautogui.moveTo(960, 780, duration=0.1)  # duration参数是可选的，表示移动到该位置所需的时间（秒）
pyautogui.click()

pyautogui.moveTo(960, 620, duration=0.1)  # duration参数是可选的，表示移动到该位置所需的时间（秒）
time.sleep(1)
pyautogui.click()

pyautogui.moveTo(920, 620, duration=0.1)  # duration参数是可选的，表示移动到该位置所需的时间（秒）
time.sleep(1)
pyautogui.click()
time.sleep(3)

# 4. 找到输入框并粘贴内容
try:
    # 假设输入框的 HTML 元素可以通过以下方式定位
    input_box = driver.find_element(By.TAG_NAME, "textarea")  # 根据实际网页结构调整
    input_box.send_keys(f'以下是我区教师队伍建设情况，请根据下述数据编写五千字左右的教师队伍数据分析报告：{text_to_input}')  # 将剪贴板内容粘贴到输入框
    time.sleep(0.5)

    # 5. 执行提问（模拟按下回车键）
    input_box.send_keys(Keys.RETURN)
    time.sleep(3000)  # 等待结果加载

except Exception as e:
    print(f"操作失败: {e}")
