from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

main_img_orig = None
watermark_img_orig = None
tk_main = None
tk_watermark = None

window = Tk()
window.title("Pro Watermarker")
window.config(padx=20, pady=20)


def upload_image():
    global main_img_orig, tk_main
    file_path = filedialog.askopenfilename()
    if file_path:
        main_img_orig = Image.open(file_path).convert("RGBA")
        preview_img = main_img_orig.copy()
        preview_img.thumbnail((500, 500))
        tk_main = ImageTk.PhotoImage(preview_img)

        preview_canvas.config(width=preview_img.width, height=preview_img.height)
        preview_canvas.delete("all")
        preview_canvas.create_image(preview_img.width / 2, preview_img.height / 2, image=tk_main, tags="main")
        preview_canvas.image = tk_main


def add_watermark():
    global watermark_img_orig, tk_watermark
    if main_img_orig is None:
        messagebox.showwarning("Error", "Upload a background image first!")
        return

    file_path = filedialog.askopenfilename()
    if file_path:
        watermark_img_orig = Image.open(file_path).convert("RGBA")

        wm_size = (40, 40)
        watermark_img_orig.thumbnail(wm_size)

        tk_watermark = ImageTk.PhotoImage(watermark_img_orig)

        preview_canvas.create_image(250, 250, image=tk_watermark, tags="wm")
        preview_canvas.wm_image = tk_watermark


def merge_and_save():
    if main_img_orig and watermark_img_orig:
        final_output = main_img_orig.copy()

        target_width = int(final_output.width * 0.20)
        w_ratio = target_width / float(watermark_img_orig.width)
        target_height = int(float(watermark_img_orig.height) * float(w_ratio))

        working_watermark = watermark_img_orig.resize(
            (target_width, target_height), Image.LANCZOS
        )

        x = (final_output.width - working_watermark.width) // 2
        y = (final_output.height - working_watermark.height) // 2

        final_output.paste(working_watermark, (x, y), working_watermark)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")]
        )

        if save_path:
            if save_path.endswith(".jpg") or save_path.endswith(".jpeg"):
                final_output = final_output.convert("RGB")
            final_output.save(save_path)
            messagebox.showinfo("Success", "Watermarked image saved!")


# --- UI Layout ---
btn_frame = Frame(window)
btn_frame.pack()

Button(btn_frame, text="1. Add Background", command=upload_image).grid(row=0, column=0, padx=5)
Button(btn_frame, text="2. Add Watermark", command=add_watermark).grid(row=0, column=1, padx=5)
Button(btn_frame, text="3. Save Merged", command=merge_and_save).grid(row=0, column=2, padx=5)

preview_canvas = Canvas(window, width=500, height=500, bg="lightgray")
preview_canvas.pack(pady=20)

window.mainloop()