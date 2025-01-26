import random
tarot_cards = {
    "The Fool": "The Fool represents new beginnings and adventures. It encourages you to have faith in the unknown and embrace spontaneity.",
    "The Magician": "The Magician signifies manifestation and resourcefulness. It suggests that you have all the tools needed to achieve your goals.",
    "The High Priestess": "The High Priestess symbolizes intuition and inner wisdom. She encourages you to trust your gut feelings and explore your subconscious.",
    "The Empress": "The Empress embodies fertility, beauty, and nurturing. She reminds you to connect with nature and embrace your creative side.",
    "The Emperor": "The Emperor stands for authority, structure, and control. He urges you to take charge of your life and establish order.",
    "The Hierophant": "The Hierophant represents tradition and spiritual guidance. He encourages you to seek wisdom through established belief systems.",
    "The Lovers": "The Lovers symbolize love, harmony, and choices. They remind you to embrace partnerships and make decisions that reflect your true values.",
    "The Chariot": "The Chariot signifies determination and willpower. It encourages you to focus on your goals and overcome obstacles with confidence.",
    "Strength": "Strength represents courage and inner strength. It reminds you to face challenges with grace and resilience.",
    "The Hermit": "The Hermit symbolizes introspection and inner guidance. He encourages you to spend time alone to reflect and gain insights.",
    "Wheel of Fortune": "The Wheel of Fortune signifies change and cycles. It reminds you that life is full of ups and downs, and you should embrace both.",
    "Justice": "Justice represents fairness and truth. It encourages you to take responsibility for your actions and seek balance.",
    "The Hanged Man": "The Hanged Man symbolizes surrender and new perspectives. It encourages you to let go and look at things from a different angle.",
    "Death": "Death signifies transformation and endings. It reminds you that every ending paves the way for new beginnings.",
    "Temperance": "Temperance embodies balance and moderation. It encourages you to find harmony in different aspects of your life.",
    "The Devil": "The Devil represents temptation and materialism. It reminds you to examine what binds you and seek liberation.",
    "The Tower": "The Tower signifies upheaval and revelation. It reminds you that sometimes destruction is necessary for new growth.",
    "The Star": "The Star symbolizes hope and inspiration. It encourages you to have faith in the future and pursue your dreams.",
    "The Moon": "The Moon represents intuition and the subconscious. It encourages you to explore your emotions and confront fears.",
    "The Sun": "The Sun symbolizes joy and success. It reminds you to celebrate achievements and embrace positivity.",
    "Judgment": "Judgment represents reflection and reckoning. It encourages you to evaluate your past actions for personal growth.",
    "The World": "The World symbolizes completion and fulfillment. It reminds you that you have achieved your goals and can now start anew."
}

def draw_tarot_cards():
    selected_cards = random.sample(list(tarot_cards.items()), 3)
    
    for card, meaning in selected_cards:
        print(f"{card}: {meaning}\n")
draw_tarot_cards()