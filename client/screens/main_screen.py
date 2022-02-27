import tkinter as tk
from tkinter import ttk

import loader
from settings import *


class MainScreen(ttk.Frame):

    """
    Main screen of the application.
    loading screen -> main screen -> ...
    """

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)

        """
        Grid configuration.
        It divides screen on two parts. (Left and right)
        Left -> Main part of the application (options, control-buttons, fields, etc.)
        Right -> Secondary part of the application (mod info, sources, etc.)
        """

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Creating widgets
        self.left_frame = LeftPartContainer(self, **loader.load_json(CARD_FRAME_CFG_FILE))
        self.right_frame = RightPartContainer(self, **loader.load_json(CARD_FRAME_CFG_FILE))

        # Widgets positioning
        self.left_frame.grid(
            row=0,
            column=0,
            sticky=tk.NSEW,
            rowspan=2,
            padx=10,
            pady=10
        )
        self.right_frame.grid(
            row=0,
            column=1,
            sticky=tk.NSEW,
            rowspan=2,
            padx=10,
            pady=10
        )


class LeftPartContainer(ttk.Frame):

    """
    This is the left part of the window
    * It's main part
    * It can't be disabled.
    """

    def __init__(self, *args, **kwargs):
        super(LeftPartContainer, self).__init__(*args, **kwargs)

        # Creating widgets
        self.status_lbl = ttk.Label(self, **loader.load_json(STATUS_LABEL_CFG_FILE))

        # Widgets positioning
        self.status_lbl.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky=tk.NSEW
        )


class RightPartContainer(ttk.Frame):

    """
    This is the right part of the window.
    * It's secondary part.
    * It can be disabled.
    """

    def __init__(self, *args, **kwargs):
        super(RightPartContainer, self).__init__(*args, **kwargs)


class _BtnSrcContainer(ttk.Frame):

    """
    This frame contains buttons which redirects you to the app-sources.
    This class is based on <tkinter.ttk.ttkFrame> class
    * It can be disabled.
    * Right part of the screen.
    """

    def __init__(self, *args, **kwargs):
        super(_BtnSrcContainer, self).__init__(*args, **kwargs)

        # Creating widgets
        self.original_btn = ttk.Button(self, **loader.load_json(ORIGINAL_GITHUB_BUTTON_CFG_FILE))
        self.mod_btn = ttk.Button(self, **loader.load_json(MODIFICATION_GITHUB_BUTTON_CFG_FILE))

        # Widgets positioning
        self.original_btn.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )
        self.mod_btn.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )


