#!/usr/bin/python
# -*- coding: UTF-8 -*-


import readline
import os

HISTORY_FILENAME = '/tmp/completer.hist'


def get_history_items():
    return [ readline.get_history_item(i)
             for i in xrange(1, readline.get_current_history_length() + 1)
             ]

class HistoryCompleter(object):
    
    def __init__(self):
        self.matches = []
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            history_values = get_history_items()
            if text:
                self.matches = sorted(h 
                                      for h in history_values 
                                      if h and h.startswith(text))
            else:
                self.matches = []
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


# Register our completer function
readline.set_completer(HistoryCompleter().complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

def input_loop():
    #if os.path.exists(HISTORY_FILENAME):
    #    readline.read_history_file(HISTORY_FILENAME)
    #print 'Max history file length:', readline.get_history_length()
    #print 'Startup history:', get_history_items()
    try:
        while True:
            line = raw_input('Prompt ("stop" to quit): ')
            if line == 'stop':
                break
            if line:
                print 'Processing "%s"' % line
    finally:
        pass
        #print 'Final history:', get_history_items()
        #readline.write_history_file(HISTORY_FILENAME)


# Prompt the user for text
input_loop()
