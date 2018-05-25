# coding=UTF-8

price_start = 0.20
price_stage = float(raw_input("请输入当前GHC价格： "))
growth_rate = float(raw_input("请输入日涨幅： "))
coin_count_daily = float(raw_input("请输入每日挖币量： "))
amount_invest = float(raw_input("请输入投资金额： "))
print("请选择计算方式：")
print("1、日日卖")
print("2、月月卖")
print("3、周周卖")
print("4、到期卖")
cal_type = int(raw_input("请输入计算方式： "))

days_count = 365 * 1
income_total = 0
is_earn = 0
fees_rate = 0.1
output = "计算依据：GHC价格" + str(price_stage) + "|日涨幅:" + str(growth_rate) + "|每日挖币量" + str(coin_count_daily)
count = 1

#用于计算月月卖
days_monthly = 0
price_monthly = 0
coins_monthly = 0
num_monthly = 0

#用于计算到期卖
coins_out = 0

#用于计算按周卖
days_weekly = 0
price_weekly = 0
coins_weekly = 0
num_weekly = 0

#用于计算算力降
#算力下降
cal_rate = -0.01

#每日收益
income_daily = 0
#累计收益
income_total

while count <= int(days_count):
	#当日价格
	price_daily = price_stage + price_start*growth_rate*count

	#算力下降
	coin_count_daily = coin_count_daily * (1 + cal_rate)

	if cal_type == 1:
		#日日卖
		income_daily = coin_count_daily * price_daily
		income_total = income_total + income_daily

		output = "当日价格：" + str(price_daily) + "|当天收益:" + str(income_daily) + "|累计收益" + str(income_total)
		print("第"+str(count)+"天： " + str(output))

		if (amount_invest < income_total*(1-fees_rate) and is_earn == 0):
			is_earn = 1
			print("-----------------------------已经回本-----------------------------")

	elif cal_type == 2:
		#月月卖
		days_monthly = days_monthly + 1
		coins_monthly = coins_monthly + coin_count_daily

		if days_monthly > 30 :
			days_monthly = 1
			num_monthly = num_monthly + 1
			income_total = income_total + coins_monthly * price_daily
			output = "卖出价格：" + str(price_daily) + "|当月收益:" + str(coins_monthly * price_daily) + "|累计收益" + str(income_total)
			print("第"+str(num_monthly)+"月： " + str(output))

			if (amount_invest < income_total*(1-fees_rate) and is_earn == 0):
				is_earn = 1
				print("-----------------------------已经回本-----------------------------")

			#月统计后归零
			coins_monthly = 0

	elif cal_type == 3:
		#周周卖
		days_weekly = days_weekly + 1
		coins_weekly = coins_weekly + coin_count_daily

		if days_weekly > 7:
			days_weekly = 1
			num_weekly = num_weekly + 1
			income_total = income_total + coins_weekly * price_daily

			output = "卖出价格：" + str(price_daily) + "|当周收益:" + str(coins_weekly * price_daily) + "|累计收益" + str(income_total)
			print("第"+str(num_weekly)+"周： " + str(output))

			if (amount_invest < income_total*(1-fees_rate) and is_earn == 0):
				is_earn = 1
				print("-----------------------------已经回本-----------------------------")

			#周统计后归零
			coins_weekly = 0
	else:
		#到期卖
		coins_out = coins_out + coin_count_daily
		income_total = coins_out * price_daily
		if (amount_invest < income_total*(1-fees_rate) and is_earn == 0):
				is_earn = 1
				print("第"+str(count)+"天已经回本")

			
	count = count + 1