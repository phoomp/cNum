dependencies = [
    'core/equations.py',
    'core/fractions.py',
    'core/terms.py'
]

target = 'bin/coefficient_by_index.py'
output = 'output.py'


def compile_and_save():
    text_to_write = []

    for d in dependencies:
        with open(d, 'r') as f:
            lines = f.readlines()
            gathering = False
            for line in lines:
                if 'BEGIN GATHER' in line:
                    gathering = True

                if 'END GATHER' in line:
                    gathering = False

                if gathering:
                    text_to_write.append(line)

    with open(target, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'BEGIN GATHER' in line:
                gathering = True

            if gathering:
                text_to_write.append(line)

            if 'END GATHER' in line:
                gathering = False

    with open(output, 'w') as out:
        text_to_write = '\n'.join(text_to_write)
        out.write(text_to_write)


def main():
    confirmation = input('Are you sure you want to proceed? ')
    if 'y' in confirmation.lower():
        compile_and_save()
    else:
        exit(0)


if __name__ == '__main__':
    main()