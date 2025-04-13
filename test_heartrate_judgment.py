import numpy as np
import time
import openai

    ser = serial.Serial('com4', 9600)  # ポート名とボーレートを環境に合わせる
    data = []

    while len(data) < 15:
        line = ser.readline().decode('utf-8').strip()
        data.append(line)

    ser.close()  # シリアルポートを閉じる
    
    try:
        sensor_data = float(data[14])  # 15行目のデータを取得
    except ValueError:
        sensor_data = None  # 数値変換に失敗した場合は None を返す
    
    return sensor_data
　　judebox=str(0)


while True:
　　num=sensor_data
    if 75 <= num <= 85:
    judebox=集中
        break
    elif num <75:
    judebox=not集中
        break
    elif  num >85 :
    judebox=super集中
    break

if judebox==集中:
    #AIの返答をだす
    if sukinakoto==??
 elif judebox==not集中:
         #AIの返答をだす
    if sukinakoto==??
 elif judebox==super集中:
         #AIの返答をだす
    if sukinakoto==??
 
    time.sleep(1)
