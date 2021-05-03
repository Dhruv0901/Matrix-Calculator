"""
This is the class file of Matrix operations. This class file contains functions
for addition, subtraction, multiplication, scalar multiplication, formation of matrix and
formation of identity matrix.
"""

menu = """
\t\tMENU\n
\t1. Addition
\t2. Subtraction
\t3. Multiplication
\t4. Scalar Multiplication\n
"""


class MatrixOperation:

    def __init__(self):

        """global variables"""

        self.raw_matrix = []  # main matrix container
        self.I_raw_matrix = []  # main matrix container for identity matrix
        self.operational_matrix = []  # the matrix formed after applying operation
        self.column_elements = []  # list to store column elements

    def add(self, matrix1, matrix2):
        """
            :param: matrix1
            :return: addition of matrix1 && matrix2
            :argument: lists as matrix
        """

        for i in range(len(matrix1)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)  # print statement for testing

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(matrix1):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
                sum = matrix1[counter_index][counter_var2] + matrix2[counter_index][counter_var2]
                self.operational_matrix[counter_index].append(sum)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def subtract(self, matrix1, matrix2):
        """
            :param: matrix1
            :return: subtraction of matrix1 && matrix2
            :argument: lists as matrix
        """

        for i in range(len(matrix1)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)  # print statement for testing

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(matrix1):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
                difference = matrix1[counter_index][counter_var2] - matrix2[counter_index][counter_var2]
                self.operational_matrix[counter_index].append(difference)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def scalar_multiply(self, integer, matrix):
        """
            :param: integer && matrix1
            :return: product of matrix with interger
            :argument: lists as matrix
        """

        # if matrix is None:
        #     matrix = list()
        for i in range(len(matrix)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(matrix):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix[0]):  # while loop to add elements as/in the columns
                product = matrix[counter_index][counter_var2] * integer
                self.operational_matrix[counter_index].append(product)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def multiply(self, matrix1, matrix2):
        """
            :param: matrix1
            :return: multiplication of matrix1 && matrix2
            :argument: lists as matrix
        """

        col_elements = Matrix().__getColumnElements__(matrix2)

        for i in range(len(matrix1)):
            self.operational_matrix.append([])

        """code to the product matrix"""

        counter_var1 = 0

        while counter_var1 < len(matrix1)+len(matrix2[0]):
            counter_var2 = 0
            product_store = []

            while counter_var2 < len(matrix2[0]):
                elements = matrix1[None][None] * col_elements[None][None]
                product_store.append(elements)

            self.operational_matrix[None][None].append(sum(product_store))

            """
            NOTE:- This function is incomplete. You can only use other function and operations.
            """

        return self.operational_matrix


class Matrix(MatrixOperation):

    def __init__(self):  # function to initialize current class

        MatrixOperation.__init__(self)  # statement to initialize MatrixOperation class

        """global variables"""

        self.raw_matrix = []  # main matrix container
        self.I_raw_matrix = []  # main matrix container for identity matrix
        self.column_elements = []  # list to store column elements

    def __formMatrix__(self, rows=int(), cols=int(), type=None):  # function to make matrix with 2 integer parameters
        """
            :param: rows && columns
            :return: matrix of M(rows) x N(columns)
            :argument: int
        """

        for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
            self.raw_matrix.append([])

        counter_index = 0  # counter value for first while loop
        counterRowNum = 1  # counter value for row no. in message

        """while loop for putting elements in the matrix"""

        while counter_index < rows:
            counter_var2 = 1  # counter value for nested while loop

            while counter_var2 <= cols:  # while loop to add elements as/in the columns
                col_elements = eval(input(f'Enter element a{counterRowNum}{counter_var2}: '))  # variable to store user's input element
                # col_elements = 5  # statement for testing the function
                self.raw_matrix[counter_index].append(col_elements)
                counter_var2 += 1

            counter_index += 1
            counterRowNum += 1

        return self.raw_matrix

    def __getMatrix__(self, matrix):  # function to print the formed matrix in a matrix format
        """
        :param: matrix
        :return: list (final matrix) in matrix format
        :argument: list as matrix
        """

        print('Your Matrix:-')

        for i in matrix:  # for loop to read the main matrix container

            for j in i:  # for loop to read and print the rows and columns
                print(f'\t{j}', end='')

            print()  # print statement to add new empty line

    def __identityMatrix__(self, rows=int(), cols=int()):
        """
            :param: rows && cols
            :return: Identity matrix
            :argument: int
        """

        for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
            self.I_raw_matrix.append([])

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < rows:
            counter_var2 = 1  # counter value for nested while loop

            while counter_var2 <= cols:  # while loop to add elements as/in the columns
                self.I_raw_matrix[counter_index].append(0)
                counter_var2 += 1

            counter_index += 1

        # print(self.I_raw_matrix)

        """resetting the counter values"""

        counter_var2 = 1
        counter_index2 = 0

        """while loop for putting 1 in the identity matrix"""

        while counter_var2 <= cols:  # while loop to add elements as/in the columns
            self.I_raw_matrix[counter_index2][counter_index2] = 1
            counter_index2 += 1
            counter_var2 += 1

        return self.I_raw_matrix
        # print(self.I_raw_matrix)

    def __getColumnElements__(self, matrix):
        """
        :param: matrix
        :return: list of column elements
        :argument: list as matrix
        """

        for i in range(len(matrix[0])):  # for loop to make a list to store column elements
            self.column_elements.append([])
        # print(self.column_elements)  # statement for testing

        """code to store column elements"""

        counter_var = 0
        
        while counter_var < len(self.column_elements):
            counter_index = 0

            while counter_index < len(matrix[0]):

                col_element = matrix[counter_index][counter_var]
                self.column_elements[counter_var].append(col_element)
                counter_index += 1

            counter_var += 1

        return self.column_elements

    def __getProperties__(self, matrix):
        """
        :param: matrix
        :return: properties of matrix in dictionary
        :argument: list as matrix
        """

        return {'rows': len(matrix), 'cols': len(matrix[0]),
                'order': f'{len(matrix)}x{len(matrix[0])}',
                'size': len(matrix)*len(matrix[0])}
