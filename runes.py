import random

runes = {
    "Fehu": "Wealth, prosperity, abundance.",
    "Uruz": "Strength, health, endurance.",
    "Thurisaz": "Conflict, protection, defense.",
    "Ansuz": "Wisdom, communication, divine inspiration.",
    "Raido": "Journey, movement, progression.",
    "Kenaz": "Creativity, knowledge, enlightenment.",
    "Gebo": "Gift, partnership, generosity.",
    "Wunjo": "Joy, harmony, fulfillment.",
    "Hagalaz": "Disruption, change, transformation.",
    "Nauthiz": "Need, necessity, restraint.",
    "Isa": "Standstill, stillness, patience.",
    "Jera": "Harvest, cycles, reward for efforts.",
    "Eihwaz": "Change, initiation, transition.",
    "Perthro": "Mystery, destiny, fate.",
    "Algiz": "Protection, defense, higher self.",
    "Sowilo": "Success, energy, vitality.",
    "Tiwaz": "Honor, justice, sacrifice.",
    "Berkano": "Growth, fertility, renewal.",
    "Ehwaz": "Trust, partnership, teamwork.",
    "Madr": "Humanity, balance, connection."
}

def draw_runes():
    selected_runes = random.sample(list(runes.items()), 3)
    
    print("Your Rune Reading:")
    for rune, meaning in selected_runes:
        print(f"{rune}: {meaning}")
    
    interpretation = interpret_combination(selected_runes)
    print("\nInterpretation of the Draw:")
    print(interpretation)

def interpret_combination(runes):
    interpretations = {
        ('Fehu', 'Uruz', 'Sowilo'): "A time of prosperity and strength is upon you. Enjoy your successes and make the most of your resources.",
        ('Thurisaz', 'Nauthiz', 'Isa'): "You may face obstacles, but patience and resilience will help you navigate through the conflict.",
        ('Raido', 'Gebo', 'Ehwaz'): "A partnership or journey brings mutual growth. Trust the relationships in your life and be open to collaboration.",
        ('Hagalaz', 'Kanoz', 'Madr'): "Disruption may lead to enlightenment. Embrace the changes as they can lead to personal growth.",
        ('Berkano', 'Jera', 'Wunjo'): "This is a time of growth and joy. Your efforts will bear fruit, bringing happiness to your life."
    }
    
    key = tuple(sorted(rune for rune, _ in runes))
    
    return interpretations.get(key, "Your runes suggest a journey of discovery. Embrace the messages they convey and trust your intuition.")

draw_runes()
