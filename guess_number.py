# 產生一個隨機整數 1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了!"
# 猜錯的話，告訴他"比答案大/小"

import random

ans = random.randint(1, 100)
while True:
	r = input('請輸入一個整數：')
	r = int(r)
	if r == ans:
		print('終於猜對了!')
		break
	elif r < ans:
		print('再接再厲，你猜的數字比答案小!')
	elif r > ans:
		print('再接再厲，你猜的數字比答案大!')