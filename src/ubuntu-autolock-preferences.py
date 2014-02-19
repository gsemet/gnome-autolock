#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#
from gi.repository import Gtk
from pprint import pprint

class AutolockPreferencesDlg:
    def get_widget(self, widget_name):
        return self.widgets.get_widget(widget_name)

    def delete(self, *args):
        Gtk.main_quit(*args)

    def apply_clicked_cb(self, button):
        pprint(self)
        self.widgets.get_widget('label1').set_text('Vous avez cliqué !')
        print "clicked!"
        return True

if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_file("../data/autolock-preferences.glade")
    builder.connect_signals(AutolockPreferencesDlg())

    window = builder.get_object("preferences")
    window.show_all()

    Gtk.main()
