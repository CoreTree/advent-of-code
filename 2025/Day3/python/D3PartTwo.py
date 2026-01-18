def read_file(filename:str = "../sample.txt") -> str:
    with open(filename, 'r') as f:
        d = f.read()
    return d

def sum_total(a:list[int]) -> int:
    total = 0
    for num in a:
        total *= 10
        total += num
    return total

def solve(line:str, battery_banks:int = 12) -> int:
    res = []
    for ch in line:
        if len(res) == 0:
            res.append(int(ch))
            continue
        if int(ch) >= min(res) and len(res) + 1 > battery_banks:
            temp = res.copy()
            temp.remove(min(temp))
            temp.append(int(ch))
            if sum_total(temp) > sum_total(res[1:] + [int(ch)]):
                res.remove(min(res))
            else:
                res.remove(res[0])
            res.append(int(ch))
        elif len(res) < battery_banks:
            res.append(int(ch))
    total = 0
    for num in res:
        total *= 10
        total += num
    print(line, total, res)
    return total

filename = "../input.txt"
# file_data = read_file(filename)
file_data = read_file()
total = 0
for i in range(len(file_data.split('\n'))):
    line = file_data.split('\n')[i]
    total += solve(line)
print("TOTAL:", total)
print("\nDIFF:", 3121910778619 - total)
assert total == 3121910778619

file_data = read_file(filename=filename).split('\n')
if file_data[-1] == "":
    del file_data[-1]
total = 0
for i in range(len(file_data)):
    line = file_data[i]
    total += solve(line)
    print(i, total)
print("TOTAL:", total)
print("\nDIFF:", 170147128753455 - total)
assert total == 170147128753455