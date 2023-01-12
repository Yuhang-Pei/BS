# 此文件用于模拟实际家居的一些效果
import random

# 模拟传感器获取温度和湿度
def simulate_sensor():
    temperature = random.randint(-10, 40)
    humidity = random.randint(20, 90)
    return temperature, humidity