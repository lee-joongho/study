# 리스트 패턴 별 일치하는 요소가 많은 순서 정렬
def solution(answers):
    p_1 = [1,2,3,4,5]
    p_2 = [2,1,2,3,2,4,2,5]
    p_3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0; cnt2 = 0; cnt3 = 0
    result_list = [0] * 3
    for idx, val in enumerate(answers):
        if val == p_1[idx%len(p_1)]:
            cnt1 += 1
        if val == p_2[idx%len(p_2)]:
            cnt2 += 1
        if val == p_3[idx%len(p_3)]:
            cnt3 += 1
    result_list[0] = cnt1
    result_list[1] = cnt2
    result_list[2] = cnt3
    
    print("result_list :", result_list)
    result = []
    for idx, val in enumerate(result_list):        
        if val == max(result_list):
            result.append(idx+1)
    print(result)
    return result
    
    
    
    #answer = []
    #return answer