import numpy as np
import time
import openai

while True:
    # 20から150までの乱数を生成（150を含む）
    num = np.random.randint(20, 151)
    print("生成された乱数:", num)

    # 乱数が80～90の範囲内の場合、反応する
    if 80 <= num <= 90:
        print("反応！")
    else:
        # AIに科学者の名言を聞いて表示
        quote = get_scientist_quote()
        print("AIからの名言:", quote)
   
    time.sleep(1)
