
def get_file_data(filename:str = "sample.txt") -> list[list[int]]:
    with open(filename, 'r') as f:
        d = f.read().split("\n")[0].split(",")
    for i in range(len(d)):
        d[i] = d[i].split("-")
        d[i] = [int(d[i][0]), int(d[i][1])]
    return d

def has_repeating_digits(numb:int) -> bool:
    def convert_to_int(st:str) -> int:
        res = []
        for ch in st:
            res.append(int(ch))
        return res
    
    numb_str = str(numb)
    numb_list = convert_to_int(numb_str)
    
    cycle = []
    for i in range(1, len(numb_list)):
        if len(numb_list) % i == 0:
            cycle = numb_list[:i]
            if len(cycle) < 1:
                continue
            found_repeating = True
            for i in range(len(numb_list)):
                if cycle[i % len(cycle)] != numb_list[i]:
                    found_repeating = False
                    break
            if found_repeating:
                return True
    return False

def calculate_invalid_ids(start:int, end:int) -> list[int]:
    total = []
    for i in range(start, end+1):
        if has_repeating_digits(i):
            total.append(i)
    return total

def iterate_ranges(ranges:list[list[int]]) -> int:
    total = 0
    for r in ranges:
        resp = calculate_invalid_ids(r[0], r[1])
        print(f"For range {r}, received responses {resp}")
        total += sum(resp)
    return total

def test_system_test_the_thing():
    file_data = get_file_data()
    resp = iterate_ranges(file_data)
    print("Test RESPONSE:", resp)
    assert resp == 4174379265

def test_121121():
    resp = iterate_ranges([[121120, 121122]])
    print("Test 121121 response:", resp)
    assert resp == 121121

if __name__ == "__main__":
    test_121121()
    print("Test 121121 passed.")

    test_system_test_the_thing()
    print("System/Function Test Passed.")

    file_data = get_file_data(filename="input.txt")
    file_data.sort()
    print("File_data:", file_data)
    resp = iterate_ranges(file_data)
    print("Test:", resp)
    if resp != 25663320831:
        print("\nDIFF:", abs(resp - 25663320831))
    assert resp == 25663320831