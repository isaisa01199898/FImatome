
liking = None
judebox = None
message = None
liking=input("あなたが好きなものは、1四字熟語、2格言、3科学、4、歴史1〜4で記入")
print(f"user_liking:{liking}")
if liking == 1:
        liking_mes=四字熟語
elif liking == 2:
　　　　　liking_mes=格言
elif liking == 3:
　　　　　liking_mes=科学史に名が残った科学者の名言
elif liking == 4:
　　　　　liking_mes=歴史の偉人の名言
        
#get heartrate for sensor
if sensor_data is not None:
   if 75 <= sensor_data <= 85:
        judebox = "集中"
   elif sensor_data < 75:
        judebox = "not集中"
   elif sensor_data > 85
        judebox = "super集中"
   else:
        print("データ未取得")  
if judebox =="集中":
        prompt=f'この人は、{liking}が好きです。勉強に集中できている人が継続的に集中できるような{liking_mes}を一つだけ教えてください。'
        elif judebox =="not集中":
                prompt=f'この人は、{liking}が好きです。勉強に集中できない人を励ます{liking_mes}を一つだけ教えてください。'
        elif judebox =="super集中":
      　　　　   prompt=f'この人は、{liking}が好きです。勉強に集中できている人が継続的に集中できるような{liking_mes}を一つだけ教えてください。'
try:
                client = Groq(api_key=GROQ_API_KEY)
                chat_history = [
                    {"role": "system", "content": "あなたは便利なアシスタントです。何事にも優しく、正確な情報でお答えください"},
                    {"role": "user", "content": prompt}
                ]
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=chat_history,
                    max_tokens=50,
                    temperature=1.2
                )
                message = response.choices[0].message.content
            except Exception as e:
                message = f"モデルの呼び出しに失敗しました: {e}"
        print(f"{message}")
        # Prepare context for rendering
        context = {
            'now_time': datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y年%m月%d日 %H:%M:%S"),
            'ser_data': ser_data,
            'form': TestForm(),
            'insert_forms': '初期値',
            'message': message,
        }
        return render(request, self.template_name, context)



