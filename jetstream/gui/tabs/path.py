import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from jetstream import calc


class Frame(ttk.Frame):
    """A tab containing the pathfinding tools."""

    def __init__(self, parent):
        """Create the frame.

        Args:
            parent: A tk or ttk object.
        """

        super(Frame, self).__init__(parent, padding=8)

        # Setup variables
        var_om1 = tk.StringVar()
        var_om2 = tk.StringVar()
        var_om3 = tk.StringVar()
        var_omd = tk.StringVar()

        var_leg1 = tk.StringVar()
        var_leg2 = tk.StringVar()
        var_leg1r = tk.StringVar()
        var_leg2r = tk.StringVar()

        # Add elements
        input_frame = ttk.Frame(self)
        output_frame = ttk.Frame(self)

        target_auto_destination = self.TargetAutoDestination(input_frame)
        target_manual_destination = self.TargetManualDestination(input_frame, var_om1, var_om2, var_om3, var_omd, var_leg1, var_leg2, var_leg1r, var_leg2r)
        target_manual_pointtopoint = self.TargetManualPointtopoint(input_frame)

        path_orbital = self.PathOrbital(output_frame, var_leg1, var_leg2, var_leg1r, var_leg2r)
        path_outpost = self.PathOutpost(output_frame)

        # Grid elements
        target_auto_destination.grid(column=0, row=0, padx=8, pady=8, stick="W E N S")
        target_manual_destination.grid(column=1, row=0, padx=8, pady=8, stick="W E N S")
        target_manual_pointtopoint.grid(column=2, row=0, padx=8, pady=8, stick="W E N S")

        path_orbital.grid(column=0, row=0, padx=8, pady=8, sticky="W E N S")
        path_outpost.grid(column=1, row=0, padx=8, pady=8, sticky="W E N S")

        input_frame.grid(column=0, row=0, padx=8, pady=8, sticky="W E N S")
        output_frame.grid(column=0, row=1, padx=8, pady=8, sticky="W E N S")

        # Configure stretch ratios
        input_frame.rowconfigure(0, weight=1)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)

        output_frame.rowconfigure(0, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    class TargetAutoDestination(ttk.LabelFrame):
        """"""

        def __init__(self, parent):
            """Create the frame.

            Args:
                parent: A tk or ttk object.
            """

            super(Frame.TargetAutoDestination, self).__init__(parent, padding=8, text="Auto Destination")

    class TargetManualDestination(ttk.LabelFrame):
        """"""

        def __init__(self, parent, var_om1, var_om2, var_om3, var_omd, var_leg1, var_leg2, var_leg1r, var_leg2r):
            """Create the frame.

            Args:
                parent: A tk or ttk object.
            """

            super(Frame.TargetManualDestination, self).__init__(parent, padding=8, text="Manual Destination")

            # Setup variables
            self.var_om1 = var_om1
            self.var_om2 = var_om2
            self.var_om3 = var_om3
            self.var_omd = var_omd

            self.var_leg1 = var_leg1
            self.var_leg2 = var_leg2
            self.var_leg1r = var_leg1r
            self.var_leg2r = var_leg2r

            # Add elements
            label_om1 = ttk.Label(self, text="Closest OM to target:")
            label_om2 = ttk.Label(self, text="2nd closest OM to target:")
            label_om3 = ttk.Label(self, text="3rd closest OM to target:")
            label_omd = ttk.Label(self, text="Distance between adjacent OMs:")

            entry_om1 = ttk.Entry(self, textvariable=var_om1)
            entry_om2 = ttk.Entry(self, textvariable=var_om2)
            entry_om3 = ttk.Entry(self, textvariable=var_om3)
            entry_omd = ttk.Entry(self, textvariable=var_omd)

            button_calc = ttk.Button(self, command=self.calc, text="Calculate")

            # Grid elements
            label_om1.grid(column=0, row=0, padx=8, pady=8, sticky="E")
            label_om2.grid(column=0, row=1, padx=8, pady=8, sticky="E")
            label_om3.grid(column=0, row=2, padx=8, pady=8, sticky="E")
            label_omd.grid(column=0, row=3, padx=8, pady=8, sticky="E")

            entry_om1.grid(column=1, row=0, padx=8, pady=8, sticky="W E")
            entry_om2.grid(column=1, row=1, padx=8, pady=8, sticky="W E")
            entry_om3.grid(column=1, row=2, padx=8, pady=8, sticky="W E")
            entry_omd.grid(column=1, row=3, padx=8, pady=8, sticky="W E")

            button_calc.grid(column=1, row=4, padx=8, pady=8, sticky="E")

            # Configure stretch ratios
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=0)
            self.rowconfigure(2, weight=0)
            self.rowconfigure(3, weight=0)
            self.rowconfigure(4, weight=0)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

        def calc(self):
            try:
                om1 = round(float(self.var_om1.get()), 1)
                om2 = round(float(self.var_om2.get()), 1)
                om3 = round(float(self.var_om3.get()), 1)
                omd = round(float(self.var_omd.get()), 1)
            except ValueError:
                messagebox.showerror(title="Invalid distances", message="One or more of the distances you have input are not valid numbers.")
                return

            leg1, leg2, leg1r, leg2r = calc.pathcalc_om(om1, om2, om3, omd)

            self.var_leg1.set(str(leg1))
            self.var_leg1r.set(str(leg2))
            self.var_leg2.set(str(leg1r))
            self.var_leg2r.set(str(leg2r))

    class TargetManualPointtopoint(ttk.LabelFrame):
        """"""

        def __init__(self, parent):
            """Create the frame.

            Args:
                parent: A tk or ttk object.
            """

            super(Frame.TargetManualPointtopoint, self).__init__(parent, padding=8, text="Manual Point to Point")

    class PathOrbital(ttk.LabelFrame):
        """"""

        def __init__(self, parent, var_leg1, var_leg2, var_leg1r, var_leg2r):
            """Create the frame.

            Args:
                parent: A tk or ttk object.
            """

            super(Frame.PathOrbital, self).__init__(parent, padding=8, text="Orbital Path")

            label_leg1 = ttk.Label(self, text="1st leg length:")
            label_leg2 = ttk.Label(self, text="2nd leg length:")
            label_leg1r = ttk.Label(self, text="Remaining distance to 2nd closest OM after 1st leg:")
            label_leg2r = ttk.Label(self, text="Remaining distance to 3rd closest OM after 2nd leg:")

            entry_leg1 = ttk.Entry(self, textvariable=var_leg1, state="readonly")
            entry_leg2 = ttk.Entry(self, text=var_leg2, state="readonly")
            entry_leg1r = ttk.Entry(self, text=var_leg1r, state="readonly")
            entry_leg2r = ttk.Entry(self, text=var_leg2r, state="readonly")

            # Grid elements
            label_leg1.grid(column=0, row=0, padx=8, pady=8, sticky="E")
            label_leg2.grid(column=0, row=1, padx=8, pady=8, sticky="E")
            label_leg1r.grid(column=0, row=2, padx=8, pady=8, sticky="E")
            label_leg2r.grid(column=0, row=3, padx=8, pady=8, sticky="E")

            entry_leg1.grid(column=1, row=0, padx=8, pady=8, sticky="W E")
            entry_leg2.grid(column=1, row=1, padx=8, pady=8, sticky="W E")
            entry_leg1r.grid(column=1, row=2, padx=8, pady=8, sticky="W E")
            entry_leg2r.grid(column=1, row=3, padx=8, pady=8, sticky="W E")

            # Configure stretch ratios
            self.rowconfigure(0, weight=0)
            self.rowconfigure(1, weight=0)
            self.rowconfigure(2, weight=0)
            self.rowconfigure(3, weight=0)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

    class PathOutpost(ttk.LabelFrame):
        """"""

        def __init__(self, parent):
            """Create the frame.

            Args:
                parent: A tk or ttk object.
            """

            super(Frame.PathOutpost, self).__init__(parent, padding=8, text="Outpost Path")
