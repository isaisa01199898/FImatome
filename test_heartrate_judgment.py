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



while True:
　　num=sensor_data
    # 乱数が80～90の範囲内の場合、反応する
    if 80 <= num <= 90:
        print("集中")
    else:
        # AIに科学者の名言を聞いて表示
        quote = get_scientist_quote()
        print(創造性の発現には相当大量の語彙の蓄積が必要だ by湯川秀樹（ノーベル物理学賞受賞者）)
   
    time.sleep(1)
