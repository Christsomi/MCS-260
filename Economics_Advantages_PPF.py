import tkinter as tk
import matplotlib.pyplot as plt

def submit():
    mpl_country_one_good1 = float(mpl_entry_country_one_good1.get())
    mpl_country_two_good1 = float(mpl_entry_country_two_good1.get())
    mpl_country_one_good2 = float(mpl_entry_country_one_good2.get())
    mpl_country_two_good2 = float(mpl_entry_country_two_good2.get())
    labor_country_one = float(labor_entry_country_one.get())
    labor_country_two = float(labor_entry_country_two.get())
    
    if mpl_country_one_good1 == mpl_country_two_good1 == mpl_country_one_good2 == mpl_country_two_good2:
        error_label.config(text="Error: All MPL values are the same.")
        return
    
    if labor_country_one == 0 or labor_country_two == 0:
        error_label.config(text="Error: Labor input cannot be 0.")
        return

    update_absolute_advantage_message(mpl_country_one_good1, mpl_country_two_good1, mpl_country_one_good2, mpl_country_two_good2)
    
    update_comparative_advantage_message(mpl_country_one_good1, mpl_country_two_good1, mpl_country_one_good2, mpl_country_two_good2)

    country_one_good1_intercept = mpl_country_one_good1 * labor_country_one
    country_one_good2_intercept = mpl_country_one_good2 * labor_country_one

    country_two_good1_intercept = mpl_country_two_good1 * labor_country_two
    country_two_good2_intercept = mpl_country_two_good2 * labor_country_two

    draw_ppf(country_one_good1_intercept, country_one_good2_intercept, country_two_good1_intercept, country_two_good2_intercept)

    error_label.config(text="")

def update_absolute_advantage_message(mpl_country_one_good1, mpl_country_two_good1, mpl_country_one_good2, mpl_country_two_good2):
    absolute_advantage_message = ""
    
    if mpl_country_one_good1 > mpl_country_two_good1 and mpl_country_one_good2 > mpl_country_two_good2:
        absolute_advantage_message = "Country 1 has an absolute advantage in both Good 1 and Good 2."
    elif mpl_country_two_good1 > mpl_country_one_good1 and mpl_country_two_good2 > mpl_country_one_good2:
        absolute_advantage_message = "Country 2 has an absolute advantage in both Good 1 and Good 2."
    elif mpl_country_one_good1 > mpl_country_two_good1 and mpl_country_two_good2 > mpl_country_one_good2:
        absolute_advantage_message = "Country 1 has an absolute advantage in Good 1, and Country 2 has an absolute advantage in Good 2."
    elif mpl_country_one_good2 > mpl_country_two_good2 and mpl_country_two_good1 > mpl_country_one_good1:
        absolute_advantage_message = "Country 1 has an absolute advantage in Good 2, and Country 2 has an absolute advantage in Good 1."
    elif mpl_country_one_good1 == mpl_country_two_good1 and mpl_country_one_good2 > mpl_country_two_good2:
        absolute_advantage_message = "No one has an absolute advantage in Good 1, but Country 1 has an absolute advantage in Good 2."
    elif mpl_country_one_good1 == mpl_country_two_good1 and mpl_country_two_good2 > mpl_country_one_good2:
        absolute_advantage_message = "No one has an absolute advantage in Good 1, but Country 2 has an absolute advantage in Good 2."
    elif mpl_country_one_good2 == mpl_country_two_good2 and mpl_country_one_good1 > mpl_country_two_good1:
        absolute_advantage_message = "Country 1 has an absolute advantage in Good 1, and no one has an absolute advantage in Good 2."
    elif mpl_country_one_good2 == mpl_country_two_good2 and mpl_country_two_good1 > mpl_country_one_good1:
        absolute_advantage_message = "Country 2 has an absolute advantage in Good 1, and no one has an absolute advantage in Good 2."
    elif mpl_country_one_good2 == mpl_country_two_good2 and mpl_country_two_good1 == mpl_country_one_good1:
        absolute_advantage_message = "No one has an absolute advantage."
    
    absolute_advantage_label.config(text=absolute_advantage_message)

def update_comparative_advantage_message(mpl_country_one_good1, mpl_country_two_good1, mpl_country_one_good2, mpl_country_two_good2):
    country_one_mpl_ratio = mpl_country_one_good1 / mpl_country_one_good2
    country_two_mpl_ratio = mpl_country_two_good1 / mpl_country_two_good2

    comparative_advantage_message = ''
    if country_one_mpl_ratio > country_two_mpl_ratio:
        comparative_advantage_message += "Country 1 has a comparative advantage in Good 1.\n"
        comparative_advantage_message += "Country 2 has a comparative advantage in Good 2."
    else:
        comparative_advantage_message += "Country 1 has a comparative advantage in Good 2.\n"
        comparative_advantage_message += "Country 2 has a comparative advantage in Good 1."

    comparative_advantage_label.config(text=comparative_advantage_message)

def draw_ppf(country_one_good1_intercept, country_one_good2_intercept, country_two_good1_intercept, country_two_good2_intercept):
   
    plt.plot([0, country_one_good1_intercept], [country_one_good2_intercept, 0], label='Country 1 PPF')
    plt.plot([0, country_two_good1_intercept], [country_two_good2_intercept, 0], label='Country 2 PPF')
    plt.xlabel('Good 1')
    plt.ylabel('Good 2')
    plt.title('Production Possibility Frontier (PPF)')
    plt.legend()
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("Trade model")


mpl_label = tk.Label(root, text="Input MPLs", font=('Arial', 8, 'bold'))
mpl_label.grid(row=0, columnspan=2)

mpl_label_country_one_good1 = tk.Label(root, text="Country 1, Good 1:")
mpl_label_country_one_good1.grid(row=1, column=0)
mpl_entry_country_one_good1 = tk.Entry(root)
mpl_entry_country_one_good1.grid(row=2, column=0)

mpl_label_country_two_good1 = tk.Label(root, text="Country 2, Good 1:")
mpl_label_country_two_good1.grid(row=1, column=1)
mpl_entry_country_two_good1 = tk.Entry(root)
mpl_entry_country_two_good1.grid(row=2, column=1)

mpl_label_country_one_good2 = tk.Label(root, text="Country 1, Good 2:")
mpl_label_country_one_good2.grid(row=3, column=0)
mpl_entry_country_one_good2 = tk.Entry(root)
mpl_entry_country_one_good2.grid(row=4, column=0)

mpl_label_country_two_good2 = tk.Label(root, text="Country 2, Good 2:")
mpl_label_country_two_good2.grid(row=3, column=1)
mpl_entry_country_two_good2 = tk.Entry(root)
mpl_entry_country_two_good2.grid(row=4, column=1)

labor_label_country_one = tk.Label(root, text="Country 1, Labor:")
labor_label_country_one.grid(row=5, column=0)
labor_entry_country_one = tk.Entry(root)
labor_entry_country_one.grid(row=6, column=0)

labor_label_country_two = tk.Label(root, text="Country 2, Labor:")
labor_label_country_two.grid(row=5, column=1)
labor_entry_country_two = tk.Entry(root)
labor_entry_country_two.grid(row=6, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=7, columnspan=2)

absolute_advantage_label = tk.Label(root, text="")
absolute_advantage_label.grid(row=8, columnspan=2)

comparative_advantage_label = tk.Label(root, text="")
comparative_advantage_label.grid(row=9, columnspan=2)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=10, columnspan=2)

root.mainloop()
