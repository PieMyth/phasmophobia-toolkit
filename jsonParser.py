# MIT License

# Copyright (c) 2020 PieMyth

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json

class parser:
    fileName = ""
    fileContents = ""

    def __init__(self):
        self.fileName = ""
        self.fileContents = ""

    def setFileName(self, fileName):
        # Set the filename to open
        self.fileName = fileName
    
    def openFile(self):
        # Open the file and load it as a string into fileContents
        if self.fileName == "":
            print("No file name given!")
            return
        self.fileContents = json.loads(open(self.fileName, 'r').read())

    def returnIndex(self, indexName):
        # Make sure the key is in the dictionary of entries
        # Return the entries linked to that key
        if indexName not in self.fileContents.keys():
            print("Not a valid key")
            return ""
        return self.fileContents[indexName]
    
    def sayings(self):
        # Return all the keys for the dictionary
        if len(self.fileContents) == 0:
            print("no entries found")
        return self.fileContents.keys()

if __name__ == "__main__":
    p = parser()
    p.setFileName("sayings.json")
    p.openFile()
    p.returnIndex("Wrong")
    print(p.returnIndex("hunt"))
    print("done")
