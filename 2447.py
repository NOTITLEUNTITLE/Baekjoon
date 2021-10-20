def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

N = int(input())      

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()


#import sys 
#def append_star(LEN):
#    if LEN == 1:
#        return ['*']
#    Stars = append_star(LEN//3)
#    L = []
#    for S in Stars:
#        L.append(S*3)
#    for S in Stars:
#        L.append(S+' '*(LEN//3)+S)
#    for S in Stars:
#        L.append(S*3)
#    return L
#n = int(sys.stdin.readline())
#print('\n'.join(append_star(n)))
