import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hexagon(x, y, size):
    """Generate hexagon coordinates."""
    angles = np.linspace(0, 2 * np.pi, 7)
    return x + size * np.cos(angles), y + size * np.sin(angles)

def plot_clusters(cluster_size):
    """Plot the frequency reuse cell clusters with green and yellow colors."""
    fig, ax = plt.subplots(figsize=(6, 6))
    size = 10
    colors = ["green", "yellow"]  # Only 2 colors for clusters
    
    cell_count = 1  # Start cell numbering

    for i in range(-cluster_size, cluster_size + 1):
        for j in range(-cluster_size, cluster_size + 1):
            x = i * 1.5 * size
            y = j * np.sqrt(3) * size + (i % 2) * (np.sqrt(3) / 2 * size)
            cluster_id = (i + j) % 2  # Alternating clusters
            color = colors[cluster_id]  
            
            # Draw hexagon
            ax.fill(*hexagon(x, y, size), color=color, edgecolor='black')
            
            # Display cell number at center of hexagon
            text_color = "white" if color == "green" else "black"
            ax.text(x, y, str(cell_count), ha='center', va='center', fontsize=10, color=text_color, fontweight='bold')

            cell_count += 1  # Increment cell count

    ax.set_xlim(-cluster_size * 15, cluster_size * 15)
    ax.set_ylim(-cluster_size * 15, cluster_size * 15)
    ax.set_aspect('equal')
    ax.axis("off")
    return fig

def update_plot():
    """Update the plot based on user input."""
    try:
        cluster_size = int(cluster_size_var.get())
        if cluster_size < 1:
            error_label.config(text="Please enter a positive integer")
            return

        for widget in plot_frame.winfo_children():
            widget.destroy()
        
        fig = plot_clusters(cluster_size)
        new_canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        new_canvas.get_tk_widget().pack()
        new_canvas.draw()

        error_label.config(text="")  
    except ValueError:
        error_label.config(text="Please enter a valid number")

# GUI Setup
root = tk.Tk()
root.title("Cell Clustering - Frequency Reuse")

frame = ttk.Frame(root, padding=10)
frame.pack()

# Cluster Size Input
cluster_size_var = tk.StringVar(value="3")
ttk.Label(frame, text="Cluster Size:").grid(row=0, column=0)
ttk.Entry(frame, textvariable=cluster_size_var, width=5).grid(row=0, column=1)
ttk.Button(frame, text="Update", command=update_plot).grid(row=0, column=2)

error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=1, column=0, columnspan=3)

# Plot Frame
plot_frame = ttk.Frame(root)
plot_frame.pack()

# Initial Plot
fig = plot_clusters(int(cluster_size_var.get()))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack()
canvas.draw()

root.mainloop()