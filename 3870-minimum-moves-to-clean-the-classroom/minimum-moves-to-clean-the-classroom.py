from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Locate the starting position and assign a unique bit
        # to each litter cell for bitmask representation.
        start = None
        litter_id = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # No litter to collect.
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1

        # BFS state:
        # (row, column, collected_litter_mask, remaining_energy)
        queue = deque([(start[0], start[1], 0, energy)])

        # For a given (position, mask), keep the maximum energy seen.
        # A state with less or equal energy is always dominated.
        best_energy = {
            (start[0], start[1], 0): energy
        }

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = 0

        while queue:
            # Process one BFS level at a time.
            for _ in range(len(queue)):
                r, c, mask, remaining = queue.popleft()

                # All litter has been collected.
                if mask == full_mask:
                    return moves

                # We cannot make another move with zero energy.
                # Reaching a reset cell restores energy immediately,
                # so such states are handled when entering 'R'.
                if remaining == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Skip cells outside the classroom or blocked by obstacles.
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_remaining = remaining - 1
                    new_mask = mask

                    # Collect litter using its corresponding bit.
                    if classroom[nr][nc] == 'L':
                        new_mask |= 1 << litter_id[(nr, nc)]

                    # Reset energy when entering a reset area.
                    if classroom[nr][nc] == 'R':
                        new_remaining = energy

                    state = (nr, nc, new_mask)

                    # If this state was already reached with more energy,
                    # there is no benefit in exploring it again.
                    if (
                        state in best_energy
                        and best_energy[state] >= new_remaining
                    ):
                        continue

                    best_energy[state] = new_remaining
                    queue.append(
                        (nr, nc, new_mask, new_remaining)
                    )

            moves += 1

        # All litter cannot be collected.
        return -1