# 39. Combination Sum
# Solved at the 5% speed mark. You managed to get the backtracking but
# didn't quite optimize effectively. This is because you didn't realize
# that there are no duplicate values, so you don't actually have to recurse
# on the entire list every time—you just do a depth first search starting
# from each index.
def combinationSum(candidates, target):
    results = []
    if len(candidates) == 0:
        return results
    candidates.sort()

    def find_combinations_to_target(current, candidates, target, index):
        # give you function a descriptive name
        if candidates[i] > target: # makes a HUGE difference in optimization
            break
        if target == 0:
            results.append(current)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            new_current = current + [candidates[i]]
            backtrack(new_current, candidates[i:], target - candidates[i], i)

    backtrack([], candidates, target, 0)
    return results

# 213. House Robber II
# Solved very optimally. Note that you managed to get this largely because
# you'd already seen the first House Robber problem, and solved it just by
# doubling the number of DP arrays you were using. Knowing the DP patterns is
# SUPER helpful here.
def robHousesII(nums):
    min_amount = 0
    if len(nums) == 0:
        return min_amount
    if len(nums) == 1:
            return nums[0]

    def max_money_from_houses(houses, max_list):
        max_list[1] = houses[0]
        for i in range(2, len(max_list)):
            max_list[i] = max(max_list[i - 1], houses[i - 1] + max_list[i - 2])
        return max_list[-1]

    with_first = nums[:len(nums) - 1]
    with_last = nums[1:]
    max_list1 = [0] * len(nums)
    max_list2 = [0] * len(nums)
    max_with_first = max_money_from_houses(with_first, max_list1)
    max_with_last = max_money_from_houses(with_last, max_list2)
    return max(max_with_first, max_with_last)
