import anywidget
import traitlets


class MultiNodeWidget(anywidget.AnyWidget):
    _esm ="lists.js"
    names = traitlets.List(traitlets.Unicode()).tag(sync=True)

    def __init__(self, names: List[str]) -> None:
        super().__init__(names=names)





widget = MultiNodeWidget(["Alice", "Bob", "Charlie"])
widget.names

widget

widget.names = widget.names + ["Dave", "Eve"]
