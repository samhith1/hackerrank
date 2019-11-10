#Ask the user to enter the number
#The number should be odd number
import random

def SuccessiveSquares(a,k,m):





    # print (k)
    m1 = 0

    # k4=k3//852
    # k=k3-k4*852


    # m=int(input(("Enter the modulo")))
    p = k
    i = 0
   # print(p)
    list_binary = []
    while (p > 0):
        rem = p % 2
        p1 = int(rem)
        list_binary.append(p1)
        p = p // 2
        # print(p)
        i = i + 1

 #   print(list_binary)
    list_numbers = []
    list_numbers.insert(0, a)
    d = a
    for i in range(1, len(list_binary)):
        d = (d ** 2) % m
        list_numbers.insert(i, d)
   # print(list_numbers)
    result = 1
    for i in range(0, len(list_numbers)):
        result1 = (list_numbers[i] ** list_binary[i])
        result = result * result1
    return (result % m)

number = int(input("Enter the number"))
if number % 2 == 0:
    print("not possible")
else:
    isPrime = False
    count = 0
    number = number - 1
    replicate = number
    while number % 2 == 0:
        count = count + 1
        number = number // 2

    print(str(replicate) +"= 2^"+str(count)+"*"+str(number))

   # print("Getting a random number between 2 and "+str(replicate))

    random_integer=random.randint(2,replicate)
    print("random integer"+str(random_integer))
    replicate = replicate + 1
    print("Applying successive squaring for "+str(random_integer)+" , "+str(number)+", "+str(replicate))

    remainder = SuccessiveSquares(random_integer,number,replicate)
    print (remainder)


    if (remainder == 1 or remainder == (replicate - 1)):
        isPrime=True
    while( not isPrime and count >= 0):
        print("Applying successive squaring for "+str(remainder)+" , "+str(2)+", "+str(replicate))
        remainder = SuccessiveSquares(remainder,2,replicate)
        print (remainder)
        if remainder == 1:
            isPrime=True
            break
        else:
            count =count - 1
    if(isPrime):
        print(str(random_integer)+"is a witness to say that"+str(replicate)+" is prime")
