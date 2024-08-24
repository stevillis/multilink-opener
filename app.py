import tkinter as tk
import webbrowser

BROWSER_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"


def open_links():
    links = text_area.get("1.0", tk.END).strip().splitlines()

    for link in links:
        if link:
            webbrowser.get("chrome").open_new_tab(link)


if __name__ == "__main__":
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(BROWSER_PATH),
    )

    root = tk.Tk()
    root.title("Multilink Opener")

    text_area = tk.Text(root, height=10, width=50)
    text_area.pack(pady=10)

    open_button = tk.Button(
        root,
        text="Open Links",
        command=open_links,
    )
    open_button.pack(pady=5)

    root.mainloop()
