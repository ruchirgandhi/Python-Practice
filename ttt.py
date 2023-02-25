def check_if_sum_possible(arr, k):
    def targetSum(S, i, currentsum, target, count):

        # Base Case
        if currentsum == target:
            return True

        if i == len(S):
            return False

        res1 = targetSum(S,i+1, currentsum+S[i], target, count+1)



print(check_if_sum_possible([2,4,5],6))

