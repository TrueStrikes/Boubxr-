# gradient.py

def gradient_text(text, start_color, end_color):
    gradient = []
    for i in range(len(text)):
        ratio = i / len(text)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        gradient.append(f"\033[38;2;{r};{g};{b}m{text[i]}\033[0m")
    return ''.join(gradient)

def gold_to_white_gradient(text):
    start_color = (255, 215, 0)  # Gold RGB
    end_color = (255, 255, 255)   # White RGB
    return gradient_text(text, start_color, end_color)
