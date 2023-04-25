#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each
#input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70],target=50 Output: 3, 4
class TwoSum:
    def find_indices(self, numbers, target):
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return seen[complement], i
            seen[num] = i
        return None