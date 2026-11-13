from textual import LogCallable
import textual
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView


class MainMenu(App):
    CSS_PATH = "index.css"

    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("Login"), id="login"),
            ListItem(Label("Exit"), id="exit"),
        )
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):
        if event.item.id == "login":
            ...
        match event.item.id:
            case "login":
                ...
            case "exit":
                self.exit()


# if __name__ == "__main__":
def main():
    app = MainMenu()
    app.run()
