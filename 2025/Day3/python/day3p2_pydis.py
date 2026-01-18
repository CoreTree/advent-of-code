def Solution(input: str) -> int:
    total: int = 0
    for bank in input.strip().split("\n"):
        bank = bank.strip() # just to make sure
        joltage: int = 0
        for i in range(11, -1, -1):
            options = set(bank[:-i] if i else bank)
            digit = sorted(options, key=lambda e: int(e), reverse=True)[0]
            bank = bank[bank.index(digit) + 1:]
            joltage += int(digit) * (10 ** i)
        print(joltage)
        total += joltage
    return total

with open('../input.txt', 'r') as f:
    d = f.read()
print("Solution:", Solution(d))