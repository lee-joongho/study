#list에서 자신과 왼쪽의 요소들 비교하면서 큰 값 return
def solution(heights):
    heights.reverse()
    answer = []
    check = False
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            if heights[i] < heights[j]:
                answer.append(len(heights) - j)
                check = True
                break
        if check == False:
            answer.append(0)
        check = False
    answer.reverse()
    return answer



#쇠막대기와 레이저의 배치를 표현한 문자열 arrangement가 매개변수로 주어질 때, 잘린 쇠막대기 조각의 총 개수를 return 하도록 solution 함수를 작성해주세요.
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')
    
    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1
    return answer


#list에서 자신과 우측의 요소들을 비교하면서 자신보다 큰값이 연속될때의 연속 횟수 return
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

