words = ["hello", "python", "computer", "mouse", "tablet", "phone", "monitor"]

for word in words:
    print(f"Here are some words: {word}.")

for i in range(1, 11):
    print(f"Let's add a few numbers to our list: {i}.")
    words.append(i)

stacked_words = [
    "These",
    "words",
    "will",
    "appear",
    "on",
    "top",
    "of",
    "each",
    "other.",
]

for stacked in stacked_words:
    print(f"We are stacked! {stacked}")
