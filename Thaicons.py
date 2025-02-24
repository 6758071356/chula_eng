import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai"), ("\u0E02", "Khor Khai"), ("\u0E03", "Khor Khuat"),
    ("\u0E04", "Khor Khwai"), ("\u0E05", "Khor Khon"), ("\u0E06", "Khor Rakhang"),
    ("\u0E07", "Ngor Ngu"), ("\u0E08", "Jor Jan"), ("\u0E09", "Chor Ching"),
    ("\u0E0A", "Chor Chang"), ("\u0E0B", "Sor So"), ("\u0E0C", "Chor Choe"),
    ("\u0E0D", "Yor Ying"), ("\u0E0E", "Dor Chada"), ("\u0E0F", "Tor Patak")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        self.is_flipped = False
        
        self.label = tk.Label(root, text="Click 'Next' to start!", font=("Arial", 40), width=10, height=3)
        self.label.pack(pady=20)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 20))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 20))
        self.next_button.pack()
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.is_flipped = False
        self.label.config(text=self.current_card[0])
    
    def flip_card(self):
        if self.current_card:
            if self.is_flipped:
                self.label.config(text=self.current_card[0])
                self.is_flipped = False
            else:
                self.label.config(text=self.current_card[1])
                self.is_flipped = True

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
