from gi.repository import Nautilus, GObject
from subprocess import run
import os

# Provide the full path to the VSCode executable for security (adjust if needed)
VSCODE = '/usr/bin/code'  # Or 'code' if in PATH

# What name do you want to see in the context menu?
VSCODENAME = 'Code'

# Always create a new window?
NEWWINDOW = False


class VSCodeExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, menu, files):
        safepaths = []
        args = []

        for file in files:
            filepath = file.get_location().get_path()

            # Get the absolute path for security
            abs_filepath = os.path.abspath(filepath)
            safepaths.append(abs_filepath)

            # If any file is a directory, add --new-window argument
            if os.path.isdir(abs_filepath) and os.path.exists(abs_filepath):
                args.append('--new-window')

        # Always create a new window if specified
        if NEWWINDOW:
            args.append('--new-window')

        # Run VSCode with the given files and arguments
        run([VSCODE] + args + safepaths)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='VSCodeOpen',
            label='Open with ' + VSCODENAME,
            tip='Opens the selected files with VSCode'
        )
        item.connect('activate', self.launch_vscode, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='VSCodeOpenBackground',
            label='Open with ' + VSCODENAME,
            tip='Opens the current directory in VSCode'
        )
        item.connect('activate', self.launch_vscode, [file_])

        return [item]
