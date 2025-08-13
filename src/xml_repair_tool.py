#!/usr/bin/env python

# This code was taken from:
# http://stackoverflow.com/questions/10604048/pythonic-way-to-fix-broken-xml

import sys
from xml.sax import handler, make_parser

class TagHandler(handler.ContentHandler):
    def __init__(self):
        handler.ContentHandler.__init__(self)

        self.stack = []


    def startElement(self, name, attrs):
        self.stack.append(name)

    def endElement(self, name):
        # TODO: might want to just confirm that the element matches the top of the stack here
        self.stack.pop()


    def finish_document(self):
        return "\n".join(["</%s>" % tag for tag in reversed(self.stack)])


parser = make_parser()
handler = TagHandler()
parser.setContentHandler(handler)

try:
    parser.parse(sys.argv[1])

except:
    # TODO: something more intelligent than just printing out the
    # constructed end of the document. Like appending it to the source
    # and repeating whatever you did to make this processing necessary.
    print(handler.finish_document())
