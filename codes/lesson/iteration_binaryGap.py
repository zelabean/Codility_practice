# 주어진 수를 2진수로 나타냈을때 1과 1사이의 공간의 최대값을 구하는 문제

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#dec2bin 의 결과는 역순으로 나타나서 실제 이진수의 값과는 다르다.
#하지만 코드의 목적은 1과 0의 위치를 찾기 위함으로 역순변환은 하지 않았다.
#2진수를 구하는 과정은 그냥 일반 수학에서 손으로 2진수를 찾듯이 찾았는데 수학적으로 더 좋은 방법이 있을 것 같다.
def dec2bin(N):
    bin = list()
    while(True):
        N, rem = N//2, N%2
        if N is 0:
            bin.append(rem)
            break
        if rem is not 0:
            bin.append(1)
        else:
            bin.append(0)
    return bin

#1의 위치를 찾아서 인덱스 값을 빼주어 사이공간의 크기를 알아낸다.
def find_gap(bin):
    gap = 0
    ones = list()
    for i in range(len(bin)):
        if bin[i] is 1:
            ones.append(i)
    
    if len(ones) > 1:
        max = 0
        for i in range(len(ones)-1):
            tmp = ones[i+1] - ones[i] - 1
            
            if max < tmp:
                max = tmp
        gap = max
    return gap

def solution(N):
    answer = 0
    # write your code in Python 3.6
    bin = dec2bin(N)
    answer = find_gap(bin)
    return answer
