import tkinter as tk
import unittest

class WebEnumeration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Web Enumeration")
        self.label = tk.Label(self.root, text="Websites:")
        self.label.pack()
        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack()

    def populate_listbox(self, websites):
        for index, website in enumerate(websites):
            self.listbox.insert(index, website)

    def run(self):
        self.root.mainloop()

class TestWebEnumeration(unittest.TestCase):
    def setUp(self):
        self.web_enum = WebEnumeration()

    def test_populate_listbox(self):
        websites = ["test1.com", "test2.com", "test3.com"]
        self.web_enum.populate_listbox(websites)
        self.assertEqual(self.web_enum.listbox.size(), len(websites))

    def test_listbox_contents(self):
        websites = ["test1.com", "test2.com", "test3.com"]
        self.web_enum.populate_listbox(websites)
        for i, website in enumerate(websites):
            self.assertEqual(self.web_enum.listbox.get(i), website)

    def test_window_title(self):
        self.assertEqual(self.web_enum.root.title(), "Web Enumeration")

    def test_label_text(self):
        self.assertEqual(self.web_enum.label.cget("text"), "Websites:")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebEnumeration)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    web_enum = WebEnumeration()
    websites = ["google.com", "facebook.com", "twitter.com", "instagram.com"]
    web_enum.populate_listbox(websites)
    web_enum.root.update_idletasks()  # Add this line
    web_enum.run()