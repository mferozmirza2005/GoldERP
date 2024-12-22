from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label, ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

Builder.load_file("index.kv")


class CustomLabel(Label):
    default_text_color = ListProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        kwargs["color"] = self.default_text_color
        super().__init__(**kwargs)


class GoldERP(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Gold ERP"

    def create_tabs(self):
        """Create the main navigation tabs."""
        tab_panel = TabbedPanel(
            background_color=(1, 1, 1),
            tab_height=30,
        )

        home_tab = TabbedPanelItem(
            text="Home", background_color=(1, 1, 1), color=(0, 0, 0)
        )
        home_tab.background_normal = ""
        home_tab.background_down = ""

        home_layout = FloatLayout(size_hint=(None, None), size=(300, 60))

        home_button = Button(
            text="Welcome to Gold ERP!",
            font_size="24sp",
            size_hint=(None, None),
            size=(260, 40),
        )
        home_button.pos_hint = {"x": 0.05, "y": 0}

        home_layout.add_widget(home_button)

        home_tab.add_widget(home_layout)

        tab_panel.add_widget(home_tab)

        tab_panel.default_tab = home_tab

        return tab_panel

    def app_main(self):
        tab_panel = self.create_tabs()
        return tab_panel

    def build(self):
        Window.maximize()
        Window.clearcolor = (1, 1, 1, 1)

        return self.app_main()


if __name__ == "__main__":
    app = GoldERP()
    app.run()
