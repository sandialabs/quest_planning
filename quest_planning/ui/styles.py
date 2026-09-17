# -*- coding: utf-8 -*-
"""
Central application stylesheet for the QuESt Planning interface.

All visual styling for the application lives here in one consolidated
stylesheet (mirroring the legacy single-QSS approach): window chrome,
scrollbars, progress bars, cards, labels, inputs and buttons. The UI
form files themselves stay structural and only carry role properties
(``cardType``, ``textRole``, ``btnRole``, ``codeRole``) that this
stylesheet uses as selectors.
"""

APP_STYLESHEET = """
/* ============================== Scrollbars ============================== */
QScrollBar:vertical {
    border: none;
    background: rgb(40, 84, 113);
    width: 8px;
    margin: 0px;
    border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: rgb(129, 194, 65);
    min-height: 25px;
    border-radius: 4px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
QScrollBar:horizontal {
    border: none;
    background: rgb(40, 84, 113);
    height: 8px;
    margin: 0px;
    border-radius: 4px;
}
QScrollBar::handle:horizontal {
    background: rgb(129, 194, 65);
    min-width: 25px;
    border-radius: 4px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* ============================== Progress bars ============================== */
QProgressBar {
    background-color: rgb(240, 240, 240);
    border: 1px solid rgb(210, 210, 210);
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk {
    background: rgb(129, 194, 65);
    border-radius: 4px;
}

/* ============================== Base ============================== */
QWidget {
    font-family: "Segoe UI";
    font-size: 10pt;
    color: rgb(20, 20, 20);
    background-color: rgb(244, 244, 244);
}
QLabel {
    background-color: transparent;
}
QDialog {
    background-color: rgb(244, 244, 244);
}

/* ============================== Main window chrome ============================== */
#frame_ribbon {
    background-color: rgb(40, 84, 113);
    border: none;
}
#frame_logo {
    background-color: transparent;
    border: none;
}
#frame_content {
    background-color: rgb(244, 244, 244);
    border: none;
}
#frame_nav_btns {
    background-color: rgb(244, 244, 244);
    border: none;
    border-top: 1px solid rgb(224, 227, 231);
}
#frame_ribbon QPushButton {
    color: rgb(255, 255, 255);
    background-color: transparent;
    border: none;
    border-radius: 6px;
    padding: 12px 14px;
    text-align: left;
}
#frame_ribbon QPushButton:hover {
    background-color: rgb(60, 120, 150);
}
#frame_ribbon QPushButton:checked {
    background-color: rgb(129, 194, 65);
    color: rgb(255, 255, 255);
    font-weight: bold;
}

/* ============================== Landing page ============================== */
QWidget#page_landing {
    background-color: rgb(255, 255, 255);
    border: 1px solid rgb(216, 216, 216);
    border-radius: 12px;
}
QWidget#page_landing QFrame {
    background-color: transparent;
    border: none;
}

/* ============================== Cards ============================== */
QFrame[cardType="card"] {
    background-color: rgb(255, 255, 255);
    border: 1px solid rgb(216, 216, 216);
    border-radius: 12px;
}
QFrame[cardType="tile"] {
    background-color: rgb(247, 247, 247);
    border: 1px solid rgb(232, 232, 232);
    border-radius: 8px;
}
QFrame[cardType="soft"] {
    background-color: rgb(250, 250, 250);
    border: 1px solid rgb(224, 227, 231);
    border-radius: 10px;
}
QFrame[cardType] QLabel {
    background-color: transparent;
}

/* ============================== Labels ============================== */
QLabel[textRole="heading"] {
    color: rgb(40, 84, 113);
    font-size: 18pt;
    font-weight: bold;
}
QLabel[textRole="section"] {
    color: rgb(40, 84, 113);
    font-weight: bold;
}
QLabel[textRole="subtitle"] {
    color: rgb(100, 100, 100);
    font-size: 10pt;
}
QLabel[textRole="caption"] {
    color: rgb(110, 110, 110);
}
QLabel[textRole="body"] {
    color: rgb(70, 70, 70);
}
QLabel[textRole="dark"] {
    color: rgb(0, 0, 0);
}

/* ============================== Inputs ============================== */
QLineEdit, QComboBox, QDoubleSpinBox, QDateEdit, QPlainTextEdit, QTextBrowser {
    background-color: rgb(255, 255, 255);
    border: 1px solid rgb(204, 204, 204);
    border-radius: 6px;
    padding: 6px 8px;
    selection-background-color: rgb(40, 84, 113);
    selection-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
}
QComboBox::drop-down {
    border: none;
    width: 24px;
}
QComboBox QAbstractItemView {
    background-color: rgb(255, 255, 255);
    border: 1px solid rgb(204, 204, 204);
    selection-background-color: rgb(40, 84, 113);
    selection-color: rgb(255, 255, 255);
}

/* Monospace log/report editors (Execute Model status panel) */
QPlainTextEdit[codeRole="true"] {
    background-color: rgb(250, 250, 250);
    border: 1px solid rgb(210, 210, 210);
    font-family: 'Menlo';
    font-size: 10pt;
}

/* ============================== Trees ============================== */
QTreeView {
    background-color: rgb(250, 250, 250);
    border: 1px solid rgb(210, 210, 210);
    border-radius: 6px;
    alternate-background-color: rgb(244, 246, 249);
}
QTreeView::item:selected {
    background-color: rgb(40, 84, 113);
    color: rgb(255, 255, 255);
}
QTreeView::item:hover {
    background-color: rgb(235, 244, 248);
}

/* ============================== Buttons ============================== */
QPushButton {
    border: 1px solid rgb(40, 84, 113);
    border-radius: 7px;
    background-color: rgb(255, 255, 255);
    color: rgb(40, 84, 113);
    padding: 7px 16px;
}
QPushButton:hover {
    background-color: rgb(235, 244, 248);
}
QPushButton:pressed {
    background-color: rgb(214, 232, 240);
}
QPushButton[btnRole="primary"] {
    background-color: rgb(40, 84, 113);
    color: rgb(255, 255, 255);
}
QPushButton[btnRole="primary"]:hover {
    background-color: rgb(60, 120, 150);
}
QPushButton[btnRole="primary"]:pressed {
    background-color: rgb(20, 60, 80);
}
QPushButton[btnRole="small"] {
    padding: 5px 10px;
    border-radius: 6px;
}
QPushButton:disabled {
    color: rgb(160, 160, 160);
    border-color: rgb(210, 210, 210);
    background-color: rgb(240, 240, 240);
}

/* ============================== Tool buttons ============================== */
QToolButton[btnRole="icon"] {
    border: none;
    border-radius: 5px;
    background-color: transparent;
}
QToolButton[btnRole="icon"]:hover {
    background-color: rgb(230, 235, 240);
}
QToolButton[btnRole="icon"]:pressed {
    background-color: rgb(210, 218, 225);
}
QToolButton[btnRole="toggler"] {
    border: 1px solid rgb(40, 84, 113);
    border-radius: 5px;
    background-color: rgb(255, 255, 255);
    color: rgb(40, 84, 113);
    padding: 4px 10px;
    font-weight: bold;
}
QToolButton[btnRole="toggler"]:hover {
    background-color: rgb(235, 244, 248);
}
QToolButton[btnRole="toggler"]:checked {
    background-color: rgb(40, 84, 113);
    color: rgb(255, 255, 255);
}
"""


def apply_stylesheet(app):
    """Apply the central application stylesheet to the given QApplication."""
    app.setStyleSheet(APP_STYLESHEET)