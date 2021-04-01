from qtpynodeeditor import NodeDataType

from nodes.IO.InModel import InModel


class RGBInModel(InModel):
    name = "RGB_IN"

    num_ports = {
        'input': 0,
        'output': 3,
    }
    port_caption = {'output': {0: 'R',
                               1: 'G',
                               2: 'B'
                               },
                    }
    port_caption_visible = {'output': {0: 'R',
                                       1: 'G',
                                       2: 'B'
                                       },
                            }
    data_type = NodeDataType("Signal", "Signal")

    def __init__(self, style=None, parent=None):
        super().__init__(style=style)

    def compute(self):
        pass
