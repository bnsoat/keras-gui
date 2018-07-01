from keras.layers import Input,Dense 
from .module_gui import ModuleGui
from .layers_info import *


#LayerInfo classess
type_to_class = {'Generic':LayerInfo,'Dense': DenseInfo}

class LayerGui(ModuleGui):
    #l = None
    _input_l = None
    _input_shape = None
    _output_shape = None
    
    
    def __init__(self,units,**kwargs):
        
        print("\n LayerGui __init(): \n {}".format(kwargs))
        allowed_kwargs = {'layer_type'}

        for kwarg in kwargs:
            if kwarg not in allowed_kwargs:
                raise TypeError('Keyword argument not understood:', kwarg)

        layer_type = kwargs.get('layer_type')     
        print("layer_type: ",layer_type)

        print("Layer Module Instance")
        self._layer_info = type_to_class[layer_type](layer_type)
        
        #self._layer_info = LayerInfo(layer_type)

    def __call__(self,input):
        self._input_l = input
        
        print("Layer called ")
    
    def output_shape(self):
        return self._output_shape
    
    def input_shape(self):
        return self._input_l.output_shape()
    def info(self):
        return self._layer_info.info()
class DenseGui(LayerGui):
    
    def __init__(self,units,
                 activation=None,
                 **kwargs):
        print("Dense Layer Module Instance")
        print("kwargs: ",kwargs)
        self._units = units
        self._activation = activation

        if 'layer_type' not in kwargs:
            kwargs['layer_type'] = 'Dense'

        super(DenseGui,self).__init__(units,**kwargs)
        
        self._output_shape = units
    
    #check if container has all necessary info for creating keras layer   
    def is_valid(self):
        if self._activation is None:
            raise TypeError('activation is not Valid:', self._activation)  
     

        return True
    def create_keras_layer(self):
        if self.is_valid():
            #create keras layer
            self._k_layer = Dense(self._units, activation=self._activation)

