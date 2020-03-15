class Matrix:
    def __init__(self,rows):
        if(type(rows) is str):
            r = []
            for j in rows.split('\n'):
                if(j!=''):
                    r.append([float(i) for i in j.split(' ') if(i!='')])
            self.rows = r
            for j in r:
                for i in j:
                    if(not i.is_integer()):
                        break
            else:
                self.rows = [[int(i) for i in j] for j in r]
        else:
            self.rows = rows

        self.m = len(self.rows)
        self.n = min([len(j) for j in self.rows])
        self.rows = [[Ai for i,Ai in enumerate(j) if(i<self.n)] for j in self.rows]

    
    def __getitem__(self, index):
        if(type(index) is tuple):
            j,i = index
            return self.rows[j][i]
        else:
            return self.rows[index]

    def __setitem__(self, index, item):
        if(type(index) is tuple):
            j,i = index
            self.rows[j][i] = item
        else:
            self.rows[index] = item
    
    def __repr__(self):
        return '\n'.join([','.join([str(i) for i in j]) for j in self])

    def __len__(self):
        return len(self.rows)


    @property
    def determinant(self):
        return NotImplementedError

    @property
    def d(self):
        return self.determinant

    ##Binary Operators##
    def __add__(self,other):
        if(type(other) is int):
            return Matrix([
                [i+other for i in j] for j in self.rows
            ])
        if(type(other) is Matrix):
            return Matrix([
                [Ai+other.rows[j][i] for i,Ai in enumerate(Aj)] for j,Aj in enumerate(self.rows)
            ])

    def __sub__(self,other):
        return self + other * -1

    def __mul__(self,other):
        if(type(other) is int or type(other) is float):
            return Matrix([
                [i*other for i in j] for j in self.rows
            ])
        
        if(type(other) is Matrix):
            result = []
            for j in range(len(self.rows)):
                subResult = []
                for i in range(len(other.rows[0])):
                    sum = 0
                    for k in range(len(self.rows[0])):
                        sum += self.rows[j][k] * other.rows[k][i]
                    subResult.append(sum)
                result.append(subResult)
            return Matrix(result)

    def __truediv__(self,other):
        if(type(other) is int or type(other) is float):
            return self * (1/other)


    def __floordiv__(self,other):
        if(type(other) is int or type(other) is float):
            return Matrix([
                [(i*1/other)//1 for i in j] for j in self.rows
            ])

    def __mod__(self,other):
        if(type(other) is int or type(other) is float):
            return Matrix([
                [i%other for i in j] for j in self.rows
            ])

    def __pow__(self,other):
        result = self
        for i in range(other):
            result = result*self
        return result


    ##Unary Operators#
    def __neg__(self):
        return Matrix([
                [-i for i in j] for j in self.rows
            ])

    def __pos__(self):
        return self

    def __invert__(self):
        inverted = [[] for _ in range(len(self.rows[0]))]
        for j,Aj in enumerate(self.rows):
            for i,Ai in enumerate(Aj):
                inverted[i].append(Ai)
        return Matrix(inverted)

    ##Assignment
    def __iadd__(self,other):
        return self + other
    def __isub__(self,other):
        return self - other
    def __imul__(self,other):
        return self * other
    def __idiv__(self,other):
        return self / other
    def __ifloordiv__(self,other):
        return self // other
    def __imod__(self,other):
        return self % other
    def __ipow__(self,other):
        return self ** other

    #Comparasion
    def __eq__(self,other):
        if(type(other) is Matrix):
            if(self.m == other.m and self.n == other.n):
                for j,Aj in enumerate(self.rows):
                    for i,Ai in enumerate(Aj):
                        if(Ai!=other.rows[j][i]):
                            return False
            else:
                return False
            return True