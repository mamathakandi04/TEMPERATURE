import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        unit = var.get()

        if unit == "Celsius":
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15
            label_result.config(text=f"{temperature} degrees Celsius = {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin")
        elif unit == "Fahrenheit":
            celsius = (temperature - 32) * 5/9
            kelvin = (temperature - 32) * 5/9 + 273.15
            label_result.config(text=f"{temperature} degrees Fahrenheit = {celsius} degrees Celsius and {kelvin} Kelvin")
        elif unit == "Kelvin":
            celsius = temperature - 273.15
            fahrenheit = (temperature - 273.15) * 9/5 + 32
            label_result.config(text=f"{temperature} Kelvin = {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit")
    except ValueError:
        label_result.config(text="Please enter a valid temperature!")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create a label and entry for temperature input
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack()
entry_temp = tk.Entry(root)
entry_temp.pack()

# Create a radio button for unit selection
var = tk.StringVar()
var.set("Celsius")
label_units = tk.Label(root, text="Select Unit:")
label_units.pack()

units = ["Celsius", "Fahrenheit", "Kelvin"]
for unit in units:
    rb = tk.Radiobutton(root, text=unit, variable=var, value=unit)
    rb.pack()

# Create a button to perform conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()