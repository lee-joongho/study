import collections

participant = [leo, kiki, eden]
completion = 	[eden, kiki]

def solution(participant, completion):    
    p_col = collections.Counter(participant)
    c_col = collections.Counter(completion)
    ans_col = p_col - c_col
    print(list(ans_col.keys())[0])
    return list(ans_col.keys())[0]

