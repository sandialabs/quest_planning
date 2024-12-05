# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 05:45:39 2024

@author: cjnewlu
"""

from PySide6.QtWidgets import QGraphicsView,QVBoxLayout,QWidget,QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MatplotlibWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # Create a label for error messages
        self.error_label = QLabel("")
        
'''


        class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def clear_plot(self):
        """Clear the current plot."""
        self.figure.clear()

    def draw_plot(self):
        """Refresh the canvas to draw the plot."""
        self.canvas.draw()
'''