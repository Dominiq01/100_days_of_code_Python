from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

window = Tk()
window.title("Add Watermark to Image")
window.config(padx=20, pady=20)
window.minsize(width=900, height=800)


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if file_path:
        img = Image.open(file_path)

        # Resize to fit the canvas (500x500)
        img = img.resize((500, 500), Image.LANCZOS)

        tk_img = ImageTk.PhotoImage(img)

        # CLEAR the canvas before adding a new image
        preview_canvas.delete("all")

        # IMPORTANT: create_image requires (x, y) coordinates
        # We put it at 250, 250 to center it in a 500x500 canvas
        preview_canvas.create_image(250, 250, image=tk_img)

        # Keep a reference!
        preview_canvas.image = tk_img


# --- UI Setup ---

add_img_button = Button(text="Add image", command=upload_image)
add_img_button.pack(pady=10)

add_watermark_button = Button(text="Add watermark")
add_watermark_button.pack(pady=10)

merge_button = Button(text="Apply")
merge_button.pack(pady=10)

# Create the canvas ONCE here, outside the function
preview_canvas = Canvas(window, width=500, height=500, bg="gray")
preview_canvas.pack(pady=20)

window.mainloop()