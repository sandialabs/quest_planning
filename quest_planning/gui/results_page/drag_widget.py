import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGridLayout, QFileSystemModel, QMenu, QScrollArea, QSizePolicy, QFrame, QToolBar, QLineEdit
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QAction, QCursor, QDragMoveEvent, QPainter, QIcon, QAction
from PySide6.QtCore import Qt, QUrl, QMimeData, QPoint, QRect, QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings

import os
from quest_planning.paths import get_path
base_dir = get_path()
map_loc = os.path.join (base_dir, "gui", "tools", "usa_110m.json")

import os
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtCore import Qt


class DraggableResizableLabel(QLabel):
    def __init__(self, pix, parent=None):
        super().__init__(parent)
        self.setPixmap(pix)
        self.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFixedSize(350, 350)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.setMouseTracking(True)
        self.resizing = False
        self.dragging = False
        self.offset = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.is_in_resize_area(event.position().toPoint()):
                self.resizing = True
            else:
                self.dragging = True
                self.offset = event.position().toPoint()
        elif event.button() == Qt.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.resizing:
            new_width = max(event.position().toPoint().x(), 10)  # Ensure minimum width
            new_height = max(event.position().toPoint().y(), 10)  # Ensure minimum height
            self.setFixedSize(new_width, new_height)
        elif self.dragging:
            self.move(self.mapToParent(event.position().toPoint() - self.offset))
        else:
            if self.is_in_resize_area(event.position().toPoint()):
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.resizing = False
        self.dragging = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def is_in_resize_area(self, pos):
        return pos.x() > self.width() - 10 and pos.y() > self.height() - 10

    def show_context_menu(self, position):
        context_menu = QMenu(self)
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_label)
        context_menu.addAction(delete_action)
        context_menu.exec(position)

    def delete_label(self):
        self.deleteLater()

class ImageGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setStyleSheet("border: 0px;")
        self.scrollArea.setFrameShape(QScrollArea.NoFrame)
        self.scrollArea.setViewportMargins(0, 0, 0, 0)
        self.containerWidget = QWidget()
        self.containerWidget.setStyleSheet("background-color:  rgb(208, 208, 208); border-radius: 25px;")
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scrollArea)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        position = event.position().toPoint()
        widget_position = self.containerWidget.mapFrom(self, position)

        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(('.png', '.jpeg', '.jpg', '.svg')):
                self.add_image(file_path, widget_position)

    def add_image(self, file_path, position):
        pixmap = QPixmap(file_path)
        label = DraggableResizableLabel(pixmap, self.containerWidget)
        label.move(position)
        label.show()


class FileBrowser(QTreeView):
    def __init__(self):
        super().__init__()
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.setModel(self.model)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)

    def setRootPath(self, path):
        self.model.setRootPath(path)
        self.setRootIndex(self.model.index(path))

    def mimeData(self, indexes):
        mime_data = QMimeData()
        file_paths = [self.model.filePath(index) for index in indexes]
        mime_data.setUrls([QUrl.fromLocalFile(path) for path in file_paths])
        return mime_data

# class WebEngineView(QWebEngineView):
#     def __init__(self):
#         super().__init__()
#         self.setAcceptDrops(True)

#         # Allow local content to access remote URLs
#         self.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

#     def dragEnterEvent(self, event):
#         """
#         Handle drag enter events.
#         """
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dragMoveEvent(self, event):
#         """
#         Handle drag move events.
#         """
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         """
#         Handle drop events. Load the dropped HTML file into the QWebEngineView.
#         """
#         self.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
#         if event.mimeData().hasUrls():
#             for url in event.mimeData().urls():
#                 if url.isLocalFile() and url.toLocalFile().endswith('.html'):
#                     # Load the local HTML file
#                     self.load(QUrl.fromLocalFile(url.toLocalFile()))
#                     break








class WebEngineView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        # Allow local content to access remote URLs
        self.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background: transparent")
        self.page().setBackgroundColor(Qt.transparent)

    def dragEnterEvent(self, event):
        """
        Handle drag enter events.
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        """
        Handle drag move events.
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """
        Handle drop events. Load the dropped HTML file into the QWebEngineView.
        """
        self.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile() and url.toLocalFile().endswith('.html'):
                    # Load the local HTML file
                    self.load(QUrl.fromLocalFile(url.toLocalFile()))
                    break


########above one is good
# class WebEngineView(QWebEngineView):
#     def __init__(self):
#         super().__init__()
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dragMoveEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         if event.mimeData().hasUrls():
#             for url in event.mimeData().urls():
#                 if url.isLocalFile() and url.toLocalFile().endswith('.html'):
#                     self.load(QUrl.fromLocalFile(url.toLocalFile()))
#                     break



# class WebEngineView(QWebEngineView):
#     def __init__(self):
#         super().__init__()
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dragMoveEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         if event.mimeData().hasUrls():
#             for url in event.mimeData().urls():
#                 if url.isLocalFile() and url.toLocalFile().endswith('.html'):
#                     self.load_html_with_js(url.toLocalFile())
#                     break
#     def load_html_with_js(self, file_path):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             html_content = file.read()

#         # Inject the necessary JavaScript libraries (if any)
#         injected_html = f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Generated HTML</title>
#             <meta charset="utf-8" />
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <!-- Add any additional CSS or JS libraries here if needed -->
#         </head>
#         <body>
#             {html_content}
#         </body>
#         </html>
#         """

#         self.setHtml(injected_html)

    # def load_html_with_js(self, file_path):
    #     with open(file_path, 'r') as file:
    #         html_content = file.read()

    #     # Inject the necessary JavaScript libraries
    #     injected_html = f"""
    #     <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Generated HTML</title>
    #         <meta charset="utf-8" />
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    #     </head>
    #     <body>
    #         {html_content}
    #         <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    #     </body>
    #     </html>
    #     """

    #     self.setHtml(injected_html)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Browser with Movable and Resizable Image Grid")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.file_browser = FileBrowser()
        self.image_grid = ImageGrid()
        self.file_browser.setRootPath(r"C:\Users\ylpomer\Desktop\planning\results")
        layout.addWidget(self.file_browser)
        layout.addWidget(self.image_grid)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
