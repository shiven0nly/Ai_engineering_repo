letter = '''Dear <|name|>
You are selected!
<|Date|>'''

# replace("name", "Shiven") this function replaces string 1 written first with string 2 written second

print(letter.replace("<|name|>", "Shiven").replace("<|Date|>", "24 september 2026"))