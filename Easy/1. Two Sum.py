class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #思路 : target 為兩個元素的解，第二個元素一定在第一個元素的左邊
        for num in nums :
            answer_num = target - num  #第二項元素為 target 減去第一項元素的值
            first_num_index = nums.index(num) # 第一項元素的位置
            next_num_index = first_num_index + 1 #第二項元素的初始位置
            nex_num_list = nums[next_num_index : ] #有可能是第二項的新串列
            if answer_num in nex_num_list : #當第二項有在新串列中，直接回傳第一個元素的位置及第二個元素的位置
                return (first_num_index, next_num_index + nex_num_list.index(answer_num)) 
                # 這裡注意第二個元素位置為 "第二項元素的初始位置" + "在新串列某位置" = 原本串列第二元素的位置 