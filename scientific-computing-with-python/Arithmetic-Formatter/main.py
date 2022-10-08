import sys
import arithmetic_arranger as arithmetics

def main():
    # Receive input from command line.
    input = sys.argv[1:]
    length = len(input)
    
    arithmetics.arithmetic_arranger(input)


if __name__ == "__main__":
    main()
