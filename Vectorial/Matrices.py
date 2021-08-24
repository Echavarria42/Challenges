from Vectores import Vector


class Matriz:

    def __init__(self, matriz):
        self.dimencion = len(matriz)
        self.matriz = matriz
    
    def sumar(self, matriz):
        solution = [Vector(self.matriz[i]).sumar(  Vector(matriz.matriz[i])  ) for i in range(self.dimencion)]
        return solution
    
    def restar(self, matriz):
        solution = [Vector(self.matriz[i]).restar(  Vector(matriz.matriz[i])  ) for i in range(self.dimencion)]
        return solution


    def mul_escalar(self, escalar):
        solution = [ Vector(i).mul_escalar(escalar) for i in self.matriz]
        return solution  

if __name__ == '__main__':
    
    m_1 = Matriz([[1,1,1],[1,1,1],[1,1,1]])
    m_2 = Matriz([[2,2,2],[2,2,2],[2,2,2]])
    m_3 = Matriz([[3,3,3],[3,3,3],[3,3,3]])

    print(m_1.sumar(m_1))