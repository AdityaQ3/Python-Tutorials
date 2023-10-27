import time


def fireworks_animation():
    for _ in range(3):
        print("🎆✨🌟💥🎇🎆✨🌟💥🎇")
        time.sleep(1)


def wish_birthday_creatively(Taranjeet):
    print("🎈🎉🍰 Happy Birthday, " + "Taranjeet" + "! 🍰🎉🎈")
    print("Today is a day to celebrate YOU!")
    fireworks_animation()
    print(f"{Taranjeet}, you're not getting older, you're getting wiser and more fabulous!")
    print("May this year be filled with love, laughter, and new adventures!")


wish_birthday_creatively("Taranjeet")


def add_one(x):
    return x + 1


d = {'a': 1, 'b': 2, 'c': 3}
result = map(add_one, d.values())
print(list(result))
