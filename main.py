from PIL import Image, ImageDraw
import imageio
import numpy as np

def draw_frame(frame_number, total_frames, image_size=(480,480)):
    width, height = image_size
    img = Image.new('RGB', image_size, 'black')
    draw = ImageDraw.Draw(img)

    num_bars = 20
    bar_width = 10
    max_height = height

    # Calculation to make bars shrink towards the center and then expand back
    max_scale = 1.0
    progress = (frame_number % total_frames) / total_frames
    if progress > 0.5:
        progress = 1 - progress
    scale = max_scale * progress * 2

    for i in range(num_bars):
        x = width // 2 + (i - num_bars // 2) * bar_width * 1.5
        bar_height = int(max_height * scale)
        y0 = (height - bar_height) // 2
        y1 = y0 + bar_height
        draw.rectangle([x, y0, x + bar_width, y1], fill='white')

    return img

def create_gif(filename, total_frames=30, fps=10):
    frames = []
    for i in range(total_frames):
        frame = draw_frame(i, total_frames)
        frames.append(np.array(frame))

    imageio.mimsave(filename, frames, fps=fps, loop=0)  # loop=0 makes the gif repeat indefinitely


def main():
    create_gif('animated_bars.gif', total_frames=60, fps=30)
    
if __name__=="__main__":
    main()
