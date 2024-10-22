import pandas as pd
from testPandas import longest_common_subsequence,display_weather
import requests

API_KEY = '507ead166bf9507db185c471386de791'

PATH = 'C:\\Users\\大帅比的电脑\\OneDrive\桌面\\pythonProject\\src\\AMap_adcode_citycode\\AMap_adcode_citycode.xlsx'


def listenerCode(text):
  df = pd.read_excel(PATH)
  text = str(text)
  
  goal = ''
  for item in range(1,len(df)):
    # 寻找两个字符串的公共部分 拿到公共部分 然后去模糊搜索
    common = longest_common_subsequence(str(df.loc[item]['中文名']),text)
    if len(common) >= 2:
      goal = common
      
  if len(goal) > 0:
    code = df[df['中文名'].str.contains(goal)]['adcode'].iloc[0]
    URL = f'https://restapi.amap.com/v3/weather/weatherInfo?city={int(code)}&key={API_KEY}&extensions=all'
    response = requests.get(URL)
    display_weather(response.text)
    return response 
  
  else:
    return Exception('未找到相关信息')
  