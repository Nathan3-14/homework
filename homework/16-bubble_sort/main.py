def bubble_sort(_unordered_list):
    new_list = _unordered_list.copy()
    comparisons = 0
    passes = 0
    while comparisons != 0 or passes != len(_unordered_list): #? Checks if there were no comparisons, or the total amount of passes is the most
        comparisons = 0
        for index in range(len(new_list)-(1+passes)):
            if new_list[index] > new_list[index+1]:
                new_list[index], new_list[index+1] = new_list[index+1], new_list[index]
            comparisons += 1
        passes += 1
    return new_list

if __name__ == "__main__":
    print(bubble_sort([4, 1, 6, 2, 1, 8]))
