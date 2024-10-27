from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import JavascriptLexer
from pygments.formatters import ImageFormatter
from pygments.styles import get_style_by_name
import io

# Codice React che vuoi convertire in immagine
code = """
const PlaybackControls = () => {
  const volume = useSelector((state) => state.mopidy.volume);
  const playState = useSelector((state) => state.mopidy.play_state);
  const currentTrack = useSelector((state) => state.mopidy.current_track);
"""

# Percorso completo del font DejaVuSansMono.ttf
font_path = "/Users/antoniotangaro/Downloads/dejavu-fonts-ttf-2.37/ttf/DejaVuSansMono.ttf"

# Usa Pygments per evidenziare la sintassi e creare l'immagine
style = get_style_by_name("dracula")  # Puoi provare anche "monokai"
formatter = ImageFormatter(style=style, font_name=font_path, font_size=16, line_numbers=False)
image_bytes = highlight(code, JavascriptLexer(), formatter)

# Converti i bytes in un'immagine Pillow
image = Image.open(io.BytesIO(image_bytes))

# Aggiungi l'intestazione con i pulsanti colorati
header_height = 30
new_image = Image.new("RGB", (image.width, image.height + header_height), "#282a36")  # Sfondo scuro come Dracula
new_image.paste(image, (0, header_height))

# Aggiungi i tre pulsanti colorati in alto a sinistra
draw = ImageDraw.Draw(new_image)
button_radius = 10
button_spacing = 15
colors = ["#ff5f57", "#ffbd2e", "#28c940"]  # Rosso, giallo, verde

for i, color in enumerate(colors):
    draw.ellipse(
        (button_spacing * (i + 1), header_height // 2 - button_radius // 2,
         button_spacing * (i + 1) + button_radius, header_height // 2 + button_radius // 2),
        fill=color
    )

# Salva l’immagine con un'estensione corretta
new_image.save("/Users/antoniotangaro/Desktop/movie_component_code_styled.png")

print("Immagine salvata come 'movie_component_code_styled.png'")
