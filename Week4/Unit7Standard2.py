def find_cruise_length(cruise_lengths, vacation_length):
    """
    Return True if vacation_length is found within the sorted cruise_lengths list 
    using a binary search; otherwise return False.
    """
    left, right = 0, len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1
    return False


def find_cabin_index(cabins, preferred_deck):
    """
    Return the index at which preferred_deck should be inserted 
    in the sorted cabins list to maintain order, or the exact index if found.
    """
    return find_cabin_index_help(cabins, preferred_deck, 0, len(cabins) - 1)


def find_cabin_index_help(cabins, preferred_deck, l, r):
    """
    Helper function that uses recursion to find the index 
    for preferred_deck in the sorted cabins list.
    """
    if l > r:
        return l
    
    m = l + (r - l) // 2
    
    if cabins[m] == preferred_deck:
        return m
    elif cabins[m] < preferred_deck:
        return find_cabin_index_help(cabins, preferred_deck, m + 1, r)
    else:
        return find_cabin_index_help(cabins, preferred_deck, l, m - 1)


def count_checked_in_passengers(rooms):
    """
    Return the number of passengers checked in (i.e., the count of 1s),
    assuming rooms is sorted (all 0s followed by 1s).
    Uses a binary search approach to find the first occurrence of 1.
    """
    l, r = 0, len(rooms) - 1
    first_one = len(rooms)
    
    while l <= r:
        mid = l + (r - l) // 2
        if rooms[mid] == 1:
            first_one = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return len(rooms) - first_one


def is_profitable(excursion_counts):
    n = len(excursion_counts)
    
    # Binary search to find the special x
    left, right = 0, n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        x = n - mid
        
        if excursion_counts[mid] >= x:
            if mid == 0 or excursion_counts[mid - 1] < x:
                return x
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

    
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))

# More Examples

print(is_profitable([0]))        # Expected: -1 
# Explanation:
#   - x = 0 would require exactly 0 excursions ≥ 0, but we have 1 excursion.
#   - x = 1 would require exactly 1 excursion ≥ 1, but we have 0.

print(is_profitable([1]))        # Expected: 1
# Explanation:
#   - x = 1 => we want exactly 1 excursion ≥ 1, and we have 1 excursion (which is 1).

print(is_profitable([0, 1]))     # Expected: 1
# Explanation:
#   - x = 1 => we want exactly 1 excursion ≥ 1, and we have exactly 1 (the "1").

print(is_profitable([1, 2]))     # Expected: -1
# Explanation:
#   - x = 1 => we'd need exactly 1 excursion ≥ 1, but we have 2.
#   - x = 2 => we'd need exactly 2 excursions ≥ 2, but only one excursion (the "2") is ≥ 2.

print(is_profitable([2, 2]))     # Expected: 2
# Explanation:
#   - x = 2 => we want exactly 2 excursions ≥ 2, and we have both [2, 2].

print(is_profitable([1, 2, 3]))  # Expected: 2
# Explanation:
#   - x = 2 => we want exactly 2 excursions ≥ 2, and indeed (2, 3) are ≥ 2.

print(is_profitable([0, 1, 2]))  # Expected: -1
# Explanation:
#   - x = 1 => we'd need exactly 1 excursion ≥ 1, but we have 2 (1, 2).
#   - x = 2 => we'd need exactly 2 excursions ≥ 2, but we have just 1 (the "2").

print(is_profitable([0, 1, 2, 3, 4]))  # Expected: -1
# Explanation:
#   - There's no integer x where the number of excursions ≥ x equals x.
