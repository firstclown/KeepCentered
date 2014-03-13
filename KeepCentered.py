#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sublime
import sublime_plugin

class KeepCentered(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        if sublime.active_window().settings().get('fss_on_distraction_free'):
            view.show_at_center(view.sel()[0].begin())
