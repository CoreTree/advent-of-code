import Foundation

func getFileData(filename:String = "sample.txt") throws -> [[Int]] {
    let fileRead = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
                    .split(separator: ",")
                    .map {
                        String($0).last != "\n" ? String($0) : String(String($0).dropLast(1))
                    }
    let res:[[Int]] = fileRead.map {
                    let temp = $0.split(separator: "-")
                    return [Int(temp[0])!, Int(temp[1])!]
                }
    return res
}

func hasRepeatingDigits(_ numb:Int) -> Bool {
    let numbStr = String(describing: numb) //This could also be "\(numb)"
    if numbStr.count % 2 == 1 { //Why bother if you can't repeat numbers anyways?
        return false
    }
    var cycle:[Int] = []
    var current:Int = 0
    var position:String.Index = numbStr.startIndex
    for i in 0..<numbStr.count {
        position = numbStr.index(numbStr.startIndex, offsetBy: i)
        let cyclePosition = cycle.index(cycle.startIndex, offsetBy: i % cycle.count)
        print(".> \(cycle[cyclePosition]) \(numbStr[position])")
        if cycle.count == 0 || (numbStr.count / 2 > cycle.count && cycle[cyclePosition] == Int(numbStr[position])) {
            cycle = numbStr[numbStr.startIndex...position].map { Int(String($0))! }
        } else {
            return false
        }
    }
    return true
}

func calculateInvalidIDs(_ start:Int, _  end:Int) -> Int {
    var total:Int = 0
    for i in start...end {
        if hasRepeatingDigits(i) {
            print("> \(i) has repeating numbers")
            total += i
        }
    }
    return total
}

func iterRanges(_ ranges:[[Int]]) -> Int {
    var total:Int = 0
    for range in ranges {
        total += calculateInvalidIDs(range[0], range[1])
    }
    return total
}

let fileData:[[Int]] = try getFileData()
print("Test getFileData(): \(fileData)")
print()
print("Test 1188511885: \(hasRepeatingDigits(1188511885))")
print()
// print("Invalid ID Sum: \(iterRanges(fileData))")
// print("Test hasRepeatingDigits: \(hasRepeatingDigits(124232124232))")