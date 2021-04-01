from qtpynodeeditor import NodeDataModel, NodeDataType

"""
Base Class for Outputs (inits overwrite input number)
"""


class OutModel(NodeDataModel):
    # Enable Model title
    caption_visible = True
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
