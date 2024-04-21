def merge_sort(L, a, b):  # a = left end # b = right end
    if a < b:
        half = (a + b) // 2
        merge_sort(L, a, half)
        merge_sort(L, half + 1, b)

        L1 = L[a:half + 1]
        L2 = L[half + 1:b + 1]

        i = a
        j = 0
        k = 0

        while j < len(L1) and k < len(L2):
            if L1[j] <= L2[k]:
                L[i] = L1[j]
                j += 1
            else:
                L[i] = L2[k]
                k += 1
            i += 1

        while j < len(L1):
            L[i] = L1[j]
            j += 1
            i += 1

        while k < len(L2):
            L[i] = L2[k]
            k += 1
            i += 1

# Example usage:
L = [2, 7, 3, 5, 8, 1, 4, 6]
merge_sort(L, 0, len(L) - 1)
print(L)
