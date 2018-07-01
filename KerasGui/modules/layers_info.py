class LayerInfo:
    def __init__(self,layer_type="Generic"):
        self._layer_type = layer_type

    def info(self):
        return self._layer_type

class DenseInfo(LayerInfo):
    def __init__(self,layer_type="Dense"):
        #layer_type = "Dense"
        super(DenseInfo,self).__init__(layer_type)
        
