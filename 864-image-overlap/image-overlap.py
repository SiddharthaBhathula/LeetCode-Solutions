from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        a_1 = []
        b_1 = []

        n = len(img1)

        # Store coordinates of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a_1.append((i, j))

                if img2[i][j] == 1:
                    b_1.append((i, j))

        d = {}
        ans = 0

        # Compare every 1 in img1 with every 1 in img2
        for a_x, a_y in a_1:
            for b_x, b_y in b_1:

                translation = (b_x - a_x, b_y - a_y)

                if translation in d:
                    d[translation] += 1
                else:
                    d[translation] = 1

                ans = max(ans, d[translation])

        return ans



                    
        