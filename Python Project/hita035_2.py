#Finding sum of the series: 1^1/1 + 2^2/2 +....+ n^n/n

#Taking n value as input from user
n = int(input("Enter n value: "))

#Initializing sum
sum = 0

#Loop for calculating sum
for i in range(1,n+1):
        sum = sum + ((i**i) / i)

#Printing the sum of the series
print(f"Sum of the series for {n} values = {sum}")
