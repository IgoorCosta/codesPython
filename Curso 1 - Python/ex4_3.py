num = int(input())

div3 = num%3
div5 = num%5

if (div3 == 0 and div5 == 0):
    print("FizzBuzz")
else: print(num)
