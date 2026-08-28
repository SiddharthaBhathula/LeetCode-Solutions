class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether s can form a palindrome
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Characters available for the left half
        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        def make_pal(left):
            if n % 2:
                return left + middle + left[::-1]
            return left + left[::-1]

        # --------------------------------------------------
        # First check whether target's left half itself can
        # be constructed.
        # --------------------------------------------------

        target_left = target[:m]

        used = [0] * 26
        possible = True

        for ch in target_left:
            idx = ord(ch) - ord('a')
            used[idx] += 1

            if used[idx] > half_cnt[idx]:
                possible = False
                break

        if possible:
            candidate = make_pal(target_left)

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # Otherwise, find the rightmost position where we can
        # make the left half larger than target's left half.
        # --------------------------------------------------

        for i in range(m - 1, -1, -1):

            # We need target[:i] to be available.
            prefix = target[:i]

            used = [0] * 26
            possible = True

            for ch in prefix:
                idx = ord(ch) - ord('a')
                used[idx] += 1

                if used[idx] > half_cnt[idx]:
                    possible = False
                    break

            if not possible:
                continue

            # At position i, choose the smallest character
            # greater than target[i].
            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):

                # Is this character still available?
                if used[c] >= half_cnt[c]:
                    continue

                # Build the new prefix
                left = prefix + chr(ord('a') + c)

                # Remaining characters
                remaining = half_cnt[:]

                for ch in left:
                    remaining[ord(ch) - ord('a')] -= 1

                # Fill the suffix with smallest characters
                suffix = []

                for j in range(26):
                    suffix.extend(
                        [chr(ord('a') + j)] * remaining[j]
                    )

                left += ''.join(suffix)

                candidate = make_pal(left)

                if candidate > target:
                    return candidate

        return ""
        