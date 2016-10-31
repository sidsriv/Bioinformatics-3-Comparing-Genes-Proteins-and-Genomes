import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

money = map(int,data[0].strip())
coins = []
coins = [int(coin) for coin in data[1].strip().split(',')]


def dpchange(money,coins):
	minnumcoins = [0]
	for m in range(1,money+1):
		minnumcoins.append(float('Inf'))
		for coin in coins:
			if m >= coin:
				if minnumcoins[m - coin] + 1 < minnumcoins[m]:
					minnumcoins[m] = minnumcoins[m - coin] + 1
	return minnumcoins[money]

if __name__ == '__main__':
	print dpchange(money,coins) 