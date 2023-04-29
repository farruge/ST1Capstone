# Using a GUI version, get student information

import tkinter


class MyGUI:
    def __init__(self):
    # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Student Details")
    # create frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
    # create the widgets for the top frame to get the name
        name_label = tkinter.Label(self.top_frame, text="Enter Student Name ")
        self.name_entry = tkinter.Entry(self.top_frame, bg='light blue', bd=2, width=10)
        name_label.pack(side='left')
        self.name_entry.pack(side='left')
    # create widgets for the address to be entered
        street_label = tkinter.Label(self.mid_frame, text="Enter Street Number and Name:  ")
        self.street_entry = tkinter.Entry(self.mid_frame, bg='orange', bd=2, width=25)
        street_label.pack(side='left')
        self.street_entry.pack(side='left')
        suburb_label = tkinter.Label(self.mid_frame, text="Enter Suburb Name:  ")
        self.suburb_entry = tkinter.Entry(self.mid_frame, bg='orange', bd=2, width=10)
        suburb_label.pack(side='left')
        self.suburb_entry.pack(side='left')
        state_label = tkinter.Label(self.mid_frame, text="Enter State Name:  ")
        self.state_entry = tkinter.Entry(self.mid_frame, bg='orange', bd=2, width=10)
        state_label.pack(side='left')
        self.state_entry.pack(side='left')
        postcode_label = tkinter.Label(self.mid_frame, text="Enter Post code:  ")
        self.postcode_entry = tkinter.Entry(self.mid_frame, bg='orange', bd=2, width=10)
        postcode_label.pack(side='left')
        self.postcode_entry.pack(side='left')
    # create widgets for the phone number and course to be entered
        phone_label = tkinter.Label(self.bottom_frame, text="Enter Phone Number and Name:  ")
        self.phone_entry = tkinter.Entry(self.bottom_frame, bg='orange', bd=2, width=25)
        phone_label.pack(side='left')
        self.phone_entry.pack(side='left')
        course_label = tkinter.Label(self.bottom_frame, text="Enter Course Name:  ")
        self.course_entry = tkinter.Entry(self.bottom_frame, bg='orange', bd=2, width=10)
        course_label.pack(side='left')
        self.course_entry.pack(side='left')
    # create the widgets for the buttons
        calc_button = tkinter.Button(self.button_frame, text="Display details", command=self.display_details)
        quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')
        # create the multi-line text area and pack it using tkinter.Text
        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=10, width=80)
        self.result_ta.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        # enter the tkinter main loop so that graphic is visible
        tkinter.mainloop()

    # Create print details method accessed by display details button
    def display_details(self):
        self.result_ta.delete('1.0', tkinter.END)
        self.result_ta.insert('1.0', "Name: " + self.name_entry.get())
        self.result_ta.insert('2.0', "\nStreet: " + self.street_entry.get())
        self.result_ta.insert('3.0', "\nSuburb, State and Postcode: " + self.suburb_entry.get() + ", " +
            self.state_entry.get() + " " + self.postcode_entry.get())
        self.result_ta.insert('4.0', "\nPhone number: " + self.phone_entry.get())
        self.result_ta.insert('5.0', "\nCourse name: " + self.course_entry.get())


my_gui = MyGUI()
