import argparse
import atexit
import cmd
import shlex
import cowsay
import logging
import readline
import argparse
import os
from src.PushPip.cow_say import Parser # need run as module 'python -m src.MergetoolCommandline.solution'

class CustomConsole(cmd.Cmd):
    history_length = 100
    fullname = os.path.join(os.path.dirname(__file__), 'history.txt')
    def __init__(self):
        super().__init__(completekey=None)
        self.parser = Parser()
        readline.parse_and_bind('tab: complete')
        readline.set_completer_delims("".join(set(readline.get_completer_delims()) - set('-')))
        readline.set_completer(self.complete)

        readline.set_history_length(self.history_length)
        if os.path.exists(self.fullname):
            readline.read_history_file(self.fullname)
        self.intro = self.parser.parser.prog
        self.cmd_names = []
        self.start_index = 0
        for el in self.parser.parser._actions:
            self.cmd_names.extend(el.option_strings)

        # print(self.cmd_names, 'cmd_names')

    def default(self, line):
        try:
            self.parser.parse(shlex.split(line))
        except SystemExit as e:
            print(e)

    def emptyline(self):
        pass

    def complete(self, text, state):
        # ret = super().complete(text, state)

        matches = [el for el in self.cmd_names if el.startswith(text)]
        rel_index = state - self.start_index
        if rel_index > len(matches): return None
        ret = matches[rel_index]

        return ret

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def postloop(self):
        print('postloop hock')
        readline.write_history_file(self.fullname)

if __name__ == '__main__':
    CustomConsole().cmdloop()



