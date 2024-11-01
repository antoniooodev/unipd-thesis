from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import JavascriptLexer
from pygments.formatters import ImageFormatter
from pygments.styles import get_style_by_name
import io

code = """
import React from 'react';

export default function Movie({
    title,
    genre,
    description,
    price,
    onBuy
}) {
    return (
        <div className="movie">
            <div className="details">
                <h1>
                    {title}
                    <span className="price">{price}</span>
                </h1>
                <p className="description">{description}</p>
                <span className="genre">{genre}</span>
            </div>
            <div>
                <button onClick={onBuy}>Buy!</button>
            </div>
        </div>
    );
}
"""

font_path = "/path/to/DejaVuSansMono.ttf"
style = get_style_by_name("dracula")
formatter = ImageFormatter(style=style, font_name=font_path, font_size=16, line_numbers=False)
image_bytes = highlight(code, JavascriptLexer(), formatter)

image = Image.open(io.BytesIO(image_bytes))
header_height = 30
new_image = Image.new("RGB", (image.width, image.height + header_height), "#282a36")
new_image.paste(image, (0, header_height))

draw = ImageDraw.Draw(new_image)
button_radius = 10
button_spacing = 15
colors = ["#ff5f57", "#ffbd2e", "#28c940"]

for i, color in enumerate(colors):
    draw.ellipse(
        (button_spacing * (i + 1), header_height // 2 - button_radius // 2,
         button_spacing * (i + 1) + button_radius, header_height // 2 + button_radius // 2),
        fill=color
    )

new_image.save("/path/to/movie_component_code_styled.png")
