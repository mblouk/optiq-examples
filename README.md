# Example scripts for the Master OPTIQ Python course

## `scope`

An example of a basic oscilloscope viewer

### Content

* `ui_scope.py`: Graphical skeleton
* `ui_scope.ui`: Corresponding Designer file
* `fake_scope.py`: Fake oscilloscope driver
* `scope_viewer.py`: Main program for the viewer

### Signal/slots organisation

1. In the `ScopeThread` class, the `run()` method calls the `get_plot()` method from the `FakeScope` class
2. Consequently, the `current_plot` signal is emitted which triggers the `send_new_plot()` method
3. The `send_new_plot()` call emits the `new_plot` signal which triggers the `display_new_plot()` method from the ScopeViewer class





