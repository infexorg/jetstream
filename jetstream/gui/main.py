from tkinter import ttk


class RootFrame(ttk.Frame):
    """The main window frame for Modis."""

    def __init__(self, parent):
        """Create the frame.

        Args:
            parent: A tk or ttk object.
        """

        super(RootFrame, self).__init__(parent)

        # Define window close action
        def on_closing():
            parent.destroy()
            from sys import exit
            exit(0)
        parent.protocol("WM_DELETE_WINDOW", on_closing)

        # Configure styles
        s = ttk.Style()
        s.configure(
            "jetstream.TNotebook",
            tabmargins=[0, 0, -1, 0],
            tabposition="wn"
        )
        s.configure(
            "jetstream.TNotebook.Tab",
            padding=8,
            width=11
        )
        s.map(
            "jetstream.TNotebook.Tab",
            expand=[
                ("selected", [0, 0, 1, 0]),
                ("active", [0, 0, 1, 0])
            ]
        )

        # Add elements
        nav = ttk.Notebook(self, style="jetstream.TNotebook")
        from jetstream.gui.tabs import home, path, browse, entry
        nav.add(home.Frame(nav), text="Home")
        nav.add(path.Frame(nav), text="Pathfinding")
        nav.add(browse.Frame(nav), text="Browse")
        nav.add(entry.Frame(nav), text="Data entry")

        # Grid elements
        nav.grid(column=0, row=0, sticky="W E N S")

        # Configure stretch ratios
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
