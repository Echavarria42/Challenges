from Vectors import Vector


class Matriz:

    def __init__(self, matriz):
        self.dimension = len(matriz)
        self.matriz = matriz
    
    def sum(self, matriz):
        solution = [Vector(self.matriz[i]).sum(  Vector(matriz.matriz[i])  ) for i in range(self.dimension)]
        return solution
    
    def subtract(self, matriz):
        solution = [Vector(self.matriz[i]).subtract(  Vector(matriz.matriz[i])  ) for i in range(self.dimension)]
        return solution


    def mul_scalar(self, escalar):
        solution = [ Vector(i).mul_scalar(escalar) for i in self.matriz]
        return solution  

if __name__ == '__main__':
    
    m_1 = Matriz([[1,1,1],[1,1,1],[1,1,1]])
    m_2 = Matriz([[2,2,2],[2,2,2],[2,2,2]])
    m_3 = Matriz([[3,3,3],[3,3,3],[3,3,3]])

    print(m_1.sum(m_1))