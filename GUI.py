#import libraries
import sys
import tkinter as tk
import csv
import matplotlib.pyplot as plt
import requests
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



# Create a window
root = tk.Tk()
root.title("Airport Analyzer")

data_selection_frame = tk.Frame(root)
data_selection_frame.pack(pady=10)

airport_loc_label = tk.Label(data_selection_frame, text="Select airport location:")
airport_loc_label.pack(side=tk.LEFT)

airport_loc_options = ["All", "Name", "TotalSeats", "Country Name"]
airport_loc_combobox = tk.ttk.Combobox(data_selection_frame, values=airport_loc_options)
airport_loc_combobox.pack(side=tk.LEFT)

# Button for visualization
generate_visualization_button = tk.Button(data_selection_frame, text="Generate Visualization", command=generate_visualization)
generate_visualization_button.pack()


visualization_frame = tk.Frame(root)
visualization_frame.pack(pady=20)

# Canvas for visualization
visualization_canvas = tk.Canvas(visualization_frame, width=500, height=400)
visualization_canvas.pack()

    visualization_canvas.delete('all')
    visualization_canvas.create_image(200, 150, image=visualization)

def airport_data():
   
    data = pd.read_csv('airport_volume_airport_locations.csv')
    return data

def create_visualization(data):
    
    pie_chart = plt.pie(data['locations'].value_counts())
    plt.title('Airport location')
    plt.show()

root.mainloop()


    def fetch(self, dataset):
        

        api_url = f"https://www.kaggle.com/datasets/zvr842/all-global-airports"
        response = requests.get(api_url)



    def plot_data(self, data):
        

        x_values = list(range(len(data)))
        y_values = [item['value'] for item in data]

        figure, ax = plt.subplots()
        ax.plot(x, y, label="Values")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
    
    def clear_data(self):
        self.airport_data = None
        self.airport_list_widget.clear()
        self.details_table.setRowCount(0)
        self.ax.clear()
        self.canvas.draw()
        self.update_status_bar('Data cleared successfully.')

        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=2, column=0, columnspan=2, pady=10)

   