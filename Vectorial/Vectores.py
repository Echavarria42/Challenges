from math_basic import multiplicar

class Vector:

    def __init__(self, vector):
        self.dimension = len(vector)
        self.vector = vector
    
    def sum(self, vector):
        if self.dimension == vector.dimension:
            solution = [self.vector[i] + vector.vector[i] for i in range(self.dimension)]           
            return solution
    
    def subtract(self, vector):
        if self.dimension == vector.dimension:
            solution = [self.vector[i] - vector.vector[i] for i in range(self.dimension)]           
            return solution
    
    def dot_product(self, vector):
        solution = 0
        for i in range(self.dimension):
            solution += (multiplicar([self.vector[i], vector.vector[i]]))
        return solution  
    
    def mul_scalar(self, scalar):
        solution = [self.vector[i] * scalar for i in self.vector]
        return solution



if __name__ == '__main__':
    v_1 = Vector([1,1,1])
    v_2 = Vector([2,2,2])
    v_3 = Vector([3,3,3])


    print(v_1.sum(v_2))

