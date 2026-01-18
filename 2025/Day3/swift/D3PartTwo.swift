import Foundation

class D3PartTwo {
    func solve(line:String) -> Int {
        let lineInt = line.map{ Int(String($0)) }
        let totalBanks:Int = 12
        var res:[Int] = []
        var currentIdx = lineInt.startIndex
        var minVal:Int?
        for i in 0..<lineInt.count {
            if lineInt[i] == nil {
                continue
            }
            if res.count < totalBanks {
                if let temp = lineInt[i] {
                    res.append(temp)
                }
            }
            minVal = findMin(input: res)
            if minVal == nil {
                continue
            }
            if minVal! > lineInt[currentIdx]! {
                continue
            }
            //TODO: Determine which number to remove from the res to be able to add the current position to res
            var moveDown:Bool = false
            for i in 0..<res.count {
                if res[i] == minVal! && !moveDown{
                    moveDown = true
                    res[i] = res[i+1]
                } else if moveDown && i == res.count - 2 {
                    break
                } else if moveDown {
                    res[i] = res[i+1]
                }
            }
        }
        return res.reduce(0, {x, y in
            (x * 10) + y
        })
    }

    func findMin(input:[Int] = []) -> Int? {
        if input.count <= 0 {
            return nil
        }
        var min = input[0]
        for i in 1..<input.count {
            if min > input[i] {
                min = input[i]
            }
        }
        return min
    }

    func readFile(filename:String = "sample.txt") throws -> [String] {
        return try String(contentsOfFile: "../\(filename)", encoding: .utf8)
            .split(separator: "\n")
            .map { String($0) }
    }
}

let filename = "input.txt"
let d3p2 = D3PartTwo()
let fileData = try d3p2.readFile()
var resp:[Int] = []
for e in fileData {
    resp.append(d3p2.solve(line: e))
}
let result:Int = resp.reduce(0, {x, y in
    x + y
})
print("-> RESP: \(result)")