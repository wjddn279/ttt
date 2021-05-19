# U X : 현재 선택된 행에서 X 칸 위에 있는 행을 선택 ---> 선택되는 행이 바뀌게 된다.
# D X : 현재 선택된 행에서 X 칸 아래에 있는 행을 선택 ---> 선택되는 행이 바뀌게 된다.
# C : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택한다. 만약 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택한다 --> 현재 행을 pop()
# Z : 가장 최근에 삭제된 행을 원래되고 복구한다.  단, 현재 선택된 행은 바뀌지 않는다.

from collections import deque

def command(cmd, array,k,n,del_stack):
    m =0
    if cmd == "C":  # 현재 선택된 행을 삭제 / 바로 아래 행을 선택
        array[k] ="X"
        del_stack.append(k)
        print("del",del_stack)
        if k == n-1: # 삭제된 행이 가장 마지막 행인 경우  ---> 바로 윗 행 선택
            k -=1
            print(k,cmd)
        else : # 삭제 된 행이 가장 마지막 행이 아닌 경우
            k= k +1
            print(k,cmd)
    elif cmd == "Z":
        if del_stack:
            m = del_stack.pop()
        array[m] ="0"
        print(k,cmd)
    elif cmd[0] == "D":
        if "X" in array[k - int(cmd[2]):k+1]:
            k = k + int(cmd[2])-array[k + int(cmd[2]):k+1].count("X")
        else:
            k = k + int(cmd[2])
        print(k,cmd)
    else: # U
        if "X" in array[k - int(cmd[2]):k+1]:
            k = k - int(cmd[2])-array[k - int(cmd[2]):k+1].count("X")
        else:
            k = k - int(cmd[2])
        print(k,cmd)
    return k,del_stack
def solution(n,k,cmd):
    answer = ""
    arr = ["0"]*n
    del_stack =[] # 삭제된 행 번호들을 들고 있음
    for i in cmd:
        k,del_stack = command(i,arr,k,n,del_stack)
        print(arr)
    answer = ''.join(arr)
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# 0000x000
#