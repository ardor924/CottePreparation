nums = [8,71,24,67,95,88,92,115,607,112]
target = 615

def two_sum(nums,target) :
    
    number_index_dict = {}
    
    for index,number in enumerate(nums) :
        target_diff = target - number
        
        if target_diff in number_index_dict  :
            return [number_index_dict[target_diff],index] # [딕셔너리에 저장한인덱스값,현재인덱스값]

        number_index_dict[number] = index

        
    return []


print(two_sum(nums,target))