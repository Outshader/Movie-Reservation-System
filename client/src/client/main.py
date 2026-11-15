import urwid


class Main:
    def __init__(self) -> None:
        self.credentials = None
        self.main()

    def handler_main(self, key):
        if key in ["q", "Q"]:
            raise urwid.ExitMainLoop()
        elif key == "1":
            self.login(key=None)

    def login(self, key):
        q1 = urwid.Edit("Email: ")
        q2 = urwid.Edit("Password: ")
        def submit_login(*args):
            self.credentials = q1.edit_text, q2.edit_text
            self.loop.widget = previous_screen

        submit = urwid.widget.Button("Submit", submit_login)
        login_walker = urwid.SimpleFocusListWalker([q1, q2, submit])
        login_widget = urwid.ListBox(login_walker)
        previous_screen = self.loop.widget
        self.loop.widget = login_widget


    def exit(self, key):
        raise urwid.ExitMainLoop()

    def main(self):
        op1 = urwid.Button("login", on_press=self.login)
        op2 = urwid.Button("exit", on_press=self.exit)
        walker = urwid.SimpleFocusListWalker([op1, op2])
        self.menu_widget = urwid.ListBox(walker)
        self.loop = urwid.MainLoop(self.menu_widget, unhandled_input=self.handler_main)
        self.loop.run()
