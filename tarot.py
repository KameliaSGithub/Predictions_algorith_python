import random

tarot_cards = {
    "The Fool": "New beginnings, innocence, spontaneity.",
    "The Magician": "Manifestation, resourcefulness, power.",
    "The High Priestess": "Intuition, unconscious knowledge, mystery.",
    "The Empress": "Fertility, beauty, nurturing.",
    "The Emperor": "Authority, structure, control.",
    "The Hierophant": "Tradition, spiritual guidance, conformity.",
    "The Lovers": "Love, harmony, choices, partnerships.",
    "The Chariot": "Determination, willpower, triumph over obstacles.",
    "Strength": "Courage, inner strength, compassion.",
    "The Hermit": "Introspection, inner guidance, solitude.",
    "Wheel of Fortune": "Change, cycles, destiny, luck.",
    "Justice": "Fairness, truth, law, accountability.",
    "The Hanged Man": "Surrender, new perspectives, letting go.",
    "Death": "Transformation, endings, new beginnings, change.",
    "Temperance": "Balance, moderation, harmony.",
    "The Devil": "Temptation, materialism, addiction.",
    "The Tower": "Upheaval, chaos, revelation.",
    "The Star": "Hope, faith, inspiration, serenity.",
    "The Moon": "Illusion, intuition, fear, subconscious.",
    "The Sun": "Joy, success, vitality, positivity.",
    "Judgment": "Reflection, reckoning, awakening.",
    "The World": "Completion, fulfillment, accomplishment, travel.",
    "Ace of Cups": "New emotional experiences, love, compassion.",
    "Two of Cups": "Connection, partnership, balancing emotions.",
    "Three of Cups": "Celebration, friendship, community.",
    "Four of Cups": "Contemplation, apathy, reevaluation.",
    "Five of Cups": "Loss, disappointment, focusing on the negative.",
    "Six of Cups": "Nostalgia, childhood memories, innocence.",
    "Seven of Cups": "Choices, fantasy, illusions.",
    "Eight of Cups": "Abandonment, quest for deeper meaning.",
    "Nine of Cups": "Contentment, satisfaction, emotional fulfillment.",
    "Ten of Cups": "Happiness, alignment, family harmony.",
    "Page of Cups": "Creativity, intuition, exploration of emotions.",
    "Knight of Cups": "Romance, charm, idealism.",
    "Queen of Cups": "Compassion, caring, emotional security.",
    "King of Cups": "Emotional balance, control, diplomacy.",
    "Ace of Pentacles": "New financial opportunities, prosperity.",
    "Two of Pentacles": "Balance, prioritization, flexibility.",
    "Three of Pentacles": "Collaboration, teamwork, skill development.",
    "Four of Pentacles": "Stability, security, control over resources.",
    "Five of Pentacles": "Financial loss, isolation, insecurity.",
    "Six of Pentacles": "Generosity, charity, sharing wealth.",
    "Seven of Pentacles": "Patience, long-term view, investment.",
    "Eight of Pentacles": "Skill development, craftsmanship, diligence.",
    "Nine of Pentacles": "Independence, self-sufficiency, luxury.",
    "Ten of Pentacles": "Legacy, inheritance, long-term success.",
    "Page of Pentacles": "Ambition, planning, new opportunities.",
    "Knight of Pentacles": "Hard work, routine, perseverance.",
    "Queen of Pentacles": "Nurturing, practicality, financial security.",
    "King of Pentacles": "Wealth, stability, security in financial matters.",
    "Ace of Swords": "Clarity, truth, new ideas.",
    "Two of Swords": "Indecision, choices, stalemate.",
    "Three of Swords": "Heartbreak, emotional pain, sorrow.",
    "Four of Swords": "Rest, recovery, contemplation.",
    "Five of Swords": "Conflict, defeat, betrayal.",
    "Six of Swords": "Transition, moving away, healing.",
    "Seven of Swords": "Deception, betrayal, strategic thinking.",
    "Eight of Swords": "Restriction, isolation, helplessness.",
    "Nine of Swords": "Anxiety, worry, nightmares.",
    "Ten of Swords": "Betrayal, loss, painful endings.",
    "Page of Swords": "Curiosity, communication, mental agility.",
    "Knight of Swords": "Ambition, action, haste.",
    "Queen of Swords": "Independence, clarity of mind, honesty.",
    "King of Swords": "Authority, intellect, clear thinking.",
    "Ace of Wands": "Inspiration, new ventures, potential.",
    "Two of Wands": "Planning, discovery, foresight.",
    "Three of Wands": "Expansion, foresight, exploration.",
    "Four of Wands": "Celebration, harmony, homecoming.",
    "Five of Wands": "Conflict, competition, rivalry.",
    "Six of Wands": "Victory, success, public recognition.",
    "Seven of Wands": "Challenge, perseverance, defensiveness.",
    "Eight of Wands": "Speed, action, rapid movement.",
    "Nine of Wands": "Resilience, persistence, courage.",
    "Ten of Wands": "Burden, responsibility, hard work.",
    "Page of Wands": "Exploration, enthusiasm, creativity.",
    "Knight of Wands": "Action-oriented, adventure, impulsiveness.",
    "Queen of Wands": "Confidence, social, warm.",
    "King of Wands": "Leadership, vision, honor."
}

def draw_tarot_cards():
    selected_cards = random.sample(list(tarot_cards.items()), 3)
    
    print("Your Tarot Reading:")
    for card, meaning in selected_cards:
        print(f"{card}: {meaning}")
    
    interpretation = interpret_combination(selected_cards)
    print("\nInterpretation of the Draw:")
    print(interpretation)

def interpret_combination(cards):
    interpretations = {
        ('The Fool', 'The Magician', 'The Empress'): "A time to embrace new beginnings and creativity. Your potential is limitless if you trust your instincts.",
        ('The Lovers', 'The Chariot', 'Strength'): "Important decisions in love or relationships may require your courage. Tap into your inner strength to navigate challenges.",
        ('Death', 'The Moon', 'The Star'): "Transformation may bring uncertainty, but hope lies ahead. Embrace the change and trust that you are guided towards a brighter future.",
        ('The Devil', 'The Tower', 'Justice'): "A revelation may lead to breaking free from unhealthy patterns. It's time to confront harsh truths to restore balance.",
        ('The Sun', 'Ten of Cups', 'The World'): "Joy and happiness abound! Achievements in family or personal life indicate that you are completing a fulfilling chapter.",
    }
    
    key = tuple(sorted(card for card, _ in cards))
    
    return interpretations.get(key, "Your cards suggest a unique journey ahead, blending various aspects of your life. Trust the process and embrace your path.")

draw_tarot_cards()
