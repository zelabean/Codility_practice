# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    if l is 0: # 리스트가 빈 리스트일때 예외처리
        return A
    K = K%l # K값이 리스트 길이보다 길어지면 에러나므로 리스트 인덱스 까지만 갖도록 처리해줌
    tmp = [0]*l
    for i in range(l-K):
        tmp[i+K] = A[i]
        
    for i in range(K):
        tmp[K-i-1] = A[l-i-1]
    return tmp
