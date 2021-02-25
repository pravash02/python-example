"""
STACK

Stack is a linear data structure which follows a particular order in which the operations are performed.
The order may be LIFO(Last In First Out) or FILO(First In Last Out)

"""


class Stack:
    def __init__(self):
        self.stack_lst = []

    def is_empty(self):
        return len(self.stack_lst) == 0

    def is_empty_for_precedence(self):
        return True if self.peek() == -1 else False

    def push(self, item):
        self.stack_lst.append(item)

    def pop(self):
        if self.is_empty():
            return float("-inf")
        return self.stack_lst.pop()

    def get_stack(self):
        return self.stack_lst

    def get_stack_size(self):
        return len(self.stack_lst)

    def peek(self):
        if self.is_empty():
            return float("-inf")
        top_item = self.stack_lst[-1]
        return top_item

    @staticmethod
    def create_stack():
        input_lst = []
        return input_lst


class CheckParenthesis(Stack):
    def __init__(self):
        Stack.__init__(self)

    @staticmethod
    def check_balancing(p1, p2):
        if p1 == '(' and p2 == ')':
            return True
        elif p1 == '{' and p2 == '}':
            return True
        elif p1 == '[' and p2 == ']':
            return True
        else:
            return False

    def parenthesis_checking(self, p):
        balanced = True
        if len(p.strip()) == 0:
            return 'Enter a valid char'
        else:
            for i in p:
                if i in '({[':
                    self.push(i)
                else:
                    if self.is_empty():
                        balanced = False
                    else:
                        top = self.pop()
                        if not self.check_balancing(top, i):
                            balanced = False
        print balanced

    @staticmethod
    def count_reversal(char):
        lst_char = list(char)
        lst_start = []
        lst_end = []
        req_start_brc = 0
        req_end_brc = 0

        for i in lst_char:
            if i == '{':
                lst_start.append(i)
            else:
                lst_end.append(i)

        if len(lst_start) == 0 and len(lst_end) % 2 == 0:
            req_start_brc = len(lst_end)
        if len(lst_end) == 0 and len(lst_start) % 2 == 0:
            req_end_brc = len(lst_start)
        if len(lst_start) != 0 and len(lst_end) != 0:
            if len(lst_start) > len(lst_end):
                req_end_brc = abs(len(lst_start) - len(lst_end))
            else:
                req_start_brc = abs(len(lst_start) - len(lst_end))
        print "Required closing brackets -", req_end_brc, "Required starting brackets -", req_start_brc

    def count_reversal_1(self, char):
        lst_char = list(char)

        if len(char) % 2 != 0:
            print "Cannot be Balanced"

        for i in lst_char:
            if i == '{':
                self.push(i)
            else:
                if not self.is_empty():
                    pop = self.pop()

                    if self.check_balancing(pop, i):
                        continue
                else:
                    self.push(i)

        print self.stack_lst
        m = self.stack_lst.count('}')
        n = self.stack_lst.count('{')
        print (m+n)/2 + n % 2

    def count_reversal_2(self, char):
        lst_char = list(char)
        start_brc = 0
        end_brc = 0
        lst_end_brc = []

        for i in lst_char:
            if i == '{':
                self.push(i)
                if len(lst_end_brc) != 0:
                    lst_end_brc.append(i)
            else:
                if not self.is_empty():
                    pop = self.pop()
                    if not self.check_balancing(pop, i):
                        continue
                    else:
                        lst_end_brc.pop()
                else:
                    lst_end_brc.append(i)

        if len(lst_end_brc) == 0:
            if self.stack_lst.count('{') % 2 == 0:
                end_brc = self.stack_lst.count('{') / 2

        if self.stack_lst.count('{') == 0:
            if len(lst_end_brc) % 2 == 0:
                start_brc = len(lst_end_brc) / 2

        if len(lst_end_brc) != 0:
            print lst_end_brc
            if lst_end_brc.count('{') > lst_end_brc.count('}'):
                print "Total brackets both start and end - ", lst_end_brc.count('{')
            elif lst_end_brc.count('}') > lst_end_brc.count('{'):
                print "Total brackets both start and end - ", lst_end_brc.count('}')
            elif lst_end_brc.count('}') == lst_end_brc.count('{'):
                if lst_end_brc.count('}') == lst_end_brc.count('{') != 1:
                    print "Total brackets both start and end - ", (lst_end_brc.count('}') + lst_end_brc.count('{')) / 2
                else:
                    print "Total brackets both start and end - ", lst_end_brc.count('}') + lst_end_brc.count('{')

        print "Required start brackets to balance -", start_brc
        print "Required end brackets to balance -", end_brc


class ConvertToBinary(Stack):
    def __init__(self):
        Stack.__init__(self)

    def binary_conversion(self, num):
        binary_str = ''
        while num != 0:
            res = num % 2
            self.push(res)
            num = num / 2

        while len(self.stack_lst) != 0:
            binary_str += str(self.pop())

        # print ''.join(str(i) for i in self.stack_lst[::-1])
        print binary_str


class InfixPostfix(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.result = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    @staticmethod
    def check_operand(char):
        return char.isalpha()

    def check_precedence(self, operator):
        try:
            pc = self.precedence[operator]
            pct = self.precedence[self.peek()]
            return True if pc <= pct else False
        except KeyError:
            return False

    def convert_to_postfix(self, char):
        for i in char:
            if self.check_operand(i):
                self.result.append(i)
            elif i == "(":
                self.push(i)
            elif i == ")":
                while (not self.is_empty()) and (self.peek() != "("):
                    cpop = self.pop()
                    self.result.append(cpop)
                if (not self.is_empty()) and (self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.is_empty()) and (self.check_precedence(i)):
                    cpop = self.pop()
                    self.result.append(cpop)
                self.push(i)

        while not self.is_empty():
            self.result.append(self.pop())

        print "".join(self.result)


class PostfixInfix(Stack):
    def __init__(self):
        Stack.__init__(self)

    @staticmethod
    def check_operand(char):
        return char.isalpha()

    def convert_to_infix(self, ch):
        for c1 in ch:
            if self.check_operand(c1):
                self.push(c1)
            else:
                pop1 = self.pop()
                pop2 = self.pop()
                val = "(" + pop2 + c1 + pop1 + ")"
                self.push(val)
        print self.stack_lst


class NextGreater(Stack):
    def __init__(self):
        Stack.__init__(self)

    def get_next_greater_elem(self, lst):
        dict_elem = {}
        for i in lst[::-1]:
            self.push(i)

        while not self.is_empty():
            pop = self.pop()
            if self.get_stack_size() == 0:
                dict_elem.update({pop: -1})
                break
            for i in lst:
                if pop == max(lst):
                    dict_elem.update({pop: -1})
                    break
                if pop == i:
                    continue
                if pop < i:
                    if i in self.stack_lst:
                        dict_elem.update({pop: i})
                        break
        print dict_elem

    def check_nxt_greater(self, lst):
        self.push(lst[0])

        for i in lst:
            temp = i

            if not self.is_empty():
                pop = self.pop()

                while pop < temp:
                    print(str(pop) + " -- " + str(temp))
                    if self.is_empty():
                        break
                    pop = self.pop()
                if pop > temp:
                    self.push(pop)
            self.push(temp)

        while not self.is_empty():
            pop = self.pop()
            tmp = -1
            print(str(pop) + " -- " + str(tmp))


class ReverseWords(Stack):
    def __init__(self):
        Stack.__init__(self)

    def reverse_individual_words(self, words):
        lst = [words]
        op_lst = []

        for i in range(0, len(lst)):
            vl = list(lst[i])
            for j in vl:
                self.push(j)

        print self.stack_lst
        while not self.is_empty():
            op_lst.append(self.pop())
        print "".join(op_lst)


class Sorting(Stack):
    def __init__(self):
        Stack.__init__(self)

    def sort_in_ascending_order(self, lst):
        temp_stack = Stack.create_stack()
        for i in lst:
            self.push(i)

        if len(self.stack_lst) == 1:
            print "Only element in stack - ", self.peek()

        while not self.is_empty():
            pop = self.pop()

            while len(temp_stack) != 0 and pop > temp_stack[-1]:
                val = temp_stack.pop()
                self.push(val)
            temp_stack.append(pop)
        print temp_stack

    def do_recursion(self, stack):
        if self.is_empty():
            return stack
        temp = self.pop()
        self.do_recursion(stack)
        self.insert_in_last(stack, temp)

        print stack

    def insert_in_last(self, stack, temp):
        if len(stack) == 0 or temp > stack[-1]:
            stack.append(temp)
            return

        x = stack.pop()
        self.insert_in_last(stack, temp)
        stack.append(x)

    def sort_using_recursion(self, lst):
        for i in lst:
            self.push(i)
        print self.stack_lst

        self.do_recursion(self.stack_lst)


class RemoveMiddleElement(Stack):
    def __init__(self):
        Stack.__init__(self)

    def remove_middle_item(self, lst):
        for i in lst:
            self.push(i)

        n = len(lst) / 2
        tmp_lst = []
        count = len(lst)
        while not self.is_empty():
            count -= 1
            pop = self.pop()
            if n == count:
                pass
            else:
                tmp_lst.append(pop)
        print tmp_lst


class ChecklongestSubstring(Stack):
    def __init__(self):
        Stack.__init__(self)

    def chk_longest_substr(self, lst):
        result = 0
        self.push(-1)

        for i in xrange(len(lst)):
            if lst[i] in "({[":
                self.push(i)
            else:
                print self.stack_lst, i, self.peek()
                self.pop()
                if not self.is_empty():
                    result = max(result, i - self.peek())
                if self.is_empty():
                    self.push(i)
        print result


class ReverseStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def rev_stack(self, stack):
        if self.is_empty():
            return stack
        temp = self.pop()
        self.rev_stack(stack)
        self.insert_stack_at_bottom(stack, temp)

        print stack

    def insert_stack_at_bottom(self, stack, temp):
        if len(stack) == 0:
            stack.append(temp)
            return
        x = stack.pop()
        self.insert_stack_at_bottom(stack, temp)
        stack.append(x)

    def reverse_stack(self, lst):
        for i in lst:
            self.push(i)
        print self.stack_lst
        self.rev_stack(self.stack_lst)


class TowerOfHanoi(Stack):
    def __init__(self):
        Stack.__init__(self)

    @staticmethod
    def move_to_poles(source, destination):

        if len(source) == 0:
            pop2 = destination.pop()
            source.append(pop2)
            return source, destination

        if len(destination) == 0:
            pop = source.pop()
            destination.append(pop)
            return source, destination

        if len(source) != 0 and len(destination) != 0:
            pop = source.pop()
            pop2 = destination.pop()
            if pop > pop2:
                source.append(pop)
                source.append(pop2)
                return source, destination
            else:
                destination.append(pop2)
                destination.append(pop)
                return source, destination

    def get_toh_function(self, lst):
        axillary_lst = []
        destination_lst = []
        no_of_moves = pow(2, len(lst)) - 1

        dict_poles = {'A': axillary_lst, 'D': destination_lst, 'S': self.stack_lst}

        if len(lst) % 2 == 0:
            temp = dict_poles['D']
            dict_poles.update({'D': dict_poles['A']})
            dict_poles.update({'A': temp})

        for i in lst[::-1]:
            self.push(i)

        source_st = self.stack_lst
        print source_st

        for i in range(1, no_of_moves+1):
            if i % 3 == 1:
                source, destination = self.move_to_poles(source_st, dict_poles['D'])
                dict_poles.update({'D': destination})
                print dict_poles, i, source
            if i % 3 == 2:
                source, destination = self.move_to_poles(source_st, dict_poles['A'])
                dict_poles.update({'A': destination})
                print dict_poles, i
            if i % 3 == 0:
                source, destination = self.move_to_poles(dict_poles['A'], dict_poles['D'])
                dict_poles.update({'A': source})
                dict_poles.update({'D': destination})
                print dict_poles, i

        print dict_poles['D']


class MaxStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def get_max_stack(self, lst):
        print lst
        max_ = -1

        self.push(max_)

        for i in lst:
            if i > self.pop():
                max_ = i
                self.push(max_)

        print self.stack_lst


class EvaluateExpression(Stack):
    def __init__(self):
        Stack.__init__(self)

    def get_evaluated_value(self, lst):
        print lst
        expression_lst = []
        arithmetic_lst = ['+', '-', '*', '/']
        result = ''

        for i in range(0, len(lst)):
            if lst[i] in arithmetic_lst:
                if not self.is_empty():
                    pop1 = self.pop()
                    pop2 = self.pop()
                    self.push(eval(str(pop2)+lst[i]+str(pop1)))
                else:
                    self.push(lst[i])
            else:
                self.push(lst[i])
        print self.pop()


class SpecialStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def get_special_stack(self, lst):
        min_val = -1
        aux_lst = []

        for i in lst:
            if self.is_empty():
                self.push(i)
                aux_lst.append(i)
                min_val = i
            else:
                self.push(i)
                aux_lst.append(min_val)
                pop = aux_lst.pop()
                if i < pop:
                    min_val = i
                    aux_lst.append(min_val)
                else:
                    aux_lst.append(min_val)

        print self.stack_lst
        print aux_lst


class ImmediateSmaller(Stack):
    def __init__(self):
        Stack.__init__(self)

    def get_immediate_smaller(self, lst):
        self.push(-1)
        for i in lst[::-1]:
            self.push(i)

        for i in lst:
            while not self.is_empty():
                self.pop()
                top = self.peek()

                if i > top:
                    print "next smaller of ", i, "----->", top
                else:
                    print "next smaller of ", i, "----->", -1
                break

        print self.stack_lst


if __name__ == '__main__':
    s = Stack()
    # c = CheckParenthesis()
    # c.parenthesis_checking('({[]})')      # IMP
    # c.count_reversal('}{{}}{{{')
    # c.count_reversal_1('}{{}}{{{')
    # c.count_reversal_2('}{{}}{{{')
    # ctb = ConvertToBinary()
    # ctb.binary_conversion(242)
    # ip = InfixPostfix()
    # ip.convert_to_postfix("A+B*C-(D/E+F*G*H)")
    # ip.convert_to_postfix("A+B*(C-D/)")
    # pi = PostfixInfix()
    # pi.convert_to_infix("ab*c+d*e/")
    # ng = NextGreater()
    # ng.get_next_greater_elem([11, 13, 21, 3, 5])      # IMP
    # ng.check_nxt_greater([11, 13, 21, 3, 5])
    # rw = ReverseWords()
    # rw.reverse_individual_words("google amazon")
    # sa = Sorting()
    # sa.sort_using_recursion([45, 8, 52])
    # sa.sort_in_ascending_order([11, 5, 15, 45, 3])
    # rm = RemoveMiddleElement()
    # rm.remove_middle_item([1, 2, 3, 4, 5, 6, 7])
    # cls = ChecklongestSubstring()
    # cls.chk_longest_substr("()(()))))")
    # rs = ReverseStack()
    # rs.reverse_stack([3, 2, 1])
    # toh = TowerOfHanoi()
    # toh.get_toh_function([1, 2, 3])
    # ms = MaxStack()
    # ms.get_max_stack([2, 5, 1, 8, 5, 9])
    # ee = EvaluateExpression()
    # ee.get_evaluated_value(["4", "13", "5", "/", "+"])
    # ss = SpecialStack()
    # ss.get_special_stack([18, 19, 29, 15, 16])
    # ims = ImmediateSmaller()
    # ims.get_immediate_smaller([5, 6, 2, 3, 1, 7])
