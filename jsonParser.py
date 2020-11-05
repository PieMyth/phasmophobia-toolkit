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
