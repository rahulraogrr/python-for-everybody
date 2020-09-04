# Fibonacci series
# 0,1,1,2,3,5,8,13,21...

try:
    term_number = int(input('Enter Term Number : '))
except:
    print('Please Enter A Valid Integer')
    quit()

n1, n2 = 0, 1
count = 0
if term_number <= 0:
    print('Please enter a positive integer')
elif term_number == 1:
    print('Fibonacci Series')
    print(n1)
else:
    print('Fibonacci Series')
    while count < term_number:
        print(n1)
        sth = n1 + n2
        n1 = n2
        n2 = sth
        count += 1

