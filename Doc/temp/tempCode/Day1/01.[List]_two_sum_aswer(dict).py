class Solution:
    def twoSum(self, nums, target) :
        '''
        Instruction:
            nums 리스트에서 두수를 선택하여 그 합이 타겟 값과 같아지는지 확인하는 함수            
        Params :
            nums : 리스트 내의 두 수를 더했을 때 타겟 값을 만들 수 있는 숫자 리스트
            target : 두 수를 더해야 하는 목표 값        
        Return :
            조건 만족시 => 조건을 만족하는 두 숫자의 인덱스를 담은 리스트
            조건 만족 안될시 => 빈 리스트 리턴
        '''
        
        number_index_dict = {} 

        for index, number in enumerate(nums): 
            target_diff = target - number  

            # 조건 만족시 두 nums 숫자의 리스트 반환
            if target_diff in number_index_dict:  
                return [number_index_dict[target_diff], index] 

            # 조건 만족 안될시 딕셔너리에 처음 인덱스 저장
            number_index_dict[number] = index  

        return []

