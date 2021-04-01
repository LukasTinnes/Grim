from qtpynodeeditor import NodeDataType
from qtpy.QtWidgets import QLineEdit
from qtpy.QtGui import QDoubleValidator

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
        self._number = None
        self._line_edit = QLineEdit()
        self._line_edit.setMaximumSize(self._line_edit.sizeHint())
        self._line_edit.setText("Yee")

    def embedded_widget(self):
        'The number source has a line edit widget for the user to type in'
        return self._line_edit

    def compute(self):
        pass
