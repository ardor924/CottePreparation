#==================================================================
#                       [리스트] Two sum
#==================================================================


# 학습용 def코드 
#------------------------   
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# 연습용  def코드  
#------------------------   
def TESTtwoSum(nums,target):
    pass

#==================================================================

numsExam = [1,12,9,36,22]
targetExam = 48

result = twoSum(numsExam,targetExam)
print(f'정답 : {result}')