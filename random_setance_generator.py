import random

def get_random_word(words):
    return random.choice(words)

names = ["Andrey", "Ivan", "George", "Alex", "Denis"]
places = ["Sofia", "Varna", "Los Angeles", "New York", "Boston"]
verbs = ["plays", "eats", "walks", "runs", "watched"]
nouns = ["cake", "apple", "bananas", "water", "whiskey"]
adverbs = ["yesterday", "last week", "today", "here", "never", "there"]
details = ["in the park", "near home", "at school", "at work", "in the gym"]

print("Hello, this is your first random sentence:")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_detail}")
    print("Click [Enter] to generate a new one.")
    input()
