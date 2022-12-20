import glob


def main():
    for file in glob.glob('*'):
        if file.split('.')[-1] != 'txt' or not file[0].isnumeric():
            continue

        with open(file, 'r') as f:
            content = f.read()

        with open('s.py', 'a+') as f:
            f.write(content)


if __name__ == '__main__':
    main()
