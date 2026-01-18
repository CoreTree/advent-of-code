def read_file():
    with open('input.txt', 'r') as f:
        d = f.read().split('\n')[0].split(',')
    d.sort()
    return d

def part2(n):
    if len(n) < 2:
        return False
    if len(n) < 3:
        if n[0] == n[1]:
            return int(n)
    elif len(n) < 4:
        if n[0] == n[1] == n[2]:
            return int(n)

    else:
        x = ""
        for i, s in enumerate(n):
            x += s
            _count = n[i + 1 :].count(x)
            sub_str_len = len(x)
            if (len(n[i + 1 :]) != 0) and len(n[i + 1 :]) == (_count * sub_str_len):
                return int(n)

    return False

def main():
    t = 0
    for r in read_file():
        r1, r2 = r.split("-")
        resp = []
        for i in range(int(r1), int(r2) + 1):
            x = part2(str(i))
            if not isinstance(x, bool):
                t += x
                resp.append(x)
        print(f"For range: [{r1}, {r2}], received responses {resp}")
    print(t)

# with open('input.txt', 'r') as f:
#     d = f.read()
# print(input(d))
main()