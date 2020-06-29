# 배열 자른 후 정렬 문제
# 입출력 예
# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
# 
# 입출력 예 설명
# [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
# [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
# [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

def solution(array, commands):
    result = []
    for command in commands:
        print(command)
        init_idx = command[0]
        last_idx = command[1]
        value_idx = command[2]
        tmp_list = array[init_idx-1:last_idx]        
        tmp_list.sort()
        #print("tmp_list : ", tmp_list)
        res_value = tmp_list[value_idx-1]
        #print(res_value)
        result.append(res_value)
    return result

# 배열에서 중복 제거
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]
def solution(arr):
    result = []
    for c in arr:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result