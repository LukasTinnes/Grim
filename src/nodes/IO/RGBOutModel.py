from qtpynodeeditor import NodeDataType

from nodes.IO.OutModel import OutModel


class RGBOutModel(OutModel):
    name = "RGB_OUT"

    num_ports = {
        'input': 3,
        'output': 0,
    }

    port_caption = {'input': {0: 'R',
                              1: 'G',
                              2: 'B',
                              },
                    'output': {}
                    }
    data_type = NodeDataType("Signal", "Signal")

    def __init__(self, style=None, parent=None):
        super().__init__(style=style)


    def put_out(self):
        pass
