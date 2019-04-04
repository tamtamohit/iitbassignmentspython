from ops import sum_of, sub_of, mult_of, div_of, sum_all


class Question4:
    def __init__(self):
        try:
            number_of_iterations = int(input("Number of test cases: "))
        except:
            return print('Use integer value.')
        results = []
        for iteration in range(number_of_iterations):
            results.append(self.start(input()))
        for result in results:
            print(result)

    def start(self, param):
        elem = param.rstrip().split(' ')
        airth_operation = elem.pop(0)
        # remove space from end

        for n, i in enumerate(elem):
            try:
                elem[n] = float(i)
            except ValueError:
                return 'Please enter a float type variable.'

        if airth_operation == '+':
            if self.check_length(elem):
                return sum_of(elem)
        elif airth_operation == '-':
            if self.check_length(elem):
                return sub_of(elem)
        elif airth_operation == '*':
            if self.check_length(elem):
                return mult_of(elem)
        elif airth_operation == '/':
            if self.check_length(elem):
                return div_of(elem)
        elif airth_operation == '$':
            return sum_all(elem)
        else:
            return 'Error with airthmatic operator'
        return 'Too many values to unpack'

    def check_length(self, elem):
        '''
        check if list has length of 2
        :param elem: list of floating type variable
        :return: bool
        '''
        if len(elem) == 2:
            return True
        else:
            return False


if __name__ == '__main__':
    ob = Question4()
