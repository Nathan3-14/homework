import statistics

nums = []
print("Enter numbers, type 'end' to exit and recieve your mean")
while True:
    in_num = input("Enter a number\n>> ")
    try:
        in_num = int(in_num)
    except:
        if in_num == "end":
            break
        print("Please enter an integer")
        continue
    nums.append(in_num)
print(f"Mean: {statistics.mean(nums)}")
input("Press enter to continue")