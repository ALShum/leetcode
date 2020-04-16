class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)


    def quickSort1(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        swap_idx = 1
        for i in range(1, len(nums)):
            if nums[i] < pivot:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                swap_idx += 1
        nums[0], nums[swap_idx - 1] = nums[swap_idx - 1], nums[0]
        L = self.quickSort1(nums[:swap_idx - 1])
        R = self.quickSort1(nums[swap_idx:])
        return L + [nums[swap_idx - 1]] + R


    def quickSort2(self, nums): ##in-place
        def quickSortInner(nums, L, R):
            if L < R:
                pivot = nums[L]
                swap_idx = L + 1
                for i in range(L+1, R):
                    if nums[i] < pivot:
                        nums[swap_idx], nums[i] = nums[i], nums[swap_idx]
                        swap_idx += 1
                nums[L], nums[swap_idx - 1] = nums[swap_idx - 1], nums[L]
                quickSortInner(nums, L, swap_idx - 1)
                quickSortInner(nums, swap_idx, R)
        quickSortInner(nums, 0, len(nums))
        return nums


    def mergeSort1(self, nums):
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]
        ll = self.mergeSort1(left)
        rl = self.mergeSort1(right)

        i,j,k = 0,0,0
        while i < len(ll) and j < len(rl):
            if ll[i] < rl[j]:
                nums[k] = ll[i]
                i+=1
            else:
                nums[k] = rl[j]
                j+=1
            k+=1

        while i < len(ll):
            nums[k] = ll[i]
            i+=1
            k+=1

        while j < len(rl):
            nums[k] = rl[j]
            j+=1
            k+=1
        return nums


    def selectSort(self, nums):
        if len(nums) <= 1:
            return nums
        insert_pos = 0
        while insert_pos < len(nums):
            min_val = float('inf')
            min_val_i = -1

            for i in range(insert_pos, len(nums)):
                if nums[i] < min_val:
                    min_val = nums[i]
                    min_val_i = i
            nums[insert_pos], nums[min_val_i] = nums[min_val_i], nums[insert_pos]
            insert_pos += 1
        return nums


    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            pos = i
            val = nums[i]
            while pos > 0 and nums[pos - 1] > val:
                nums[pos] = nums[pos - 1]
                pos -= 1
            nums[pos] = val
        return nums


    import heapq
    def heapSort(self, nums):
        def heapSortInner(nums):
            heapq.heapify(nums)
            while nums:
                elem = heapq.heappop(nums)
                yield elem
        return list(heapSortInner(nums))

