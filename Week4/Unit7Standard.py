def find_cruise_length(cruise_lengths, vacation_length):
    left = 0
    right = len(cruise_lengths) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if cruise_lengths[mid] == vacation_length:
            return True
        elif vacation_length < cruise_lengths[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))