class Question2BracketsMatch:
    def __init__(self):
        try:
            number_of_iterations = int(input("Number of test cases: "))
        except:
            return print('Use integer value.')
        self.open_dict = {'{': 1, '[': 1, "(": 1}
        self.close_dict = {'}': '{', ']': "[", ")": "("}
        results = []
        for iteration in range(number_of_iterations):
            results.append(self.check_brackets(input()))
        for result in results:
            print(result)

    def check_brackets(self, param):
        check_list = []
        for word in param:
            if word in self.open_dict.keys():
                check_list.append(word)
            elif word in self.close_dict.keys():
                if len(
                    check_list) == 0: return 'No'  # If string starts with closing bracket
                                                   # or checklist has no element
                if check_list[-1] == self.close_dict[word]:
                    check_list.pop(-1)
                else:
                    return 'No'
        if len(check_list) == 0:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    ob = Question2BracketsMatch()
