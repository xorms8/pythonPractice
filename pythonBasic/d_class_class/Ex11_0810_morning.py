# 1. 다음 코드를 람다 함수 형태로 수정할 때, 알맞은 코드를 작성하시오.
# def f(x, y):
# return x ** y
#

(lambda x,y : x ** y)


# 2. 다음과 같이 리스트 컴프리헨션으로 되어 있는 코드를 람다(lambda) 함수와 map() 함수를 사용하여 표현하시오.
# >>> ex = [1, 2, 3, 4, 5]
# >>> [value **2 for value in ex]
# [1, 4, 9, 16, 25]
ex = [1,2,3,4,5]
result=list(map(lambda x : x**2, ex ))
print(result)

#
# 3. 다음과 같이 코드를 작성했을 때, 예측되는 실행 결과를 쓰시오.
# >>>def transpose_list(two_dimensional_list):
# ... return [row for row in zip(*two_dimensional_list)]
# ...
# >>>transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
#
[(1,2,3), (4,5,6) ,(7,8,9,)]


# 4. 다음 코드의 실행 결과를 쓰시오.
date_info = {'year': "2019", 'month': "9", 'day': "6"}
result = "{year}-{month}-{day}".format(**date_info)
print(result)
# 2019 - 9 - 6




# 5. n개의 벡터의 크기가 동일한지 확인하는 함수를 한 줄의 코드로 작성하시오.


def vector_size_check(a_value, b_value, c_value):
    if len(a_value) == len(b_value) and len(b_value) == len(c_value) and len(a_value) == len(c_value):
        return True
    else:
        return False
'''
vector_size_check = lambda x,y,z: (True if len(x)==len(y) and len(y)==len(z) else False)
'''

a = (1, 2, 3)
b = (4, 5, 6)
c = (6, 7, 9)

print(vector_size_check(a,b,c))        # True

a=(1,2,3)
b=(4,5,6)
c=(6,7)
print(vector_size_check(a,b,c))        # False



#
#
#
#
# 6. 다음과 같이 2개 이상의 행렬을 더하는 코드를 작성하시오.[ 답제공 ]
# def matrix_addition(*matrix_variables):
# ... return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]
#
# >>>matrix_y = [[2, 5], [2, 1]]
# >>>matrix_z = [[2, 4], [5, 3]]
# >>>matrix_addition(matrix_y, matrix_z)
# [[4, 9], [7, 4]]
