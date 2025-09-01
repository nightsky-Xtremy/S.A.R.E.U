#!/usr/bin/env python3
import gi
import json
import random
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

# Cargar respuestas
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

class SAREU:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("sareu.glade")

        self.window = self.builder.get_object("main_window")
        self.combobox = self.builder.get_object("combobox")
        self.button = self.builder.get_object("button")
        self.advice_label = self.builder.get_object("advice_label")

        for situation in responses.keys():
            self.combobox.append_text(situation)

        self.button.connect("clicked", self.get_advice)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def fade_in(self, widget, text):
        widget.set_opacity(0)
        widget.set_text(text)
        self.opacity = 0
        def increase_opacity():
            if self.opacity < 1:
                self.opacity += 0.05
                widget.set_opacity(self.opacity)
                return True
            return False
        GLib.timeout_add(30, increase_opacity)

    def get_advice(self, widget):
        situation = self.combobox.get_active_text()
        if situation and situation in responses:
            advice = random.choice(responses[situation])
            self.fade_in(self.advice_label, advice)
        else:
            self.fade_in(self.advice_label, "Temo que mis conocimientos están limitados, sin embargo sigo estando para apoyarte en lo que necesites")

if __name__ == "__main__":
    SAREU()
    Gtk.main()

