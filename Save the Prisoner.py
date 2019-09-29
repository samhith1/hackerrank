#!/bin/python3


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    prisonerchoosen=s
    m=m-1
    prisonerchoosen+=1
    r=m%n
    result=(r+(prisonerchoosen-1))%n
    if(result==0):
        return n
    else:
        return result
    pass

if __name__ == '__main__':
    list1=[]

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        list1.insert(t_itr,result)
    print(list1)

