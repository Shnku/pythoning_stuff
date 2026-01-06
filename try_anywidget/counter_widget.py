import anywidget
import traitlets


class CounterWidget(anywidget.AnyWidget):
    _esm = "counter_widget.js"
    _css = "counter_widget.css"

    value = traitlets.Int(0).tag(sync=True)

    def set_data(self, val):
        self.value = val


c = CounterWidget(value=45)
