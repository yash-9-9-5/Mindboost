# Line 1-4: Importing required modules for GUI, styling, randomness, and timing
import tkinter as tk  # tkinter: Standard Python interface to the Tk GUI toolkit
from tkinter import ttk, messagebox, font  # ttk: themed widgets, messagebox: dialogs, font: font management
import random  # random: for selecting random thoughts
import time  # time: for animation timing

# Line 6: Define the main application class using OOP principles
class PositiveThoughtsApp:
    # Line 7-25: Constructor method initializes the app window, styles, data, and widgets
    def __init__(self, root):
        self.root = root  # Store the main Tkinter window instance
        self.root.title("MindBoost - Positive Affirmations")  # Set window title
        self.root.geometry("800x500")  # Set default window size
        self.root.minsize(700, 450)  # Set minimum window size
        self.root.configure(bg='#2A2A2A')  # Set background color
        
        # Line 13-20: Define a custom color scheme for consistent UI styling
        self.colors = {
            'background': '#2A2A2A',  # Main background color
            'primary': '#4A90E2',     # Primary accent color (buttons, headers)
            'secondary': '#6C5CE7',   # Secondary accent color (button hover)
            'accent': '#FF6B6B',      # Accent color (button pressed)
            'text': '#FFFFFF',        # Default text color
            'card_bg': '#363636'      # Card background color
        }
        
        # Line 22: Configure custom widget styles using ttk.Style
        self.configure_styles()
        
        # Line 24: Initialize the list of positive thoughts/affirmations
        self.thoughts = self.create_thoughts_list()
        
        # Line 26: Build and place all GUI widgets
        self.create_widgets()
        
        # Line 28: Schedule the first thought update (random thought display)
        self.update_thought()
        
        # Line 30-32: Keep window always on top and handle close event
        self.root.attributes('-topmost', False)  
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Custom close handler

    # Line 34-54: Method to configure custom styles for all widgets
    def configure_styles(self):
        style = ttk.Style()  # Create a style object
        style.theme_use('clam')  # Use 'clam' theme for modern look
        
        # Configure frame backgrounds
        style.configure('TFrame', background=self.colors['background'])
        style.configure('Card.TFrame', 
                       background=self.colors['card_bg'],
                       borderwidth=2,
                       relief='raised',
                       bordercolor='#404040')
        # Configure primary button style
        style.configure('Primary.TButton',
                       font=('Segoe UI', 12, 'bold'),
                       background=self.colors['primary'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       padding=10)
        style.map('Primary.TButton',
                 background=[('active', self.colors['secondary']),
                             ('pressed', self.colors['accent'])])
        # Configure label styles for quotes and headers
        style.configure('Quote.TLabel',
                        font=('Segoe UI', 14, 'italic'),
                        background=self.colors['card_bg'],
                        foreground=self.colors['text'],
                        wraplength=650,
                        padding=20)
        style.configure('Header.TLabel',
                       font=('Segoe UI', 24, 'bold'),
                       background=self.colors['background'],
                       foreground=self.colors['primary'])
        style.configure('Secondary.TLabel',
                       font=('Segoe UI', 10),
                       background=self.colors['background'],
                       foreground='#AAAAAA')

    # Line 56-250: Method to create and return the list of positive thoughts/quotes
    def create_thoughts_list(self):
        return [
            # Each string is a positive affirmation or motivational quote
            # ... (list of thoughts, see original code for full list)
            # Add your 250 thoughts here
            # ... (remaining thoughts)
        ]

    # Line 252-295: Method to create and place all GUI widgets
    def create_widgets(self):
        main_frame = ttk.Frame(self.root)  # Main container frame
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Padding for aesthetics
        
        # Header section with app title and status
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, 
                 text="🌟 MindBoost",
                 style='Header.TLabel').pack(side=tk.LEFT)  # App title
        
        self.status_label = ttk.Label(header_frame,
                                    text="Next refresh: 2:00:00",
                                    style='Secondary.TLabel')  # Countdown timer label
        self.status_label.pack(side=tk.RIGHT)
        
        # Card frame for displaying the current thought
        card_frame = ttk.Frame(main_frame, style='Card.TFrame')
        card_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.thought_label = ttk.Label(card_frame,
                                     style='Quote.TLabel',
                                     anchor=tk.CENTER)  # Label for the thought text
        self.thought_label.pack(fill=tk.BOTH, expand=True)
        
        # Control panel with refresh button and progress bar
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=20)
        
        self.refresh_btn = ttk.Button(control_frame,
                                    text="🔄 New Thought",
                                    style='Primary.TButton',
                                    command=self.update_thought)  # Button to get a new thought
        self.refresh_btn.pack(side=tk.RIGHT, ipadx=20)
        
        self.time_progress = ttk.Progressbar(control_frame,
                                          orient=tk.HORIZONTAL,
                                          length=200,
                                          mode='determinate')  # Progress bar for countdown
        self.time_progress.pack(side=tk.RIGHT, padx=20)
        
        self.time_remaining = 7200  # 2 hours in seconds for countdown
        self.update_progress()  # Start the countdown

    # Line 297-308: Method to update the progress bar and countdown timer
    def update_progress(self):
        progress_value = (7200 - self.time_remaining) / 72  # Calculate progress percentage
        self.time_progress['value'] = progress_value  # Update progress bar
        self.time_remaining -= 1  # Decrement timer
        if self.time_remaining <= 0:
            self.time_remaining = 7200  # Reset timer when it reaches zero
        mins, secs = divmod(self.time_remaining, 60)
        hours, mins = divmod(mins, 60)
        self.status_label.config(text=f"Next refresh: {hours:02}:{mins:02}:{secs:02}")  # Update label
        self.root.after(1000, self.update_progress)  # Schedule next update in 1 second

    # Line 310-312: Method to get a random thought from the list
    def get_random_thought(self):
        return random.choice(self.thoughts)  # Return a random thought

    # Line 314-318: Method to update the displayed thought and reset timer
    def update_thought(self):
        new_thought = self.get_random_thought()  # Get a new random thought
        self.animate_thought_change(new_thought)  # Animate the change
        self.time_remaining = 7200  # Reset timer

    # Line 320-336: Method to animate the transition between thoughts
    def animate_thought_change(self, new_thought):
        # Improved animation with valid color transitions
        original_bg = self.colors['card_bg']  # Card background color
        text_color = self.colors['text']  # Text color
        
        # Fade out effect by blending text color to background
        for i in range(10, 0, -1):
            blend = self.color_interpolate(text_color, original_bg, i/10)
            self.thought_label.configure(foreground=blend)
            self.root.update()
            time.sleep(0.03)
        
        self.thought_label.configure(text=new_thought)  # Update text
        
        # Fade in effect by blending background to text color
        for i in range(0, 11):
            blend = self.color_interpolate(original_bg, text_color, i/10)
            self.thought_label.configure(foreground=blend)
            self.root.update()
            time.sleep(0.03)
        
        self.thought_label.configure(foreground=text_color)  # Ensure final color is correct

    # Line 338-347: Helper function to interpolate between two hex colors
    def color_interpolate(self, start_hex, end_hex, factor):
        """Helper function for color transitions"""
        start = int(start_hex[1:], 16)  # Convert hex to int
        end = int(end_hex[1:], 16)
        
        r = int(((start >> 16) & 0xFF) * (1 - factor) + ((end >> 16) & 0xFF) * factor)
        g = int(((start >> 8) & 0xFF) * (1 - factor) + ((end >> 8) & 0xFF) * factor)
        b = int((start & 0xFF) * (1 - factor) + (end & 0xFF) * factor)
        return f'#{r:02x}{g:02x}{b:02x}'  # Return blended color as hex string

    # Line 349-354: Handler for window close event
    def on_close(self):
        self.root.attributes('-topmost', False)  # Remove always-on-top before closing
        if messagebox.askokcancel("Quit", "Do you want to close MindBoost?"):
            self.root.destroy()  # Close the app if user confirms

# Line 356-361: Main entry point for the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Segoe UI", size=10)  # Set default font for consistency
    app = PositiveThoughtsApp(root)  # Instantiate the app class
    root.mainloop()  # Start the Tkinter event loop