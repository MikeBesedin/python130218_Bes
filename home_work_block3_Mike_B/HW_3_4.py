deposit = 1000
P = float(input('Enter digit  in range  0 < P < 25: '))
goal = 1100
i = 1
profit = 0
profit = deposit * P / 100 * i
end_of_month = deposit + profit
while end_of_month <= goal:
    i += 1
    profit = deposit * P / 100 * i
    end_of_month = deposit + profit

print('To exceed goal, which is 1100 BYN, it takes %.0f month and your deposit will be %.2f BYN' % (i, end_of_month))