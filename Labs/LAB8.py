fibo = [1, 2, 3, 5, 8, 13, 21]

boolean = True
for i in range(2, len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i] == fibo[i-1] + fibo[i-2]:
        continue
    else:
        boolean = False
        break

if boolean:
    print("It is a Fibonacci list")
else:
    print("It is not a Fibonacci list")
