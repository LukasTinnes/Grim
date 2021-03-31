import logging
import json
import qtpynodeeditor as nodeeditor
from PyQt5.QtWidgets import QApplication

from qtpynodeeditor import (NodeData, NodeDataModel, NodeDataType,
                            NodeValidationState, Port, PortType, StyleCollection)

from nodes.ADDModel import ADDModel
from nodes.DIVModel import DIVModel
from nodes.MODModel import MODModel
from nodes.MULModel import MULModel
from nodes.SUBModel import SUBModel
from nodes.XORModel import XORModel


def main(app, init_style):
    # Load style, if an initial style is wanted
    if init_style:
        with open(init_style) as f:
            json_style = json.load(f)
        style = StyleCollection.from_json(json_style)
    else:
        style = None
    # Create registry, to register possible node types
    registry = nodeeditor.DataModelRegistry()
    # Add node models to registry
    models = [XORModel, ADDModel, SUBModel, MULModel, DIVModel, MODModel]
    for model in models:
        registry.register_model(model, category="Arithmetics", style=style)
    scene = nodeeditor.FlowScene(style=style, registry=registry)

    view = nodeeditor.FlowView(scene)
    view.setWindowTitle("Grim")
    view.resize(1000, 750)
    view.show()
    return scene, view


if __name__ == '__main__':
    # Create logging
    logging.basicConfig(filename="debug.log", level=logging.DEBUG)
    # Create and run qt5 application
    app = QApplication([])
    scene, view = main(app, "../data/styles/tatami.json")
    view.show()
    app.exec_()
