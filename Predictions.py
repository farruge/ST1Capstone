# Using a GUI version, create a Wine Quality Predictor

import tkinter
import pickle

class MyGUI:
    def __init__(self):
    # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Wine Quality Predictor")
    # create frames to group widgets
        self.first_frame = tkinter.Frame()
        self.second_frame = tkinter.Frame()
        self.third_frame = tkinter.Frame()
        self.fourth_frame = tkinter.Frame()
        self.fifth_frame = tkinter.Frame()
        self.sixth_frame = tkinter.Frame()
        self.seventh_frame = tkinter.Frame()
        self.eighth_frame = tkinter.Frame()
        self.ninth_frame = tkinter.Frame()
        self.tenth_frame = tkinter.Frame()
        self.eleventh_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=10, width=40)

    # create the widgets to get the input chemical components
        FixAc_label = tkinter.Label(self.first_frame, text="Enter Fixed Acidity: ")
        FixAc_label.pack(side='left')
        self.FixAc_entry = tkinter.Entry(self.first_frame, bg='light grey', bd=2, width=10)
        self.FixAc_entry.pack(side='right')
        VolAc_label = tkinter.Label(self.second_frame, text="Enter Volatile Acidity: ")
        VolAc_label.pack(side='left')
        self.VolAc_entry = tkinter.Entry(self.second_frame, bg='light grey', bd=2, width=10)
        self.VolAc_entry.pack(side='right')
        CitAc_label = tkinter.Label(self.third_frame, text="Enter Citric Acid: ")
        CitAc_label.pack(side='left')
        self.CitAc_entry = tkinter.Entry(self.third_frame, bg='light grey', bd=2, width=10)
        self.CitAc_entry.pack(side='right')
        ResSug_label = tkinter.Label(self.fourth_frame, text="Enter Residual Sugar: ")
        ResSug_label.pack(side='left')
        self.ResSug_entry = tkinter.Entry(self.fourth_frame, bg='light grey', bd=2, width=10)
        self.ResSug_entry.pack(side='right')
        Chlo_label = tkinter.Label(self.fifth_frame, text="Enter Chlorides: ")
        Chlo_label.pack(side='left')
        self.Chlo_entry = tkinter.Entry(self.fifth_frame, bg='light grey', bd=2, width=10)
        self.Chlo_entry.pack(side='right')
        FreeS2_label = tkinter.Label(self.sixth_frame, text="Enter Free Sulfur Dioxide: ")
        FreeS2_label.pack(side='left')
        self.FreeS2_entry = tkinter.Entry(self.sixth_frame, bg='light grey', bd=2, width=10)
        self.FreeS2_entry.pack(side='right')
        TotS2_label = tkinter.Label(self.seventh_frame, text="Enter Total Sulfur Dioxide: ")
        TotS2_label.pack(side='left')
        self.TotS2_entry = tkinter.Entry(self.seventh_frame, bg='light grey', bd=2, width=10)
        self.TotS2_entry.pack(side='right')
        Density_label = tkinter.Label(self.eighth_frame, text="Enter Density: ")
        Density_label.pack(side='left')
        self.Density_entry = tkinter.Entry(self.eighth_frame, bg='light grey', bd=2, width=10)
        self.Density_entry.pack(side='right')
        pH_label = tkinter.Label(self.ninth_frame, text="Enter pH: ")
        pH_label.pack(side='left')
        self.pH_entry = tkinter.Entry(self.ninth_frame, bg='light grey', bd=2, width=10)
        self.pH_entry.pack(side='right')
        Sulph_label = tkinter.Label(self.tenth_frame, text="Enter Sulphates: ")
        Sulph_label.pack(side='left')
        self.Sulph_entry = tkinter.Entry(self.tenth_frame, bg='light grey', bd=2, width=10)
        self.Sulph_entry.pack(side='right')
        Alco_label = tkinter.Label(self.eleventh_frame, text="Enter Alcohol: ")
        Alco_label.pack(side='left')
        self.Alco_entry = tkinter.Entry(self.eleventh_frame, bg='light grey', bd=2, width=10)
        self.Alco_entry.pack(side='right')

    # create the widgets for the buttons
        calc_button = tkinter.Button(self.button_frame, text="Calculate Quality", command=self.calc_quality)
        quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='top')

    # create the multi-line  text area and pack it using tkinter.Text

        self.result_ta.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()
        self.seventh_frame.pack()
        self.eighth_frame.pack()
        self.ninth_frame.pack()
        self.tenth_frame.pack()
        self.eleventh_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
    # enter the tkinter main loop so that graphic is visible
        tkinter.mainloop()

    # do the wine quality prediction  - TO BE DONE
    def calc_quality(self):
        if (float(self.FixAc_entry.get()) < 0) or \
            (float(self.VolAc_entry.get()) < 0) or \
            (float(self.CitAc_entry.get()) < 0) or \
            (float(self.ResSug_entry.get()) < 0) or \
            (float(self.Chlo_entry.get()) < 0) or \
            (float(self.FreeS2_entry.get()) < 0) or \
            (float(self.TotS2_entry.get()) < 0) or \
            (float(self.Density_entry.get()) < 0) or \
            (float(self.pH_entry.get()) < 0) or \
            (float(self.Sulph_entry.get()) < 0) or \
            (float(self.Alco_entry.get()) < 0):
            self.result_ta.delete('1.0', tkinter.END)
            self.result_ta.insert("1.0", "All component levels must be greater than 0. \n  Please review the results.")
        else:
            # load model
            with open("winequality_predictor.h5", 'rb') as file:
                loaded_model = pickle.load(file)
            input_array = [float(self.FixAc_entry.get()), float(self.VolAc_entry.get()), float(self.CitAc_entry.get()),
                            float(self.ResSug_entry.get()), float(self.Chlo_entry.get()), float(self.FreeS2_entry.get()),
                            float(self.TotS2_entry.get()), float(self.Density_entry.get()), float(self.pH_entry.get()),
                            float(self.Sulph_entry.get()), float(self.Alco_entry.get())]
            prediction = loaded_model.predict([input_array])
            self.result_ta.delete("1.0", tkinter.END)
            self.result_ta.insert("1.0", "Predicted wine quality is: " + str(prediction))



my_gui = MyGUI()