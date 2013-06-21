import tw2.core as twc
import tw2.forms as twf



# imports from this package
from tw2.jqplugins.ui import base as uibase
from tw2.jqplugins.ui import jquery_ui

ui_spinner_js = twc.JSLink(
    modname=__name__,
    filename='static/ui.spinner.min.js',
    resources=[uibase.jquery_ui]
    )


class SpinnerWidget(uibase.JQueryUIWidget, twf.TextField):

    resources = [ ui_spinner_js ] 

    template = "tw2.jqplugins.ui_spinner.templates.spinner"
    jqmethod = "spinner"
