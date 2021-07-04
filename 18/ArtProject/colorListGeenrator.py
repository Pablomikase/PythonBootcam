import colorgram

colors = colorgram.extract('abstractArt.jpg', 30)
rbg_colors = []
print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rbg_colors.append(new_color)

print(rbg_colors)