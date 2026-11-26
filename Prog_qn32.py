# Best time to buy and sell stock

prices = [7,1,5,3,6,4]
profit = 0
smallest = float('inf')
for i in range(0, len(prices)):
    smallest = min(smallest, prices[i])
    profit = max(profit, prices[i] - smallest)

print("The maximum profit is:", profit)
    