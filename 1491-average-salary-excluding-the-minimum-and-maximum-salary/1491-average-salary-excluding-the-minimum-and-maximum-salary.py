class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum1 = sum(salary) - salary[0] - salary[-1]
        sum1 = sum1/(len(salary)-2)
        return sum1