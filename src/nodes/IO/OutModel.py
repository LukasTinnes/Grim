from qtpynodeeditor import NodeDataModel, NodeDataType

"""
Base Class for Outputs (inits overwrite input number)
"""


class OutModel(NodeDataModel):
    # Enable Model title
    caption_visible = True
    # Define port
    num_ports = {
        'input': 3,
        'output': 0,
    }
    port_caption = {'input': {0: 'A',
                              1: 'B',
                              2: 'C',
                              },
                    }
    # Port Caption
    port_caption_visible = True
    # Define datatype for checks later
    data_type = NodeDataType("Signal", "Signal")

    # Style and parent could be changed later if wanted, if not it uses standard nodeeditor style
    def __init__(self, style=None, parent=None):
        super().__init__(style=style)
        self._out = None

    @property
    def caption(self):
        return self.name

    # Overwritten in submodules
    def compute(self):
        pass
