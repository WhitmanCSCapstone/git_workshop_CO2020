import os

cheat = True

def main():
    if (cheat):
        print_file('beszel.txt')
        for file in os.listdir():
            if file.endswith(".txt") and file != 'beszel.txt':
                print_file(file)
        return
    # Part 5: Copy this line to call `print_file` on your own file.
    print_file('beszel.txt')
    print_file('abbey.txt')
    print_file('ChrisPyles.txt')
    print_file('leaf.txt')
    print_file('owen.txt')
    print_file('Yeon.txt')

def print_file(path):
    f = open(path, 'r')
    for line in f:
        print(line, end='')

if __name__ == '__main__':
    main()
