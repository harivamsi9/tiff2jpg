


from PIL import Image

def convert_tiff_to_jpg(input_tiff_path, output_jpg_path):
    tiff_image = Image.open(input_tiff_path)
    
    if tiff_image.mode == 'P':
        tiff_image = tiff_image.convert('RGB')

    tiff_image.save(output_jpg_path + '.jpg', 'JPEG')
    tiff_image.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Convert TIFF images to JPG format.')
    parser.add_argument('input_tiff', help='Path to the input TIFF image.')
    parser.add_argument('output_jpg', help='Path to save the output JPG image.')

    args = parser.parse_args()
    convert_tiff_to_jpg(args.input_tiff, args.output_jpg)

if __name__ == '__main__':
    main()
