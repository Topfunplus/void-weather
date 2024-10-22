import speech_recognition as sr
from nameReader import listenerCode

# 创建recognizer和microphone实例
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# 从文件导入音频
with sr.AudioFile('C:\\Users\\大帅比的电脑\\OneDrive\\桌面\\pythonProject\\src\\static\\test.wav') as source:
    audio = recognizer.record(source)
    
# 识别音频
try:
    text = recognizer.recognize_google(audio, language='zh-CN')
    print(f"The audio transcript is: {text}")
    # 监听
    listenerCode(text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Service error; {e}")


