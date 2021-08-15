import tkinter as tk
def main():
    #callback function to draw grids on the cavas when the event occures
    def make_grid(event=None):
        width = canvas.winfo_width() # Get current width of canvas
        height = canvas.winfo_height() # Get current height of canvas

        # here we draw all vertical lines 
        for i in range(0, width ,size_of_squares,):
            canvas.create_line([(i, 0), (i, height)], tag='grid_line')

        # here we draw all horizontal lines
        for i in range(0, height, size_of_squares):
            canvas.create_line([(0, i), (width, i)], tag='grid_line')

    #here we read the window size .int() is used to convert it to integer 
    window_size=int(input("what should be the size of the window in pixels?:"))
    #here we read the square size
    size_of_squares=int(input("Enter the size of squares in the sheet:"))
    root = tk.Tk()
    #setting the title for the root window
    root.title("Cuadricula")
    canvas= tk.Canvas(root, height=window_size, width=window_size, bg='white')#since we use square grid we use both height and widith for the widow same
    #we tell the cavas to fit into the parent window both vertically and horrizondally
    canvas.pack(fill=tk.BOTH, expand=True)
    # <Configure> is an event which is triggered when the object chages the size
    # we are specifying a callback function to draw lines when the even occure
    canvas.bind('<Configure>', make_grid)
    root.mainloop()
main()
