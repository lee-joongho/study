##########################################
# 입력 받은 문자열에서 앞, 뒤의 특정 문자를 제거하는 기능
# @param    message     입력 문자열
# @param    trimStr     제거할 문자
# @return   결과 문자열
##########################################
def getTrimString(message, trimStr):
    result = ""
    head_ind = 0
    tail_ind = len(message)
    for i in range(len(message)):
        if message[i] == trimStr:
            head_ind = i+1
        else:
            break
    for i in range(len(message)-1,-1,-1):
        if message[i] == trimStr:
            tail_ind = i
        else:
            break
    result = message[(head_ind):tail_ind]
    return result