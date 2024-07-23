# written by copilot based on my code
    def minWindow(s: str, t: str) -> str:
        if len(s) < len(t): return ''

        substring_counter = Counter(t)
        counter = Counter()
        l = r = 0
        min_length = float('inf')
        min_string = ''

        for r, c in enumerate(s):
            if c in substring_counter:
                counter[c] += 1
            while counter & substring_counter == substring_counter:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_string = s[l:r+1]
                d = s[l]
                if d in substring_counter:
                    counter[d] -= 1
                l += 1

        return min_string if min_length <= len(s) else ''
