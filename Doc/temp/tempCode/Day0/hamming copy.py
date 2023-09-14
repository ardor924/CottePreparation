# 1번
def distance(strand1, strand2):
    if len(strand1) != len(strand2): raise ValueError("Strands must be of equal length.")
    return sum(c1 == c2 for c1, c2 in zip(strand1, strand2))


# 2번(5줄버전)
def distance(strand1, strand2):    
    # 문자열 길이비교, 길이가 다를시 예외발생
    if len(strand1) != len(strand2): raise ValueError("Strands must be of equal length.")    
    # 동일한 위치의 문자를 튜플형태로 추출하여 일치하는지 여부를 판단, 리스트 컴프리헨션은 True,False로 하여 sum함수로 총합을 리턴
    return sum(char_from_strand1 == char_from_strand2 for char_from_strand1, char_from_strand2 in zip(strand1, strand2))    




# 3번
def distance(strand1, strand2):
    if len(strand1) != len(strand2): 		                                    # 두 문자열의 길이가 틀릴경우 예외발생							
        raise ValueError("Strands must be of equal length.")    
    else : match_count = sum(   char_from_strand1 == char_from_strand2          # 리스트내 결과를 합산하여  match_count에 대입(리스트 컴프리헨션 사용)
                                for char_from_strand1, char_from_strand2        # 동일한 위치의 문자를 추출한뒤 값을비교(맞으면True=1,틀리면False=2)
                                in zip(strand1, strand2)                    )   # zip에서 두 문자열을 튜플형태로 한 문자씩 추출												
    return match_count





    
# 4번
def distance(strand1, strand2):
    if len(strand1) != len(strand2): 									# 두 문자열의 길이가 틀릴경우 예외발생
        raise ValueError("Strands must be of equal length.")    
    match_count = sum(													# 리스트 컴프리헨션 사용
        				char_from_strand1 == char_from_strand2			# 동일한 위치의 문자를 추출한뒤 값을비교(맞으면True=1,틀리면False=2)
            			for char_from_strand1, char_from_strand2 
               			in zip(strand1, strand2)    
        			 )   												# 결과를 합산하여  match_count에 대입
    return match_count


# 5번
def distance(strand1, strand2):
    '''
    info : 	두 문자열의 길이가 틀릴경우 예외발생\n
			리스트 컴프리헨션 사용\n
   			동일한 위치의 문자를 추출한뒤 값을비교(맞으면True=1,틀리면False=2)\n
   			결과를 합산하여  match_count에 대입
    '''
    if len(strand1) != len(strand2): 									
        raise ValueError("Strands must be of equal length.")    
    match_count = sum(													
        				char_from_strand1 == char_from_strand2			
            			for char_from_strand1, char_from_strand2 
               			in zip(strand1, strand2)    
        			 )   												
    return match_count






def distance(strand1, strand2):
    if len(strand1) != len(strand2): 
        raise ValueError("Strands must be of equal length.")    
    else :
        match_count = sum(
         					True if char_from_strand1 == char_from_strand2 else False 
              				for char_from_strand1, char_from_strand2 
                  			in zip(strand1, strand2)
         				 )
    return match_count
