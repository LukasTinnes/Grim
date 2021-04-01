import logging
import json
import qtpynodeeditor as nodeeditor
from PyQt5.QtWidgets import QApplication

from qtpynodeeditor import (NodeData, NodeDataModel, NodeDataType,
                            NodeValidationState, Port, PortType, StyleCollection)

from nodes.IO.RGBInModel import RGBInModel
from nodes.IO.RGBOutModel import RGBOutModel
from nodes.arithmetics.ADDModel import ADDModel
from nodes.arithmetics.DIVModel import DIVModel
from nodes.arithmetics.MODModel import MODModel
from nodes.arithmetics.MULModel import MULModel
from nodes.arithmetics.SUBModel import SUBModel
from nodes.arithmetics.XORModel import XORModel


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
    # IOModels
    io_models = [RGBInModel, RGBOutModel]
    for model in models:
        registry.register_model(model, category="Arithmetics", style=style)
    for model in io_models:
        registry.register_model(model, category="IO", style=style)
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
    app_scene, app_view = main(app, "../data/styles/tatami.json")
    app_view.show()
    app.exec_()
