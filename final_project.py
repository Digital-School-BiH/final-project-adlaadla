import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("900x600")
root.title("are they fair?")
root.resizable()
root.config(bg="#ABE96D")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)

dscLabel= tk.Label(root, text="   Are the brands you buy from working ethically? Find out here!   ",
                   bg="#DEFFAD", fg="black", font=("Arial", 10) )
dscLabel.grid(column=0, row=0, sticky=tk.W, padx=15, pady=10)

bnLabel= tk.Label(root, text="   enter the brand name:   ",bg="#DEFFAD", fg="black", font=("Arial", 10) )
bnLabel.grid(column=0, row=2, sticky=tk.W, padx=15, pady=10)

entry= tk.Entry(root, width=30)
entry.grid(column=1, row=2, sticky=tk.W, padx=15, pady=10)

logo_image = Image.open("logo.png")
logo_image = logo_image.resize((100, 100))  
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="#ABE96D")
logo_label.image = logo_photo  
logo_label.grid(row=0, column=3, padx=15, pady=10, sticky="w")


def see_sources():
    sources = (
        "Sources:\n"
        "https://www.sustainably-chic.com/blog/fast-fashion-brands-to-avoid", " ",
                   "https://sustainablebusinessunion.com/20-most-unethical-companies/", " ",
        "https://goodonyou.eco/best-and-worst-beauty-brands-2024/", " ",
        "https://www.sustainably-chic.com/blog/fast-fashion-brands-to-avoid"

    )
    result_label.config(text=sources)

def reccs():
    reccs = (
        "Recommendations to be more ethical:\n"
        "Use products that: "
        "are cruelty-free, "
        "fair trade, "
        "don't contain palm oil, "
        "aren't fast fashion \n"
        "use the same phone until it's really broken and not useable, \n"
        "buy clothes at a thrift store and use them longer, \n"
        "recycle"

        )
    result_label.config(text=reccs)

def cr():
    cr = (
        "this was made by Adla Mahmutovic as the final project for "
        "the python course in digital school (April2025)"
        )
    result_label.config(text=cr)

def gd():
    gd = (
        "the grading goes from 1 to 5, 1 being very ethical, and 5 being HORRIBLE"
        )
    result_label.config(text=gd)

def lg():
    lg = (
        "the logo was made using canva and is inspired by the fair trade logo"
        )
    result_label.config(text=lg)

def get_brands():
    list_brands = []
    with open("brands.txt") as file:
        for line in file:
            line = line.strip()
            if "/" in line:
                pt = line.split("/", 1)
                if len(pt) == 2:
                    brand, reason = pt
                    list_brands.append((brand.strip(), reason.strip()))
    return list_brands

def write_to_file(brand, reason):
    with open('brands.txt', 'a') as file:
        file.write ("\n" + brand + "/" + reason)


def check_brand():
    brand_entered = entry.get().strip().lower()
    found = False
    for brand, reason in get_brands():
        if brand.lower() == brand_entered:
            result_label.config(text=f"{brand.title()}:\n{reason}")
            found = True
            break
    if not found:
        result_label.config(text="Sorry, brand not found.")

bButton = tk.Button(root, text="Check", bg="#DEFFAD", fg="black", font=("Arial", 10), command=check_brand)
bButton.grid(column=1, row=3, sticky=tk.W, padx=15, pady=10)

sButton = tk.Button(root, text="Source", bg="#DEFFAD", fg="black", font=("Arial", 10), command=see_sources)
sButton.grid(column=1, row=4, sticky=tk.W, padx=15, pady=10)

rButton = tk.Button(root, text="Recommendation", bg="#DEFFAD", fg="black", font=("Arial", 10), command=reccs)
rButton.grid(column=1, row=5, sticky=tk.W, padx=15, pady=10)

cButton = tk.Button(root, text="Credits", bg="#DEFFAD", fg="black", font=("Arial", 10), command=cr)
cButton.grid(column=3, row=14, sticky=tk.W, padx=15, pady=10)

lButton = tk.Button(root, text="Logo", bg="#DEFFAD", fg="black", font=("Arial", 10), command=lg)
lButton.grid(column=3, row=15, sticky=tk.W, padx=15, pady=10)

gButton = tk.Button(root, text="Guide", bg="#DEFFAD", fg="black", font=("Arial", 10), command=gd)
gButton.grid(column=1, row=6, sticky=tk.W, padx=15, pady=10)

result_label = tk.Label(root, text="", bg="#ABE96D", fg="black", font=("Arial", 10), wraplength=400, justify="left")
result_label.grid(column=0, row=7, columnspan=2, sticky=tk.W, padx=15, pady=10)


root.mainloop()
