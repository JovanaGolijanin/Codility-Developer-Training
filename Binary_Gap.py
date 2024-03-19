def solution(N):
    binarniBroj = ''
    while N > 0:
        binarniBroj = str(N % 2) + binarniBroj
        N = N // 2  

    trenutniGap = 0
    maxGap = 0
    
    for cifra in binarniBroj:
        if cifra == '0':
            trenutniGap += 1
        else:
            if trenutniGap > maxGap:
                maxGap = trenutniGap
            trenutniGap = 0
    return maxGap

