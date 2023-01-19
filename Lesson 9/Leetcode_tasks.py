# HW 9 Vitalii Holub

# 1. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def single_number(nums: list[int]):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num


# 2. Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# 3. Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

def third_max(nums: list[int]) -> int:
    nums = set(nums)
    if len(nums) >= 3:
        return sorted(nums)[-3]
    return max(nums)
