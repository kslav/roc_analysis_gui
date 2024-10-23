import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import os
import datetime
import numpy as np
import tkinter as tk
from tkinter import filedialog, IntVar, Checkbutton

def load_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx")])
    input_entry.delete(0, tk.END)  # Clear current text
    input_entry.insert(0, file_path)  # Insert the selected file path

def select_save_folder():
    global save_path
    save_path = filedialog.askdirectory(title="Select Save Folder")
    output_entry.delete(0, tk.END)  # Clear current text
    output_entry.insert(0, save_path)  # Insert the selected folder path

def compute_roc():
    global save_plot, show_plot
    save_plot = save_plot_var.get()
    show_plot = show_plot_var.get()

    data_dict = pd.read_excel(file_path, sheet_name=None)  # Load all sheets
    sheets = list(data_dict.keys())  # Get all sheet names
    print(sheets)

    for sheet in sheets:
        print(f"Computing ROC for {sheet}")
        data = data_dict[sheet]
        y_true = data['Actual'].dropna()
        y_scores = data['Confidence'].dropna()

        fpr, tpr, thresholds = roc_curve(y_true, y_scores)
        roc_auc = auc(fpr, tpr)

        J = tpr - fpr
        optimal_idx = np.argmax(J)

        plt.figure()
        plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.scatter(fpr[optimal_idx], tpr[optimal_idx], color='red')
        plt.plot([0, 1], [0, 1], color='red', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f"ROC Curve - {sheet}")
        plt.legend(loc='lower right')
        plt.gca().set_aspect('equal')

        if save_plot:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            plt.savefig(os.path.join(save_path, f"{sheet}_{timestamp}.png"))

    if show_plot:
        plt.show()

# Create a basic GUI
master = tk.Tk()
master.title("ROC Analysis")
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Select Excel File:")
input_entry = tk.Entry(top_frame, width=40)  # Entry for the input file path
browse1 = tk.Button(top_frame, text="Browse", command=load_file)

output_path = tk.Label(bottom_frame, text="Select Folder in Which to Save Outputs:")
output_entry = tk.Entry(bottom_frame, width=40)  # Entry for the output folder path
browse2 = tk.Button(bottom_frame, text="Browse", command=select_save_folder)

save_plot_var = IntVar()
check_save_plot = Checkbutton(bottom_frame, text="Save Plots", variable=save_plot_var)
show_plot_var = IntVar()
check_show_plot = Checkbutton(bottom_frame, text="Show Plots", variable=show_plot_var)

begin_button = tk.Button(bottom_frame, text='Run ROC Analysis!', command=compute_roc)

# Pack widgets
top_frame.pack(side=tk.TOP, padx=10, pady=10)
bottom_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
line.pack(pady=10)

# Pack input path components
input_path.pack(padx=5)
input_entry.pack(padx=5)
browse1.pack(padx=5)

# Pack output path components
output_path.pack(padx=5)
output_entry.pack(padx=5)
browse2.pack(padx=5)

# Pack checkboxes and buttons
check_save_plot.pack(pady=5)
check_show_plot.pack(pady=5)
begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
