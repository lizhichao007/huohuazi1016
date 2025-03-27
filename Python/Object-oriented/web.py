import webbrowser

try:
    # 打开Google的主页
    webbrowser.open('https://w3.huawei.com/next/indexa.html?locale=cn')
except Exception as e:
    print(f"发生错误：{e}")