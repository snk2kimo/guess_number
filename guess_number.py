# 產生一個隨機整數 1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了!"
# 猜錯的話，告訴他"比答案大/小"
# 加入顯示猜的次數

import random # 載入模組
# 調用函式隨機產生一個整數，存入ans
ans = random.randint(1, 100) 
count = 0
while True:
	count += 1 # 此為count = count +1 的縮寫
	r = input('請輸入一個整數：')
	r = int(r)
	if r == ans:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif r < ans:
		print('你猜的數字比答案小!')
	elif r > ans:
		print('你猜的數字比答案大!')
	print('這是你猜的第', count, '次')