memo = {}
def climbStairs(n) :
    memo = {} 

    def calculate(n):
        if n in memo:
            return memo[n]
        if n == 1 or n == 2:
            memo[n] = n
        else:
            memo[n] = calculate(n - 1) + calculate(n - 2)
        return memo[n]
    return calculate(n)


print(f'계단오르는 방법 : {climbStairs(5)}가지')
