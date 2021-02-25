import random


class CodeBreaker:

    @staticmethod
    def generate_code():
        code = [i for i in range(1, 10)]
        random.shuffle(code)
        rnd_code = "".join(str(i) for i in code[:3])
        return rnd_code

    @staticmethod
    def get_user_guess(comp_code, user_code):

        if comp_code == user_code:
            res = 'CODE CRACKED'
            return res

        lst = []

        for ind, val in enumerate(user_code):
            if val == comp_code[ind]:
                lst.append('match')
            elif val in comp_code:
                lst.append('close')
            else:
                lst.append('nope')
        return lst


if __name__ == '__main__':
    print('Welcome to code breaker')
    computer_generated_code = CodeBreaker.generate_code()
    user_guess = input("please enter your 3-digit code")

    result = CodeBreaker.get_user_guess(computer_generated_code, user_guess)

    while result != 'CODE CRACKED':
        print(result)
        user_guess = input("please enter your 3-digit code")
        result = CodeBreaker.get_user_guess(computer_generated_code, user_guess)
        print(result)

