import random
from enum import Enum
from typing import Dict, List
from datetime import datetime


class Mood(Enum):
    """Enum for different mood states."""
    HAPPY = "happy"
    SAD = "sad"
    MOTIVATED = "motivated"
    CALM = "calm"
    ANXIOUS = "anxious"
    NOSTALGIC = "nostalgic"
    ROMANTIC = "romantic"
    CONTEMPLATIVE = "contemplative"


class QuoteDatabase:
    """Database of mood-based quotes."""
    
    QUOTES: Dict[str, List[str]] = {
        "happy": [
            "Life is about creating yourself. 🌟",
            "Happiness is not by chance, but by choice. ✨",
            "Every moment is a fresh beginning. 🌈",
            "The best time to plant a tree was 20 years ago. The second best time is now. 🌱",
            "Your smile is the most beautiful curve on your body. 💫",
            "Today is a good day to have a good day. ☀️",
        ],
        "sad": [
            "It's okay to not be okay. That's how we learn to be brave. 🤍",
            "The wound is the place where the Light enters you. 🌙",
            "Sadness is temporary; your strength is permanent. 💙",
            "Every night brings a new day. ⭐",
            "You are allowed to feel lost and still be okay. 🌊",
            "This too shall pass. 🌸",
        ],
        "motivated": [
            "The only way to do great work is to love what you do. 🔥",
            "Success is not final, failure is not fatal. 💪",
            "Don't watch the clock; do what it does. Keep going. ⏰",
            "You are capable of amazing things. 🚀",
            "The only impossible journey is the one you never begin. 🎯",
            "Your potential is endless. 💎",
        ],
        "calm": [
            "Breathe. Let it go. Everything is okay. 🕊️",
            "Peace comes from within. Do not seek it without. 🧘",
            "In the middle of chaos, there is also opportunity. ☯️",
            "Still waters run deep. 🌊",
            "Sometimes the most productive thing you can do is nothing. 🍃",
            "Serenity is not freedom from the storm, but peace amid the storm. ⛅",
        ],
        "anxious": [
            "You don't have to see the whole staircase, just take the first step. 👣",
            "Anxiety is temporary; you are permanent. 🌟",
            "You are stronger than your struggle. 💪",
            "This moment is not your final moment. 🌅",
            "Courage is not the absence of fear, but action despite it. 🦁",
            "You've survived 100% of your worst days so far. 📈",
        ],
        "nostalgic": [
            "The good old days are not behind us; they're a part of us. 📷",
            "Memory is a way of holding onto the things you love. 🎞️",
            "Yesterday is but history, tomorrow is a mystery, but today is a gift. 🎁",
            "Some memories are unforgettable, remaining ever vivid and heartwarming. 💭",
            "The past cannot be changed. The future is yet in your power. ⏳",
            "Nostalgia is a file that removes all the rough edges from the good old days. 🌙",
        ],
        "romantic": [
            "Love is not about finding someone to live with. It's about finding someone you can't imagine living without. 💕",
            "The heart wants what it wants. 💗",
            "In every conceivable manner, the family is link to our past, bridge to our future, and the context for our present. 💑",
            "You are my today and all of my tomorrows. 🌹",
            "Love looks not with the eyes, but with the heart. 👁️💖",
            "Being deeply loved by someone gives you strength; loving someone deeply gives you courage. 💞",
        ],
        "contemplative": [
            "We are not makers of history. We are made by history. 📚",
            "The unexamined life is not worth living. 🤔",
            "To know oneself is the beginning of wisdom. 🔮",
            "What we think, we become. 💭",
            "The universe is not only queerer than we suppose, but queerer than we can suppose. 🌌",
            "Life is what happens when you're busy making other plans. 🎨",
        ],
    }


class MoodQuoteGenerator:
    """Generate aesthetic quotes based on mood."""
    
    def __init__(self):
        """Initialize the quote generator."""
        self.quote_db = QuoteDatabase()
        self.history: List[Dict] = []
    
    def get_quote(self, mood: str) -> str:
        """
        Get a random quote for the specified mood.
        
        Args:
            mood: The mood as a string (e.g., 'happy', 'sad')
            
        Returns:
            A quote string
            
        Raises:
            ValueError: If mood is not recognized
        """
        try:
            mood_enum = Mood[mood.upper()]
        except KeyError:
            raise ValueError(
                f"Mood '{mood}' not recognized. "
                f"Available moods: {', '.join([m.value for m in Mood])}"
            )
        
        quotes = self.quote_db.QUOTES.get(mood_enum.value, [])
        if not quotes:
            raise ValueError(f"No quotes found for mood: {mood}")
        
        quote = random.choice(quotes)
        
        # Track history
        self.history.append({
            "mood": mood_enum.value,
            "quote": quote,
            "timestamp": datetime.now().isoformat()
        })
        
        return quote
    
    def get_random_quote(self) -> tuple:
        """
        Get a random quote from any mood category.
        
        Returns:
            Tuple of (mood, quote)
        """
        random_mood = random.choice(list(Mood))
        quote = self.get_quote(random_mood.value)
        return random_mood.value, quote
    
    def display_quote(self, quote: str, mood: str) -> None:
        """
        Display a quote with aesthetic formatting.
        
        Args:
            quote: The quote text
            mood: The mood category
        """
        border = "✧" * 40
        print(f"\n{border}")
        print(f"  Mood: {mood.upper()}")
        print(f"{border}")
        print(f"\n  {quote}\n")
        print(f"{border}\n")
    
    def get_history(self) -> List[Dict]:
        """Get the history of generated quotes."""
        return self.history
    
    def clear_history(self) -> None:
        """Clear the quote history."""
        self.history = []
    
    def get_available_moods(self) -> List[str]:
        """Get list of available moods."""
        return [mood.value for mood in Mood]


def main():
    """Main function to demonstrate the mood quote generator."""
    generator = MoodQuoteGenerator()
    
    print("\n" + "=" * 50)
    print("  🌟 AESTHETIC MOOD-BASED QUOTE GENERATOR 🌟")
    print("=" * 50)
    
    # Display available moods
    print("\nAvailable Moods:")
    for mood in generator.get_available_moods():
        print(f"  • {mood.capitalize()}")
    
    # Interactive loop
    while True:
        print("\nOptions:")
        print("  1. Get quote by mood")
        print("  2. Get random quote")
        print("  3. View history")
        print("  4. Clear history")
        print("  5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            mood_input = input("Enter mood (or 'list' to see all): ").strip().lower()
            
            if mood_input == "list":
                print("\nAvailable moods:")
                for mood in generator.get_available_moods():
                    print(f"  • {mood}")
                continue
            
            try:
                quote = generator.get_quote(mood_input)
                generator.display_quote(quote, mood_input)
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "2":
            mood, quote = generator.get_random_quote()
            generator.display_quote(quote, mood)
        
        elif choice == "3":
            history = generator.get_history()
            if not history:
                print("\n📭 No history yet.")
            else:
                print("\n📜 Quote History:")
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. [{entry['mood'].upper()}] {entry['quote']}")
        
        elif choice == "4":
            generator.clear_history()
            print("\n✨ History cleared!")
        
        elif choice == "5":
            print("\n✨ Thank you for using the Mood Quote Generator! ✨\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()