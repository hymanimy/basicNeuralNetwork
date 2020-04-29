import random
#check out assert and try, raise, valuerror

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        #the matrix data is stored in a 2d array
        self.m = [[0 for i in range(cols)] for j in range(rows)]

    def show(self):
        for i in range(self.rows):
            print(self.m[i])

    def __add__(self, other):
        #element-wise addition
        if(type(self) == type(other) and self.rows == other.rows and self.cols == other.cols):
            new = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new.m[i][j] = self.m[i][j] + other.m[i][j]
            return new
        elif(isinstance(other, int) or isinstance(other, float)):
            new = Matrix(self.rows, self.cols)
            for i in range(new.rows):
                for j in range(new.cols):
                    new.m[i][j] = self.m[i][j] + other
            return new
        else:
            print("Matrices must be of equivalent dimensions!")

    def __sub__(self, other):
        #element-wise addition
        if(type(self) == type(other) and self.rows == other.rows and self.cols == other.cols):
            new = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new.m[i][j] = self.m[i][j] - other.m[i][j]
            return new
        elif(isinstance(other, int) or isinstance(other, float)):
            new = Matrix(self.rows, self.cols)
            for i in range(new.rows):
                for j in range(new.cols):
                    new.m[i][j] = self.m[i][j] - other
            return new
        else:
            print("Matrices must be of equivalent dimensions!")

    def __mul__(self,other):
        #element-wise multiplication. commutative. can be done with another matrix or scalar
        if(type(self) == type(other) and self.rows == other.rows and self.cols == other.cols):
            new = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new.m[i][j] = self.m[i][j] * other.m[i][j]
            return new
        elif(isinstance(other, int) or isinstance(other, float)):
            new = Matrix(self.rows, self.cols)
            for i in range(new.rows):
                for j in range(new.cols):
                    new.m[i][j] = self.m[i][j] * other
            return new
        else:
            print("Matrices must be of equivalent dimensions!")

    def dot(self, other):
        #Proper matrix multiplication
        if(self.cols == other.rows):
            new = Matrix(self.rows, other.cols)
            #loop through each cell in matrix
            for i in range(new.rows):
                for j in range(new.cols):
                    for k in range(self.cols):
                        new.m[i][j] += self.m[i][k] * other.m[k][j]
            return new
        else:
            print("1st matrix must have same number of cols to 2nd's number of rows")

    def transpose(self):
        new = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new.m[j][i] = self.m[i][j]
        return new

    def rand(self):
        #fills the matrix randomly with values between 1 and -1
        for i in range(self.rows):
            for j in range(self.cols):
                self.m[i][j] = (random.random() * 2) - 1


    def apply(self, foo):
        #applies a function foo to every element in the matrix
        new = Matrix(self.rows, self.cols)
        for i in range(new.rows):
            for j in range(new.cols):
                new.m[i][j] = foo(self.m[i][j])
        return new

    def average(self):
        # Average error from the output vector, returned as float
        av = 0
        for i in range(self.rows):
            for j in range(self.cols):
                av  += self.m[i][j]
        av = av/(self.rows * self.cols)
        return av

def randMatrix(rows, cols):
    new = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            new.m[i][j] = (random.random() * 2) - 1
    return new

def listToMatrix(arr):
    # Converts a 1D list into a column vector
    new = Matrix(len(arr), 1)
    for i in range(new.rows):
        for j in range(new.cols):
            new.m[i][j] = arr[i]
    return new
