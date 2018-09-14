#!/usr/bin/python
# -*- coding: UTF-8 -*-


import readline
import os
import pprint

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

books = []

def load():
    global books
    print "Loading books from DB"
    try:
        f = open("lib.db", "r")
        info = f.read()
        books = eval(info)
        f.close()
    except:
        pass
 

def store():
    global books
    print "Storing books to DB"
    f = open("lib.db", "w+")
    f.write(str(books))
    f.close()
    pass

def addbook(book):
    global books
    abook = {}
    abook['title']  = book[0]
    abook['author'] = book[1]
    abook['class']  = book[2]
    abook['isbn']   = book[3]
    books.append(abook)
    print 'Added new book "%s"' % (book)
    pass

def listbooks():
    global books
    pp = pprint.PrettyPrinter(indent=8)
    pp.pprint(books)
    pass

def handle_cmd(cmd):
    c = cmd.split(' ')
    if (c[0] == 'addbook'):
        addbook(c[1:])
    elif (c[0] == 'listbooks'):
        listbooks()
    else:
        print "Invalid/Unknown CMD"
    pass


def input_loop():
    #if os.path.exists(HISTORY_FILENAME):
    #    readline.read_history_file(HISTORY_FILENAME)
    #print 'Max history file length:', readline.get_history_length()
    #print 'Startup history:', get_history_items()
    try:
        while True:
            line = raw_input('Please Enter your CMD("stop" to quit):')
            if line == 'stop':
                break
            if line:
                handle_cmd(line)

    finally:
        pass
        store()
        #print 'Final history:', get_history_items()
        #readline.write_history_file(HISTORY_FILENAME)


# Program starts here
load()
input_loop()
