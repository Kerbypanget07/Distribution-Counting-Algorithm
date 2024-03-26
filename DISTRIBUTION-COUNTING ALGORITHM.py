def count_frequency_and_sort(input_string):
    freq = {}
    for char in input_string:
        freq[char] = freq.get(char, 0) + 1
    
    alphabets = sorted(freq.keys())
    
    pos = {}
    for i, char in enumerate(alphabets):
        pos[char] = i
    
    tbl = []
    for char in input_string:
        tbl.append((char, pos[char]))
    
    tbl.sort(key=lambda x: x[1])
    
    sorted_output = ''.join([char for char, _ in tbl])
    
    return sorted_output

input_str = "bcddcbaab"
output = count_frequency_and_sort(input_str)
print("Sorted output:", output)
