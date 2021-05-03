"""
1. This is a matrix calculator. Just solve your matrix problems in 3 easy steps:-

    optional step: Enter the formula in which you want to solve those matrix Q.s
    step 1: Enter the order of that matrix
    step 2: Enter the elements of that matrix
    step 3: Enter the operation you want to perform on that matrices

2. All the operations are there in the form of functions in MatrixOperation class.
3. The code for that MatrixOperation class is there in a different python file and
    here that class is imported using static import.
"""

from Personal_Projects.Matrix_calculator.matrix_class import Matrix, menu


def __init_matrix__():
    counterVar1 = 1  # counter value for wile loop and matrix message

    while counterVar1 <= 2:

        print(f'Matrix {counterVar1}:-\n')
        rows = int(input('Enter the no. of rows:- '))
        cols = int(input('Enter the no. columns:- '))
        print()

        if counterVar1 == 1:

            matrix1 = Matrix().__formMatrix__(rows, cols)
            # print(matrix1)
            Matrix().__getMatrix__(matrix1)
            print()

        elif counterVar1 == 2:
            matrix2 = Matrix().__formMatrix__(rows, cols)
            # print(matrix2)
            Matrix().__getMatrix__(matrix2)
            print()

        counterVar1 += 1

if __name__ == '__main__':

    while True:
        matrix1 = None
        matrix2 = None

        print('what operation you want to perform on these matrices?\n\n')
        print(menu)
        operationChoice = int(input('Enter your choice no.:- '))

        if operationChoice == 1:

            __init_matrix__()

            POM1 = Matrix().__getProperties__(matrix1)
            POM2 = Matrix().__getProperties__(matrix2)

            if POM1['order'] == POM2['order']:

                addOut = Matrix().add(matrix1, matrix2)
                Matrix().__getMatrix__(addOut)

            else:
                # raise IndexError
                print('Order of both the matrices are not same.\n'
                      'To perform addition, order of both the matrices must be same')

        elif operationChoice == 2:
            
            __init_matrix__()

            POM1 = Matrix().__getProperties__(matrix1)
            POM2 = Matrix().__getProperties__(matrix2)

            if POM1['order'] == POM2['order']:

                subOut = Matrix().subtract(matrix1, matrix2)
                Matrix().__getMatrix__(subOut)

            else:
                # raise IndexError
                print('Order of both the matrices are not same.\n'
                      'To perform subtraction, order of both the matrices must be same')

        elif operationChoice == 3:

            __init_matrix__()

            multiOut = Matrix().multiply(matrix1, matrix2)
            Matrix().__getMatrix__(multiOut)

        elif operationChoice == 4:

            print(f'Matrix:-\n')
            rows = int(input('Enter the no. of rows:- '))
            cols = int(input('Enter the no. columns:- '))
            print()

            matrix = Matrix().__formMatrix__(rows, cols)
            # print(matrix1)
            Matrix().__getMatrix__(matrix1)
            print()

            sMultiOut = Matrix().scalar_multiply(None, matrix)
            Matrix().__getMatrix__(sMultiOut)

        else:
            print('No such choice available in the menu')
