from math import floor, ceil

def binary_to_denary(binary: str) -> int:
    current = 0
    for char in binary:
        current *= 2
        if char == "1":
            current += 1
    return current

hex_binary_lookup = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}
def binary_to_hex(binary: str) -> str:
    binary_lenth = ceil(len(binary)/4)
    binary = binary.rjust(binary_lenth*4, "0")
    to_return = []
    
    for i in range(binary_lenth):
        current = binary[0+4*i:4+4*i]
        # print(f"  {current}")
        to_return.append(hex_binary_lookup[current])
    return "".join(to_return)



def denary_to_binary(denary: int) -> str:
    current = []
    while denary != 0:
        current.append(denary % 2)
        denary = floor(denary/2)

    current.reverse()
    return "".join(
        [str(item) for item in current]
    )

def denary_to_hex(denary: int) -> str:
    return binary_to_hex(denary_to_binary(denary))

def hex_to_binary(_hex: str) -> str:
    to_return = ""
    for char in _hex:
        to_return += denary_to_binary(hex_to_denary(char))
    return to_return

def hex_to_denary(_hex: str) -> int:
    hex_list = [char for char in _hex]
    hex_list.reverse() #? Used to get indexing correct (for place)
    to_return = 0
    for index, char in enumerate(hex_list):
        num = 0
        match char:
            case "A":
                num = 10
            case "B":
                num = 11
            case "C":
                num = 12
            case "D":
                num = 13
            case "E":
                num = 14
            case "F":
                num = 15
            case _:
                num = int(char)
        to_return += num * 16 ** index
    return to_return

if __name__ == "__main__":
    print(f"1011   -> denary = {binary_to_denary("1011")}")
    print(f"11     -> binary = {denary_to_binary(11)}")
    print("")
    print(f"101001 -> hex    = {binary_to_hex("101001")}")
    print(f"29     -> binary = {hex_to_binary("29")}")
    print("")
    print(f"35     -> hex    = {denary_to_hex(35)}")
    print(f"23     -> denary = {hex_to_denary("23")}")
