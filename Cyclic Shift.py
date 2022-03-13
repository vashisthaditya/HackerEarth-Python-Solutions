num_test_cases = int(input())
for i in range(num_test_cases):
    array_length, num_of_repetition = map(int, input().split())
 
    count = 0
    bin_num = input()
    original_bin_num = bin_num
    dec_num = int(bin_num, 2)
    maximum = dec_num
    dec_num_array = [dec_num]
 
    for j in range(array_length - 1):
        bin_num = bin_num[1:] + bin_num[0]
        if bin_num == original_bin_num:
            break
        dec_num = int(bin_num, 2)
        dec_num_array.append(dec_num)
    maximum = max(dec_num_array)
    maxIndex = dec_num_array.index(maximum)
    num_cyclic_shifts = maxIndex + (len(dec_num_array) * (num_of_repetition-1))
    print(num_cyclic_shifts)