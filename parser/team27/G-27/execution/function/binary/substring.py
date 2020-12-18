import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from bstring_functions import substring

class Substring(Function):
    def __init__(self, input1, input2, input3, row, column):
        Function.__init__(self,row,column)
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
    
    def execute(self, environment):
        #input es una lista
        value2 = self.input2.execute(environment)
        value3 = self.input3.execute(environment)

        if value2['typ'] != Type.INT:
            return {'Error':"El valor " + str(value2['value']) + " no es Entero", 'linea':self.row,'columna':self.column }
        if value3['typ'] != Type.INT:
            return {'Error':"El valor " + str(value3['value']) + " no es Entero", 'linea':self.row,'columna':self.column }
        
        if isinstance(self.input1,list):
            respuesta = []
            for val in self.input1:
                value = val.execute(environment)
                if value['typ'] != Type.STRING:
                    return {'Error':"El valor " + value['value'] + " no es String", 'linea':self.row,'columna':self.column }
                result = substring(value['value'],value2['value'],value3['value'])
                respuesta.append({'value':result, 'typ': Type.STRING})
            return respuesta
        #input valor puntual
        else:
            value = self.input1.execute(environment)
            if value['typ'] != Type.STRING:
                return {'Error':"El valor " + value['value'] + " no es String", 'linea':self.row,'columna':self.column }
            return [{'value': substring(value['value'],value2['value'],value3['value']), 'typ': Type.STRING}]