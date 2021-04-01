from qtpynodeeditor import (NodeData, NodeDataModel, NodeDataType,
                            NodeValidationState, Port, PortType)
"""
Base Class for Inputs
"""


class InModel(NodeDataModel):
    # Enable Model title
    caption_visible = True
    # Define port
    num_ports = {
        'input': 0,
        'output': 0,
    }
    # Port Caption
    port_caption_visible = False
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
