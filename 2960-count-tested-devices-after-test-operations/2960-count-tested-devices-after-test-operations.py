class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c = 0
        for i in range(0,len(batteryPercentages)):
            if batteryPercentages[i] > 0: 
                c = c+1
                for j in range(i+1,len(batteryPercentages)):
                    if batteryPercentages[j] != 0:
                        batteryPercentages[j] -= 1
        return c


        