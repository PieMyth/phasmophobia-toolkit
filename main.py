import windowManager as wm


def main():
    # Create window name with size
    root = wm.tk.Tk(className="Phasmophobia Toolkit")
    root.geometry("300x200")
    app = wm.windowWrapper(master=root)
    # Set the tts voice speed
    app.setSpeed(175)
    # Window loop
    app.mainloop()


if __name__ == "__main__":
    main()
    pass