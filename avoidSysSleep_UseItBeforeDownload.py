import os

os.system("powercfg -change -standby-timeout-ac 0")
os.system("powercfg -change -standby-timeout-dc 0")

print("睡眠已关闭")

os.system("powercfg -change -standby-timeout-ac 20")
os.system("powercfg -change -standby-timeout-ac 20")
# 恢复电脑睡眠设置