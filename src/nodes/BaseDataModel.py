from qtpynodeeditor import NodeDataModel, NodeDataType


class BaseDataModel(NodeDataModel):
    # Enable Model title
    caption_visible = True
    # Define port
    num_ports = {
        'input': 2,
        'output': 1,
    }
    # Port Caption
    port_caption_visible = True
    # Define datatype for checks later
    data_type = NodeDataType("Signal", "Signal")

    # Style and parent could be changed later if wanted, if not it uses standard nodeeditor style
    def __init__(self, style=None, parent=None):
        super().__init__(style=style)
        self._in_1 = None
        self._in_2 = None
        self._out = None

    @property
    def caption(self):
        return self.name

    # Overwritten in submodules
    def compute(self):
        pass
