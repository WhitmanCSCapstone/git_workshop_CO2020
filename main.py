def main():
    # TODO Copy this line to call `print_file` on your own file.
    print_file('beszel.txt')

def print_file(path):
    f = open(path, 'r')
    for line in f:
        print(line, end='')

if __name__ == '__main__':
    main()
