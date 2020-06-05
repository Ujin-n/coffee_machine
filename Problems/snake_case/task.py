camel_phrase = input()
snake_phrase = ''
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for word in camel_phrase:
    if word in capitals:
        snake_phrase += '_'
    snake_phrase += word.lower()

print(snake_phrase)
