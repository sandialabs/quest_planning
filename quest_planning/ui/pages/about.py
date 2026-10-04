import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser
import markdown
from quest_planning.paths import get_path
from quest_planning.ui.forms.about_page.ui_about import Ui_AboutPage

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutPage()
        self.ui.setupUi(self)
        readme_path = get_path().parent / "README.md"
        with open(readme_path, encoding="utf-8") as f:
            html = markdown.markdown(f.read(), extensions=["tables"])
        font_size = "14px"
        styled_html = f"""<html><body style="font-size: {font_size};">
            {html}
            <style>
                img {{ display: block; margin: 0 auto; max-width: 100%; height: auto; }}
            </style>
        </body></html>"""
        self.ui.textBrowser_README.setHtml(styled_html)
        self.ui.textBrowser_README.setOpenExternalLinks(True)
