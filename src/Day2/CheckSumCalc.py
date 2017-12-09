import sys
import os

class CheckSumCalc:
    def GetDifference(self, input):
         maxValue = max(input)
         minValue = min(input)
         return int(maxValue) - int(minValue)
    
    def GetDifferencesOfDivisions(self, input):
        for idx, entry in enumerate(input):
            valueToCompare = entry
            for entry in input:
                if entry == valueToCompare:
                    continue
                elif entry > valueToCompare and entry % valueToCompare == 0:
                    return entry / valueToCompare
                elif entry < valueToCompare and valueToCompare % entry == 0:
                    return valueToCompare / entry

def ExtractPuzzleInput(file):
    PuzzleInput = []
    for line in file:
        lineToIntArray = list(map(int, line.split()))
        PuzzleInput.append(lineToIntArray)
    return PuzzleInput

def main():
    thisDir = os.path.dirname(__file__)
    absFilePath = os.path.join(thisDir, "bin/PuzzleInput.txt")
    file = open(absFilePath, "r")
   
    PuzzleInput = ExtractPuzzleInput(file)
    calc = CheckSumCalc()
    totalValue = 0
    for entry in PuzzleInput:
        totalValue += calc.GetDifference(entry)

    print(f"Puzzle input: \n{PuzzleInput}")
    print(f"\nTotal value of all differences within the spreadsheet: {totalValue}")
    totalValue = 0
    for entry in PuzzleInput:
        totalValue += calc.GetDifferencesOfDivisions(entry)

    print(f"Total value of all cleanly divisible differences within each row: {int(totalValue)}")
    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))