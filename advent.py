from input import inputValues

def main():
    print("welcome to the advent of code!!")
    
    # Day One: Puzzle One
    # frequency = 0
    # for value in inputValues:
    #     frequency += value
    # print(frequency)
    
    # Answer = 553

    # Day One: Puzzle Two
    frequencyList = []
    found = False
    frequency = 0
   
    while not found:
        for value in inputValues:

            if frequency in frequencyList:
                found = True
                print(frequency)
                break

            frequencyList.append(frequency)
            frequency += value
    #Answer: 78724
        



    




if __name__ == "__main__":
    main()