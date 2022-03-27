class Stack:
    def __init__(self, income_list):
        self.income_list = income_list
    def isempty(self):
        if self.income_list == []:
            return True
        else:
            return False
    def __getitem__(self, item):
        return self.income_list[-1 - item]
    def push(self, item):
        return self.income_list.append(item)
    def __str__(self):
        return str(self.income_list)
    def pop(self):
        return self.income_list.pop()
    def peek(self):
        return self.income_list[-1]
    def size(self):
        return len(self.income_list)

def check(check_data):
    stack = Stack([])
    open_list = ['[','{','(']
    close_list = [']','}',')']
    for element in check_data:
        if element in open_list:
            stack.push(element)
        elif (element in close_list) and (stack.size() != 0):
            pos = close_list.index(element)
            if stack[0] == open_list[pos]:
                stack.pop()
            else:
               return print('NotBalanced')
        else:
            return print('NotBalanced')
    if stack.isempty():
        return print('OK')
    else:
        return print('NotBalanced')

if __name__ == "__main__":

    a = '[([])((([[[]]])))]{()}'
    check(a)