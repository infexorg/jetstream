def start():
    """Start Jetstream"""

    import tkinter as tk
    from jetstream.gui import main

    # Setup the root window
    root = tk.Tk()
    # root.overrideredirect(1)
    root.minsize(width=800, height=400)
    root.geometry("800x600")
    root.title("INFEX Jetstream")
    # root.iconbitmap(__file__[:-11] + "assets/modis.ico")

    # Add elements
    main = main.RootFrame(root)

    # Grid elements
    main.grid(column=0, row=0, padx=0, pady=0, sticky="W E N S")

    # Configure stretch ratios
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main.columnconfigure(0, weight=1)
    main.rowconfigure(0, weight=1)

    # Run the root window
    root.mainloop()

    return


if __name__ == '__main__':
    start()
