import tkinter as tk

import loader
from settings import *
from client.screens import *


class Application(tk.Tk):

    """
    Main window of the application. (it's modified <tkinter.Tk> class)
    It's the parent of whole widgets
    """

    def __init__(self):
        super(Application, self).__init__()

        """
        Application configuring.
        It uses config from <appc.py> file.
        Some options can be deleted.
        """

        self.title(app_win_title)   # app title
        self.geometry("{}x{}+{}+{}".format(*app_win_size, *self.get_xy_center_move()))  # window size and position
        self.resizable(*app_win_resizable)  # is resizable?
        self.overrideredirect(app_win_borderless)   # window borderless mode
        self.wm_attributes(TK_ATTRIBUTE_TOPMOST, app_win_topmost)   # topmost rendering
        self.use_custom_theme(THEMES_DATA_FILES_LIST[0], 1)
        self.update_screen(LoadingScreen)

    def get_xy_center_move(self):

        """
        Use this method if you want to position window to the center of the screen.
        It returns move_x and move_y coordinates.
        example: win.geometry({}x{}+{move_x}+{move_y}) from top-left part of the screen.
        :return: move_x: int; move_y: int
        """

        x = self.winfo_screenwidth() - app_win_size[0]
        y = self.winfo_screenheight() - app_win_size[1]

        return x // 2, y // 2

    def use_custom_theme(self, data_file_path: str, style_index: int):

        """
        Use it if you want to activate custom ttk-theme.
        Enabled themes are kept in <assets/themes> folder.
        This method requires theme-data-file path and style index.
        * About indexes -> 0 - light; 1 - dark;
        * All the information about theme can be found in <assets/themes-data> folder
        """

        self.tk.call(TK_COMMAND_SOURCE, loader.load_json(data_file_path)['source'])
        self.tk.call(TK_COMMAND_SET_THEME, loader.load_json(data_file_path)['styles'][style_index])

    def update_screen(self, new_screen: object):

        """
        This method destroys all widgets which is contained in the window surface.
        It uses for screen changing in the app. Like -> loading screen -> main screen -> ...
        * NewScreen must be tkinter.Frame or ttk.Frame, but other tkinter widgets are also supported.
        """

        assert isinstance(new_screen, object)

        [widget.destroy() for widget in self.winfo_children()]

        new_screen(self).pack(
            fill=tk.BOTH,
            expand=True
        )

    def on_close(self):

        """
        This method is called when user tries to close the window of the application.
        * Describe algo here.
        """

        self.destroy()  # default

