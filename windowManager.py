import tkinter as tk
import pyttsx3
import jsonParser as j
import threading


class windowWrapper(tk.Frame):
    def __init__(self, master=None):
        # Initialize and create all the variable needed for execution
        super().__init__(master)
        self.master = master
        self.engine = pyttsx3.init() # object creation
        self.jparser = j.parser()
        self.jparser.setFileName("sayings.json")
        self.jparser.openFile()
        self.running = True
        self.keys = []
        self.keysLength = 0
        self.sayings = []
        self.sayingsLength = 0
        self.volume = 1.0
        self.selection= ""
        self.running = True
        # Create a thread so the window can stop at any time
        self.th = threading.Thread(target=self.playVoice)
        # Get all the keys available from the dropdown
        for saying in self.jparser.sayings():
            self.keys.append(saying)
        self.keysLength = len(self.keys)
        # Debugging
        # print(self.keys)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the gui windows and where they are located
        self.versionLabel = tk.Label(self.master, text="Phasmophobia Toolkit v0.1").pack(side=tk.TOP, anchor=tk.NW)
        self.instructions = tk.Label(self.master, text="Select a target:").pack(side=tk.TOP, anchor=tk.NW)
        self.optionsVar = tk.StringVar()
        self.optionsVar.set("--Select An Option--")
        self.optionsVar.trace('w', self.change_dropdown)
        self.popupMenu = tk.OptionMenu(self.master, self.optionsVar, *self.keys).pack(side=tk.TOP, anchor=tk.NW)
        self.sayingsCount = tk.Entry(self.master)
        self.sayingsCount.insert(0,"10")
        self.voiceButton = tk.Button(self.master)
        self.voiceButton["text"] = "Play"
        self.voiceButton["command"] = self.playVoiceWrapper
        self.voiceButton.pack(side=tk.TOP, anchor=tk.NW)
        self.stopButton = tk.Button(self.master)
        self.stopButton["text"] = "Stop"
        self.stopButton["command"] = self.stopVoice
        self.stopButton.pack(side=tk.TOP, anchor=tk.NW)

    def change_dropdown(self, *args):
        # Callback function for dropdown selection
        self.selection = str(self.optionsVar.get())
        print(self.optionsVar.get())

    def setSpeed(self,speed):
        # Set the speed of the tts engine
        self.engine.setProperty('rate', speed)

    def getSayingsFromIndex(self,index):
        # Update to get the sayings from the current collection
        self.sayings = self.jparser.returnIndex(index)
        self.sayingsLength = len(self.sayings)

    def setRunning(self,setTo):
        # Bool to control running operation
        self.running = setTo

    def getKeys(self):
        # Wrapper for keys from the json
        return self.jparser.sayings()

    def stopVoice(self):
        # Cancel the current voice function
        self.running = False

    def playVoiceWrapper(self):
        # Spin up a new thread and start playing the voice
        self.th = threading.Thread(target=self.playVoice)
        self.th.start()

    def playVoice(self):
        # Loop through all of the sayings
        # Exit after one loop
        print("Playing voice: " + self.selection)
        self.getSayingsFromIndex(self.selection)
        i = 0
        self.running = True
        while i < self.sayingsLength and self.running is True:
            print(self.sayings[i])
            self.engine.say(self.sayings[i])
            self.engine.runAndWait()
            self.engine.stop()
            i += 1
        print("Finished voice")
        self.running = False


if __name__ == "__main__":
    # Testing
    root = tk.Tk(className="Phasmophobia Toolkit")
    root.geometry("300x200")
    app = windowWrapper(master=root)
    app.mainloop()