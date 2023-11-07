"""Contain definition for a GUI that demonstrates searching capabilities."""

import random
import tkinter as tk
from tkinter import messagebox

# This uses the same gui you used, but I implemented binary search instead. 

class SortGui:
    """Create a GUI that can be manipulated to show binary searching algorithm."""

    def __init__(self, initial_values: list[int]) -> None:
        """Create a canvas of rectangles that can later be highlighted and un-highlighted as needed later."""

        self.values = sorted(initial_values) # sort data for binary search

        # A list of indices that are related to the canvas rectangles created later in this code.
        self.rectangle_indices = []

        # Indicates the "status" of the rectangles, for example, green is a matched value, yellow is a values not yet checked, and red is a checked value that is a non-match.
        self.matched_value_highlight = "green"
        self.unseen_value_highlight = "yellow"
        self.seen_value_highlight = "orange"
        self.incorrect_value_highlight = "red"


        # create toplevel
        self.root = tk.Tk()

        # create canvas to display results
        self.canvas = tk.Canvas(self.root, height=600, width=800, bg="lightgray")
        self.canvas.grid(row=0, column=0)

        # create entry for user input, to be used for seraching algorithms
        self.search_input = tk.Entry(self.root)
        self.search_input.grid(row=1, column=0)

        # create button to later start the search process
        self.start_search_button = tk.Button(self.root, text="start search", command=self.search)
        self.start_search_button.grid(row=1, column=1)

        # initialize rectangles on GUI
        self.rect_width = 20

        self.x_offset = 10 # buffer between left edge of canvas and first rectangle
        self.x_step = self.rect_width + 5 # horizontal spacing between rectangles

        self.y_offset = 10 # buffer between top edge of canvas and rectangles
        self.value_multiplier = 5 # multiplier of value to determine rectangle height

        # Draw some rectangles based on the initial_values list and append the index returned to the rectangle_indices.
        for index,value in enumerate(self.values):
            x0 = self.x_offset + self.x_step * index
            y0 = self.y_offset # a bit useless
            x1 = x0 + self.rect_width
            y1 = y0 + value * self.value_multiplier
            
            self.rectangle_indices.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.unseen_value_highlight))

    def mainloop(self):
        """Pass mainloop call on to this GUI's Toplevel object."""
        self.root.mainloop()
    
    def search(self):
        """Find all instances of rectangles.
        
            Find all instances of rectangles with a height dteermined by a user-selected
              value in this object's canvas and highlight them.

            parameters: none
            return: none
        """

        # grab search candidate
        candidate = self.search_input.get()
        try:
            candidate = int(candidate)
        except ValueError:
            messagebox.showinfo(title="Alert!?!", message=f"{candidate} is an invalid value, try again")
            print(f"{candidate} is an invalid value, try again")

        left = 0
        right = len(self.values) - 1

        found = False

        while left <= right:
            
            mid = (left + right ) // 2
            delay = 100 * mid
            
            if self.values[mid] == candidate:
                self.canvas.itemconfig(mid, fill=self.matched_value_highlight)
                self.root.after(delay, self.root.update())
                found = True
                break
            
            elif self.values[mid] < candidate:

                for i in range(0, mid):
                    self.canvas.itemconfig(i, fill=self.incorrect_value_highlight)

                left = mid + 1
                self.canvas.itemconfig(mid, fill=self.seen_value_highlight)
                self.root.after(delay, self.root.update())

            else:
                for i in range(mid, len(self.values) + 1):
                    self.canvas.itemconfig(i, fill=self.incorrect_value_highlight)

                right = mid - 1
                self.canvas.itemconfig(mid, fill=self.seen_value_highlight)
                self.root.after(delay, self.root.update())
        
        if not found:
            for i in range(len(self.values) + 1):
                self.canvas.itemconfig(i, fill=self.incorrect_value_highlight)



rando_list = []
for i in range(31):
    rando_list.append(random.randint(1, 31))
sg = SortGui(rando_list)
sg.mainloop()