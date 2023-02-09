import argparse
from pathlib import Path

from pdfreader import SimplePDFViewer, PageDoesNotExist


parser = argparse.ArgumentParser()
parser.add_argument('pdf_files', nargs='+', type=str)


def main(args):
    pdf_files = args.pdf_files
    pdf_files = [Path(x) for x in pdf_files]

    for file in pdf_files:
        print(f'Working on {file}')
        fd = open(file, 'rb')
        viewer = SimplePDFViewer(fd)

        plain_text = ''
        pdf_markdown = ''
        images = []
        try:
            while True:
                viewer.render()
                pdf_markdown += viewer.canvas.text_content
                plain_text += ''.join(viewer.canvas.strings)
                images.extend(viewer.canvas.inline_images)
                images.extend(viewer.canvas.images.values())
                viewer.next()
        except PageDoesNotExist:
            pass

        with open('pdf.md', 'w+') as f:
           f.write(pdf_markdown)
        print(pdf_markdown)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
