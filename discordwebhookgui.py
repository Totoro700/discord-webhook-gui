import tkinter as tk
import tkinter.font as tkfont
import tkinter.colorchooser as colorchooser
from discord_webhook import DiscordWebhook, DiscordEmbed

FONT_SIZE = 12
FONT_SIZE_LARGE = FONT_SIZE * 2

def on_input_change(event):
    entry = event.widget
    text = entry.get()
    entry.config(width=len(text) + 5)

def send_message():
    input1_value = input1.get()
    input2_value = input2.get()
    webhook = DiscordWebhook(url=urllabel.get(), rate_limit_retry=True)
    color = color_label.cget("bg")
    if color != "white":
        color = color.replace("#", "")
    else:
        color = "00ffff"
    embed = DiscordEmbed(title=input1_value, description=input2_value, color=color)
    webhook.add_embed(embed)

    image_url = image_url_entry.get().strip()
    if image_url:
        embed.set_image(url=image_url)
    else:
        embed.set_image(url=None)

    try:
        response = webhook.execute()
        print(str(webhook) + " --- " + str(embed.toString()))
        message_label.config(text="Sent", fg="green")
    except:
        print("Error, try again")
        
def open_color_picker():
    color = colorchooser.askcolor()
    if color[1] is not None:
        color_label.configure(bg=color[1])

window = tk.Tk()
window.title("Discord Webhook")
window.state('zoomed')

font = tkfont.Font(size=FONT_SIZE_LARGE)

urllabel = tk.Label(window, text="Url: ", font=font, justify="center")
urllabel.pack()

urllabel = tk.Entry(window, font=font, justify='center')
urllabel.pack()

label1 = tk.Label(window, text="Title: ", font=font, justify="center")
label1.pack()

input1 = tk.Entry(window, font=font, justify='center')
input1.pack()
input1.bind("<KeyRelease>", on_input_change)

label2 = tk.Label(window, text="Description: ", font=font, justify="center")
label2.pack()

input2 = tk.Entry(window, font=font, justify='center')
input2.pack()
input2.bind("<KeyRelease>", on_input_change)

color_button = tk.Button(window, text="Select Color", command=open_color_picker, font=font)
color_button.pack()

color_label = tk.Label(window, text=" ", bg="white", width=20, height=2, font=font)
color_label.pack()

image_url_label = tk.Label(window, text="Image URL: ", font=font, justify="center")
image_url_label.pack()

image_url_entry = tk.Entry(window, font=font, justify='center')
image_url_entry.pack()
image_url_entry.bind("<KeyRelease>", on_input_change)

send_button = tk.Button(window, text="Send", command=send_message, font=font)
send_button.pack()

message_label = tk.Label(window, text="", fg="red", font=font)
message_label.pack()

window.mainloop()