class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        memo = {}

        def cost_calculater(n):
            # 이미 실행한 계산결과면 저장(중복방지)
            if n in memo:
                return memo[n]

            else : 
                # 0번,1번 계단 비용 그대로 저장
                if n < 2:
                    memo[n] = cost[n]
                # 0번,1번 계단 이 아닌경우    
                else:
                    # 현재계단비용 + 이전계산비용 계산 결과를 저장 
                    memo[n] = cost[n] + min(cost_calculater(n - 1), cost_calculater(n - 2))

            return memo[n]

        # 최소비용을 리턴
        total_cost_1 = cost_calculater(len(cost) - 1)
        total_cost_2 = cost_calculater(len(cost) - 2)
        return min(total_cost_1, total_cost_2)