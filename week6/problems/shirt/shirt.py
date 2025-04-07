import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        input = sys.argv[1].strip()
        output = sys.argv[2].strip()
        if validate_file_types(input, output):
            create_image(input, output)
        else:
            sys.exit("File type error: Input and Output files types must match.")
    elif len(sys.argv) > 3:
        sys.exit("To many command-line arguments")
    else:
        sys.exit("To few command-line arguments")

def create_image(input, output):
    try:
        if not os.path.exists(input):
            sys.exit(f"Error: The file {input} does not exist.")
        shirt_image = Image.open("shirt.png")
        with Image.open(input) as image:
            image = ImageOps.fit(image, shirt_image.size)
            image.paste(shirt_image, mask = shirt_image)
            image.save(output)
    except FileNotFoundError:
        sys.exit("File not found")

def validate_file_types(input, output):
    if input.endswith(".jpg") and output.endswith(".jpg"):
        return True
    elif input.endswith(".jpeg") and output.endswith(".jpeg"):
        return True
    elif input.endswith(".png") and output.endswith(".png"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()