class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = []

        for i in range(len(arr)):
            arr.pop(0)
            if arr:
                new.append(max(arr))
            else:
                new.append(-1)

        return new