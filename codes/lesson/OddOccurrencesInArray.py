# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    A.sort()
    B = set(A)
    B = list(B)
    B.sort()
    
    ## sort랑 다 필요없이 count로 찾으면 빠르지면 O(N^2)이 나왔다. 수정한 코드는 O(N) or O(N*logN)이라고 한다...
    # for i in range(len(B)):
    #     tmp = A.count(B[i])
    #     if tmp%2 is 1:
    #         return B[i]
    C = [0]*len(B)
    tmp = A[0]
    idx = 0
    C[idx] += 1
    for i in range(1,len(A)):
        if tmp == A[i]:
            C[idx] += 1
        else:
            tmp = A[i]
            idx += 1
            C[idx] += 1
    for i in range(len(C)):
        if C[i]%2 is 1:
            return B[i]
