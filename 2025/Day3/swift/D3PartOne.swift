import Foundation

class D3PartOne {
    func search(_ line:String) -> Int {
        var pair:Int = 0
        var calculatedTemp:Int = 0
        var tempI:String.Index = "".endIndex
        var tempJ:String.Index = "".endIndex
        for i in 0..<line.count {
            for j in (i+1)..<line.count {
                tempI = line.index(line.startIndex, offsetBy: i)
                tempJ = line.index(line.startIndex, offsetBy: j)
                calculatedTemp = ((Int("\(line[tempI])") ?? 0) * 10)
                calculatedTemp += (Int("\(line[tempJ])") ?? 0)
                
                if calculatedTemp > pair {
                    pair = calculatedTemp
                }
            }
        }
        return Int(String(describing: pair))!
    }
}

// CLI Runtime;
let fileName = "input.txt"
let lines = try String(contentsOfFile: "../\(fileName)", encoding: .utf8)
                .split(separator: "\n")
                .map { String($0) }
let d3po = D3PartOne()
var total:Int = 0
for line in lines {
    total += d3po.search(line)
}
print("Total: \(total)")