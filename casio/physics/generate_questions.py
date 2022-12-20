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


def main():
    while True:
        question = input('q: ')
        a = input('a: ')
        b = input('b: ')
        c = input('c: ')
        d = input('d: ')

        choices = {'A': a, 'B': b, 'C': c, 'D': d}


if __name__ == '__main__':
    main()