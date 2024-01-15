import fontforge

# Generate bold weight
font = fontforge.open('fonts/ttf/FragmentMono-Regular.ttf')
font.selection.all()
font.fontname = 'FragmentMono-Bold'
font.fullname = 'Fragment Mono Bold'
font.weight = 'Bold'
font.changeWeight(32, "LCG", 0, 0, "squish")
font.generate('weights/FragmentMono-Bold.ttf')
print(font)
font.close()

# Generate semi-bold weight
font = fontforge.open('fonts/ttf/FragmentMono-Regular.ttf')
font.selection.all()
font.fontname = 'FragmentMono-SemiBold'
font.fullname = 'Fragment Mono SemiBold'
font.weight = 'SemiBold'
font.changeWeight(21, "LCG", 0, 0, "squish")
font.generate('weights/FragmentMono-SemiBold.ttf')
print(font)
font.close()

# Generate medium weight
font = fontforge.open('fonts/ttf/FragmentMono-Regular.ttf')
font.selection.all()
font.fontname = 'FragmentMono-Medium'
font.fullname = 'Fragment Mono Medium'
font.weight = 'Medium'
font.changeWeight(10, "LCG", 0, 0, "squish")
font.generate('weights/FragmentMono-Medium.ttf')
print(font)
font.close()
