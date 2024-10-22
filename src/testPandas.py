# 寻找两个字符串的公共最长子序列字符串
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # 创建一个二维数组来存储最长公共子序列的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填充dp表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 回溯获取最长公共子序列
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # 将最长公共子序列逆序输出
    lcs.reverse()
    return ''.join(lcs)

    
def display_weather(data):
    # 找到并解析必要的信息
    city = data.split('"city":"')[1].split('"')[0]
    adcode = data.split('"adcode":"')[1].split('"')[0]
    province = data.split('"province":"')[1].split('"')[0]
    reporttime = data.split('"reporttime":"')[1].split('"')[0]
    
    # 获取天气预报
    casts = data.split('"casts":')[1].split('}]')[0].replace('},', '},\n')

    print(f"城市: {city} (编码: {adcode})")
    print(f"省份: {province}")
    print(f"报告时间: {reporttime}")
    print("\n天气预报:\n")

    # 分割每一天的天气数据
    for cast in casts.split('},'):
        date = cast.split('"date":"')[1].split('"')[0]
        week = cast.split('"week":"')[1].split('"')[0]
        dayweather = cast.split('"dayweather":"')[1].split('"')[0]
        nightweather = cast.split('"nightweather":"')[1].split('"')[0]
        daytemp = cast.split('"daytemp":"')[1].split('"')[0]
        nighttemp = cast.split('"nighttemp":"')[1].split('"')[0]
        daywind = cast.split('"daywind":"')[1].split('"')[0]
        nightwind = cast.split('"nightwind":"')[1].split('"')[0]
        
        print(f"日期: {date} (周{week})")
        print(f"白天气温: {daytemp}°C, 天气: {dayweather}, 风向: {daywind}")
        print(f"夜间气温: {nighttemp}°C, 天气: {nightweather}, 风向: {nightwind}")
        print("-" * 40)

