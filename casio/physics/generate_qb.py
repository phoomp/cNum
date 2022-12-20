class Question:
    def __init__(self, question, choices, answer=None):
        self.question = question
        self.choices = choices
        self.answer = answer

    def __str__(self):
        str_to_return = f'''
        {"{"}
            "question": "{self.question}",
            "choices": {str(self.choices)},
            "answer": "{str(self.answer)}"
        {"},"}
        '''
        return str_to_return


def write_question(q):
    q = str(q)
    with open('output.txt', 'a+') as file:
        file.write(q)


def new_question(line):
    try:
        a = int(line[0])
        assert '.' in line
        assert line.split('.')[1][0] == ' '
        # assert line[2] == ' '
        return True
    except Exception as e:
        return False


def main():
    current = 'question'
    questions = []
    question = ''
    choices = {}

    with open('raw.txt', 'r') as f:
        for line in f:
            line = line.replace('Turn over', '')
            line = ' '.join(line.split('\n'))
            line = line.replace('\t', ' ')
            line = ' '.join(line.split())

            line_heading = line.split('.')[0]
            print(line_heading)
            if line_heading == 'A' or line_heading == 'B' or line_heading == 'C' or line_heading == 'D':
                current = line_heading
            else:
                current = 'question'

            if new_question(line):
                if question != '':
                    q = Question(question, choices)
                    # print(q)
                    questions.append(q)
                    question = ''
                    choices = {}
                question += ' '.join(line.split()[1:])

            else:
                if current == 'question':
                    question += line
                else:
                    if current in choices:
                        choices[current] += line
                    else:
                        choices[current] = line

    q = Question(question, choices)
    questions.append(q)

    for q in questions:
        print(q)

    with open('ans_raw.txt', 'r') as f:
        answers = f.read().replace(' ', '').split()
        print(f'Q: {len(questions)}')
        print(f'A: {len(answers)}')
        assert len(answers) == len(questions)
        print('Check passed! Writing files...')

        for i, q in enumerate(questions):
            a = answers[i]
            q.answer = a
            write_question(q)


if __name__ == '__main__':
    main()