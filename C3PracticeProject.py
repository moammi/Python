def collatz(number):

    if number % 2 == 0:
        print(number //2)
        return number // 2
    
    elif number % 2 == 1:
        answer = 3 * number +1
        print(answer)
        return answer

x = input('Please fill in a number')
try:
    while x !=1:
          x = collatz(int(x))
except ValueError:
    print('Error: You can only fill in a number')
