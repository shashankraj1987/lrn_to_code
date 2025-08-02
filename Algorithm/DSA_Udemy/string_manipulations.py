import heapq
from collections import Counter


def first_non_repeating_char(val: str) -> int | None:
        if not val:
            return None

        char_counts = Counter(val)
        print(char_counts)

        for x, char in enumerate(val):
            if char_counts[char] == 1:
                return x
        return None

def reorganizing_string(val: str) -> str:
    count = Counter(val)
    max_heap = [[-cnt,char] for char, cnt in count.items()]

    heapq.heapify(max_heap)
    # print(max_heap)

    prev = None
    res = ''
    while max_heap or prev:

        if prev and not max_heap:
            return ""
        # else:
            # print("Max Heap is ", max_heap)
            # print("Prev is ", prev)

        cnt, char = heapq.heappop(max_heap)
        # print(f"Count is {cnt}")
        # print(f"Character is {char}")
        res += char
        cnt += 1

        if prev:
            heapq.heappush(max_heap, prev)
            # print("When Prev, max_heap is", max_heap)
            prev = None
        if cnt != 0:
            prev = [cnt, char]
            # print(prev, "\n******************************")
    return res


string = "aabbbbccddefg"
non_rep = first_non_repeating_char(string)
if non_rep:
    print(string[non_rep])

print(reorganizing_string(string))