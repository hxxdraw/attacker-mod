from .main_screen import *


class LoadingScreen(ttk.Frame):

    """
    Application loading screen.
    * It uses for <application.update_screen(instance)>
    (It handles animations)
    """

    def __init__(self, *args, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)

        # Starting loading
        self.after(LOADING_DELAY, self.start_progress)

        # Images
        self.logo = tk.PhotoImage(file=NINJA_LOGO_PNG)
        self.parent = args[0]

        # Widgets
        self.container = ttk.Frame(self)
        self.loading_progressbar = ttk.Progressbar(self.container)
        self.loading_logo_lbl = ttk.Label(self.container, image=self.logo)

        self.loading_logo_lbl.pack(
            padx=10,
            pady=10,
        )
        self.loading_progressbar.pack(
            padx=10,
            pady=10,
            fill=tk.X
        )
        self.container.place(
            relx=.5,
            rely=.5,
            anchor=tk.CENTER
        )

    def start_progress(self):

        """
        This method starts frames-loading progress.
        Also, application look better with it.
        * Application screen should be change after the loading.
        """

        for frame in range(TROLL_FACE_ANIMATION_FRAMES_COUNT):
            TROLL_FACE_FRAMES.append(tk.PhotoImage(file=TROLL_FACE_ANIMATION_GIF, format=f"gif -index {frame}"))
            self.loading_progressbar['value'] += 100 / TROLL_FACE_ANIMATION_FRAMES_COUNT
            self.loading_progressbar.update()

        self.parent.update_screen(MainScreen)


