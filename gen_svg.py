import svgwrite

dwg = svgwrite.Drawing("hello.svg", profile="tiny", size=("600px", "100px"))


gradient = dwg.defs.add(dwg.linearGradient(id="gradient", x1="0", y1="0", x2="1", y2="0"))
gradient.add_stop_color(offset=0, color="#f099d3", opacity=1)
gradient.add_stop_color(offset=0.5, color="#d922f5", opacity=1)
gradient.add_stop_color(offset=1, color="#691ae8", opacity=1)

dwg.add(dwg.text(
    "Welcome to my profile, I am glad to see you here 😊",
    insert=("50%", "50%"),
    text_anchor="middle",
    font_size=20,
    font_weight="bold",
    fill="url(#gradient)"
))
dwg.save()