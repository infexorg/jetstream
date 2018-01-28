from tkinter import ttk


class Frame(ttk.Frame):
    """A tab displaying all stored data."""

    def __init__(self, parent):
        """Create the frame.

        Args:
            parent: A tk or ttk object.
        """

        super(Frame, self).__init__(parent, padding=8)
