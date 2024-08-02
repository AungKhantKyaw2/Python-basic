
# from tkinter import *
# import time

# def start_countdown():
#     global countdown_time
#     try:
#         # Get input values and convert them to integers
#         hours = int(hours_entry.get())
#         minutes = int(minutes_entry.get())
#         seconds = int(seconds_entry.get())
        
#         # Validate input values
#         if hours < 0 or minutes < 0 or seconds < 0:
#             countdown_label.config(text="Please enter non-negative values.")
#             return
        
#         # Calculate total countdown time in seconds
#         countdown_time = hours * 3600 + minutes * 60 + seconds
        
#         # Disable input fields and button
#         submit_button.config(state="disabled")
#         hours_entry.config(state="disabled")
#         minutes_entry.config(state="disabled")
#         seconds_entry.config(state="disabled")
        
#         # Start the countdown
#         update()
#     except ValueError:
#         countdown_label.config(text="Please enter valid integers.")

# def update():
#     global countdown_time
#     if countdown_time > 0:
#         # Calculate hours, minutes, and seconds for display
#         hours = countdown_time // 3600
#         minutes = (countdown_time % 3600) // 60
#         seconds = countdown_time % 60
        
#         # Update the countdown label
#         countdown_label.config(text=f"Countdown: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
#         # Decrement the countdown time
#         countdown_time -= 1
        
#         # Schedule the next update
#         countdown_label.after(1000, update)
#     else:
#         countdown_label.config(text="Time's up!")
#         # Re-enable input fields and button
#         submit_button.config(state="normal")
#         hours_entry.config(state="normal")
#         minutes_entry.config(state="normal")
#         seconds_entry.config(state="normal")

# # Create the main window
# window = Tk()
# window.title("Countdown Timer")



# # Countdown input frame
# countdown_input = Frame(window)
# countdown_input.pack()

# # Hours input
# hours_label = Label(countdown_input, text="Hours:")
# hours_label.grid(row=0, column=0)
# hours_entry = Entry(countdown_input, width=3)
# hours_entry.grid(row=0, column=1)

# # Minutes input
# minutes_label = Label(countdown_input, text="Minutes:")
# minutes_label.grid(row=0, column=2)
# minutes_entry = Entry(countdown_input, width=3)
# minutes_entry.grid(row=0, column=3)

# # Seconds input
# seconds_label = Label(countdown_input, text="Seconds:")
# seconds_label.grid(row=0, column=4)
# seconds_entry = Entry(countdown_input, width=3)
# seconds_entry.grid(row=0, column=5)

# # Submit button
# submit_button = Button(countdown_input, text="Start Countdown", command=start_countdown)
# submit_button.grid(row=0, column=6)

# # Countdown label
# countdown_label = Label(window, font=('Arial', 25), fg="red", bg='black')
# countdown_label.pack()

# # Start the Tkinter main loop
# window.mainloop()
