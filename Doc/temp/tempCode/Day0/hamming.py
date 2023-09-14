def distance(strand1, strand2): # 2번(5줄)
    # 문자열 길이비교, 길이가 다를시 예외발생
    if len(strand1) != len(strand2): raise ValueError("Strands must be of equal length.")    
    # 동일한 위치의 문자를 튜플형태로 추출하여 일치하는지 여부를 판단, 리스트 컴프리헨션은 True,False로 하여 sum함수로 총합을 리턴
    return sum(True if char_from_strand1 == char_from_strand2 else False for char_from_strand1, char_from_strand2 in zip(strand1, strand2))    






