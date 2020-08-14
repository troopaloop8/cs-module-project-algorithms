'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_vals = []
    i = 0
    while i < len(nums):
        end_index = i + k
        
        try:
            
            window = nums[i:end_index]
            if len(window) < k:
                break
            else:
                print(window)
                i += 1
                winmax = max(window)
                max_vals.append(winmax)
        except IndexError:
            i += 1
    
    return max_vals
        

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
