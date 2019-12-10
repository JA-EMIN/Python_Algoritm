# list 담긴 숫자를 모든 숫자를 더한다고 가정
# 1. list 내에 int형 정수 있다면 loop으로도 처리 가능
# 2. 하지만 list 내에 list 또는 tuple등의 data가 들어 올 수 있으므로 재귀함수로 처리

numbers = [10, (10, 20), [[[10, 9], 10], [10, 9]],30]

def SumOfNumbers(sum, array):
    if len(array) == 0:
        return sum
    else:
        if type(array[0]) == type(1):               #list의 첫번째 인자가 int라면
            sum += array[0]
        else:                                       #list의 첫번째 인자가 int가 아닐 때,
            sum += SumOfNumbers(0, array[0])        #재귀함수 호출하여 list 또는 tuple의 내부로 접근
        return SumOfNumbers(sum, array[1:])         #list의 다음 인자를 가르키도록하여 재귀함수 호출



print(SumOfNumbers(0, numbers))
