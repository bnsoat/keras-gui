from keras.layers import Input,Dense 
from  .module_gui import ModuleGui

class LayerGui(ModuleGui):
    l = None
    _input_l = None
    _input_shape = None
    _output_shape = None
    def __init__(self,units):
        print("Layer Module Instance")
    
    def __call__(self,input):
        self._input_l = input
        
        print("Layer called ")
    
    def output_shape(self):
        return self._output_shape
    
    def input_shape(self):
        return self._input_l.output_shape()
class DenseGui(LayerGui):
    
    def __init__(self,units):
        print("Dense Layer Module Instance")
        
        

        self.l = Dense(units, activation='relu')
        self._output_shape = units

