import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time

# FONTS
TITLEFONT = ("Verdana", 15)
MEGAFONT = ("Verdana", 50)

# variables
highbeams = False
lights = False
speed = 0

# destination variables
destinations = [
    "Daejeon: 160",
    "Gwangju: 357",
    "Busan: 325"
]
destination = 0

# music variables
playlist = [
    "BTS - Dynamite",
    "BTS - Boy With Luv",
    "BTS - Yet To Come",
    "BTS - Fire",
    "BTS - Butter",
    "BTS - FAKE LOVE",
    "BTS - My Universe"
]
song = 0

# main window
class AutovisApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (Menu, Directions, Headlights, Speedometer, Cameras, Music):
            frame = page(main_frame, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_frame(Menu)

    # display parameter frame
    def display_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# welcome frame
class Menu(tk.Frame):
    
    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)

        # welcome text
        label = ttk.Label(self, text="Digital Dash", font=TITLEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        label2 = ttk.Label(self, text="by Autovis", font=TITLEFONT)
        label2.grid(row=1, column=2, padx=10, pady=35)
        #
        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=2, column=0, padx=10, pady=10)

        # # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=2, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=2, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=2, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=2, column=4, padx=10, pady=10)


# helper function - update destination
# receives action string and label to update
def update_destination(action, label):
    # brings current destination index into scope
    global destination
    if action == "next":
        # prevent destination index from going out of bounds
        # if incrementing out of bounds, set destination index to 0
        if destination == len(destinations) - 1:
            destination = 0
        else:
            destination += 1
    else:
        # if decrementing out of bounds, set destination index to last index
        if destination == 0:
            destination = len(destinations) - 1
        else:
            destination -= 1
    # update text to the destination in destinations
    # slice string to display location and distance on new lines
    label.config(
        text=f"Destination:\n{destinations[destination][0:-5]}\n{destinations[destination][-3:]} km"
    )


# directions frame
class Directions(tk.Frame):

    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)

        # display directions title
        label = ttk.Label(self, text="Directions", font=TITLEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # open image, put onto label, display
        img = ImageTk.PhotoImage(Image.open("assets/maps.png"))
        label2 = ttk.Label(self, image=img)
        label2.image = img
        label2.grid(row=1, column=1)

        # display current location
        current_location_label = ttk.Label(self, text="Location:\nSeoul", font=TITLEFONT)
        current_location_label.grid(row=1, column=2)

        # display destination
        destination_label = ttk.Label(
            self,
            text=f"Destination:\n{destinations[0][0:-5]}\n{destinations[0][-3:]} km",
            font=TITLEFONT)
        destination_label.grid(row=1, column=3)

        # previous and next buttons to call helper functions
        # passes actions (prev or next) and destination_label
        prev_button = ttk.Button(self, text="Prev",
                                 command=lambda: update_destination("prev", destination_label))
        prev_button.grid(row=1, column=0, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next",
                                 command=lambda: update_destination("next", destination_label))
        next_button.grid(row=1, column=4, padx=10, pady=10)

        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=2, column=0, padx=10, pady=10)

        # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=2, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=2, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=2, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=2, column=4, padx=10, pady=10)


# helper function - toggle headlights
# receives label to update
def toggle_lights(label, label2):
    # brings global lights variable into scope
    global lights
    global highbeams
    # assign lights to the opposite of what it currently is
    lights = not lights
    # if lights is on, update text to ON
    # otherwise, update text to OFF
    if lights:
        label.config(text="ON")
    else:
        highbeams = False
        label.config(text="OFF")
        label2.config(text="OFF")


# helper function - toggle high-beams
# receives label to update
def toggle_high(label):
    # brings global lights (headlights) and highbeams variables into scope
    global lights
    global highbeams
    # checks if the headlights are on before turning on
    if lights and not highbeams:
        highbeams = True
    else:
        highbeams = False
    if highbeams:
        label.config(text="ON")
    else:
        label.config(text="OFF")



# headlights frame
class Headlights(tk.Frame):

    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)

        # display headlights label
        headlights_label = ttk.Label(self, text="Headlights", font=TITLEFONT)
        headlights_label.grid(row=0, column=2, padx=10, pady=10)

        # display headlights status
        headlights_toggle_label = ttk.Label(self, text="OFF", font=TITLEFONT)
        headlights_toggle_label.grid(row=1, column=2, pady=10)

        # button to turn on Headlights
        headlights_button = ttk.Button(
            self, text=f'Toggle Headlights', command=lambda: toggle_lights(
                headlights_toggle_label, highbeams_toggle_label
            )
        )
        headlights_button.grid(row=2, column=2)

        # display high-beams label
        highbeams_label = ttk.Label(self, text="High-Beams", font=TITLEFONT)
        highbeams_label.grid(row=3, column=2, padx=10, pady=10)

        # display high_beams status
        highbeams_toggle_label = ttk.Label(self, text="OFF", font=TITLEFONT)
        highbeams_toggle_label.grid(row=4, column=2, pady=10)

        # button to turn on Headlights
        highbeams_button = ttk.Button(
            self, text=f'Toggle High-Beams', command=lambda: toggle_high(highbeams_toggle_label)
        )
        highbeams_button.grid(row=5, column=2)

        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=6, column=0, padx=10, pady=10)

        # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=6, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=6, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=6, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=6, column=4, padx=10, pady=10)


# helper function - update speed
# receives speed label and target label to update and slider
def update_speed(speed_label, target_label, slider):
    # bring current speed into scope
    global speed
    # set target to the slider value
    target = int(slider.get())
    # change target label text to target speed
    target_label.config(text=f"{'{:0>3}'.format(target)}")
    # assign acceleration time of 1km to 1 second
    t = 1
    # if target is greater than current speed
    if target > speed:
        # update speed, increase acceleration until target speed matched
        for i in range(int(speed), int(target)):
            # if slider moved, break loop
            if int(slider.get()) != target:
                target_label.config(text=f"...")
                break
            speed += 1
            if t > 0.2:
                t *= 0.9
            # update speed text
            speed_label.config(text=f"{'{:0>3}'.format(speed)}")
            speed_label.update()
            slider.update()
            # wait for (t)
            time.sleep(t)
    # same concept for target speed < current speed, but down
    if target < speed:
        for i in range(int(speed), int(target), -1):
            if int(slider.get()) != target:
                target_label.config(text=f"...")
                break
            speed -= 1
            if t > 0.2:
                t *= 0.9
            speed_label.config(text=f"{'{:0>3}'.format(speed)}")
            speed_label.update()
            slider.update()
            time.sleep(t)


# speedometer frame
class Speedometer(tk.Frame):

    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)

        # slider to select speed
        slider = ttk.Scale(self, from_=0, to=160, orient="horizontal")
        slider.grid(row=2, column=2, padx=10, pady=10)

        # label to display speed
        speed_label = ttk.Label(self, text=f"{'{:0>3}'.format(speed)}", font=MEGAFONT)
        speed_label.grid(row=0, column=1, padx=10, pady=10)

        # display target speed
        target_label = ttk.Label(self, text=f"...", font=MEGAFONT)
        target_label.grid(row=0, column=3, padx=10, pady=10)

        # display kmph text
        kmph_label = ttk.Label(self, text="kmph", font=TITLEFONT)
        kmph_label.grid(row=1, column=2, padx=10, pady=10)

        # display current and target speed
        current_label = ttk.Label(self, text="current", font=TITLEFONT)
        current_label.grid(row=1, column=1, padx=10, pady=10)
        target_label2 = ttk.Label(self, text="target", font=TITLEFONT)
        target_label2.grid(row=1, column=3, padx=10, pady=10)

        # button to set speed
        set_button = ttk.Button(
            self, text="Set Speed", command=lambda: update_speed(speed_label, target_label, slider)
        )
        set_button.grid(row=3, column=2, padx=10, pady=10)

        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=4, column=0, padx=10, pady=10)

        # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=4, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=4, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=4, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=4, column=4, padx=10, pady=10)


# cameras frame
class Cameras(tk.Frame):

    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)

        # display cameras title
        label = ttk.Label(self, text="Cameras", font=TITLEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # display left blind spot text
        cam_label = ttk.Label(self, text="Left Blind Spot", font=TITLEFONT)
        cam_label.grid(row=2, column=1)

        # display right blind spot text
        cam_label = ttk.Label(self, text="Right Blind Spot", font=TITLEFONT)
        cam_label.grid(row=2, column=3)

        # display left blind spot picture
        img = ImageTk.PhotoImage(Image.open("assets/left.png"))
        label2 = ttk.Label(self, image=img)
        label2.image = img
        label2.grid(row=1, column=1)

        # display right blind spot picture
        img = ImageTk.PhotoImage(Image.open("assets/right.png"))
        label2 = ttk.Label(self, image=img)
        label2.image = img
        label2.grid(row=1, column=3)

        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=3, column=0, padx=10, pady=10)

        # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=3, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=3, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=3, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=3, column=4, padx=10, pady=10)


# helper function - update song
# same functionality as update destination function
def update_song(action, label):
    global song
    if action == "next":
        if song == len(playlist) - 1:
            song = 0
        else:
            song += 1
    else:
        if song == 0:
            song = len(playlist) - 1
        else:
            song -= 1
    artist = playlist[song].split(" - ")[0]
    song_title = playlist[song].split(" - ")[1]
    label.config(
        text=f"{artist} - {song_title}"
    )


# music frame
class Music(tk.Frame):

    def __init__(self, parent, main_frame):
        tk.Frame.__init__(self, parent)
        # display music title
        label = ttk.Label(self, text="Music", font=TITLEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # display song cover
        img = ImageTk.PhotoImage(Image.open("assets/bts.jpeg"))
        label2 = ttk.Label(self, image=img)
        label2.image = img
        label2.grid(row=1, column=2)

        # display current song
        song_label = ttk.Label(self, text="BTS - Dynamite", font=TITLEFONT)
        song_label.grid(row=2, column=2, padx=10, pady=10)

        # previous and next buttons to call update song function
        prev_button = ttk.Button(self, text="Prev",
                                 command=lambda: update_song("prev", song_label))
        prev_button.grid(row=1, column=0, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next",
                                 command=lambda: update_song("next", song_label))
        next_button.grid(row=1, column=4, padx=10, pady=10)

        # <------------------------------------- BUTTON SELECTION --------------------------------------->
        # button to first page
        button1 = ttk.Button(self, text="Directions",
                             command=lambda: main_frame.display_frame(Directions))
        button1.grid(row=3, column=0, padx=10, pady=10)

        # button to second page
        button2 = ttk.Button(self, text="Headlights",
                             command=lambda: main_frame.display_frame(Headlights))
        button2.grid(row=3, column=1, padx=10, pady=10)

        # button to third page
        button3 = ttk.Button(self, text="Speedometer",
                             command=lambda: main_frame.display_frame(Speedometer))
        button3.grid(row=3, column=2, padx=10, pady=10)

        # button to fourth page
        button4 = ttk.Button(self, text="Cameras",
                             command=lambda: main_frame.display_frame(Cameras))
        button4.grid(row=3, column=3, padx=10, pady=10)

        # button to fifth page
        button5 = ttk.Button(self, text="Music",
                             command=lambda: main_frame.display_frame(Music))
        button5.grid(row=3, column=4, padx=10, pady=10)


# Run window
app = AutovisApp()
app.mainloop()


