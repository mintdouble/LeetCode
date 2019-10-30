# 建立一个列表维护每一轮比赛的得分，按照对应的规则来进行计算总得分
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        prior = []
        score = 0
        for i in ops:
            if i == 'C':
                if len(prior) > 0:
                    score -= prior[-1]
                    prior.pop()
            elif i == 'D':
                if len(prior) > 0:
                    score += (2 * prior[-1])
                    prior.append(2 * prior[-1])
            elif i == '+':
                if len(prior) > 1:
                    score += (prior[-1] + prior[-2])
                    prior.append(prior[-1] + prior[-2])
                elif len(prior) > 0:
                    score += prior[-1]
                    prior.append(prior[-1])
                else:
                    continue  
            else:
                score += int(i)
                prior.append(int(i))
        return score
