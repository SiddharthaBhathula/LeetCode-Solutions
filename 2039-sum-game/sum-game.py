class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Determines whether Alice can guarantee a win in the Sum Game.

        The string is divided into two halves. Alice wins if the
        final sums of both halves cannot be made equal by Bob.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(num)

        # Sum of known digits in the first and second halves.
        sum1 = 0
        sum2 = 0

        # Number of '?' in the first and second halves.
        q1 = 0
        q2 = 0

        # Process both halves of the string.
        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    q1 += 1
                else:
                    sum1 += int(num[i])
            else:
                if num[i] == '?':
                    q2 += 1
                else:
                    sum2 += int(num[i])

        # If the total number of '?' is odd, Alice wins.
        if (q1 + q2) % 2 == 1:
            return True

        # Difference between the number of '?' on both sides.
        question_diff = q2 - q1

        # Maximum possible difference that the '?' characters
        # can create between the two halves.
        required_difference = question_diff * 9 // 2

        # Alice wins if the existing digit difference cannot
        # be balanced by assigning values to '?'.
        return sum1 - sum2 != required_difference