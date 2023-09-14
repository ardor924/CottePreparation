#==================================================================
#               [해시테이블-딕셔너리] Valid parentheses
#==================================================================


# 학습용 def코드 
#------------------------   

def twoSum(nums, target) :
    number_index_dict = {} 
    for index, number in enumerate(nums): 
        target_diff = target - number  
        # 조건 만족시 두 nums 숫자의 리스트 반환
        if target_diff in number_index_dict:  
            return [number_index_dict[target_diff], index] 
        # 조건 만족 안될시 딕셔너리에 처음 인덱스 저장
        number_index_dict[number] = index  
    return []


#==================================================================

numsExam = [1,12,9,36,22]
targetExam = 48

result = twoSum(numsExam,targetExam)
print(f'정답 : {result}')