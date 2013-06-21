from tw2.core.testbase import WidgetTest
from tw2.jqplugins.ui_spinner import *

class TestJqplugins.ui_spinner(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Jqplugins.ui_spinner
    # Initilization args. go here 
    attrs = {'id':'jqplugins.ui_spinner-test'}
    params = {}
    expected = """<div id="jqplugins.ui_spinner-test"></div>"""
