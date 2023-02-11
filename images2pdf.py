#!/usr/bin/env python3

import argparse

from PIL import Image
from fpdf import FPDF


def get_image_mm_size(path):
    with Image.open(path) as image:
        pixel_w = image.width
        pixel_h = image.height
        dpi = image.info['dpi'] or (72, 72)
        ratio = 25.4
        mm_w = pixel_w / dpi[0] * ratio
        mm_h = pixel_h / dpi[1] * ratio
        return mm_w, mm_h


def parse_images_paths(txtpath):
    with open(txtpath, 'r') as txtfile:
        lines = txtfile.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if len(line) > 0:
                lines[index] = line
            else:
                lines.pop(index)
        return lines


def output_filename(txtpath):
    if txtpath is None:
        return 'demo.pdf'
    else:
        return txtpath.split(".")[0] + ".pdf"


def create_pdf(txtpath):
    paths = parse_images_paths(txtpath)
    if len(paths) > 0:
        firstpath = paths[0]
        size = get_image_mm_size(firstpath)
        width = size[0]
        height = size[1]
        fpdf = FPDF(orientation='P', unit='mm', format=size)
        for imagepath in paths:
            fpdf.add_page()
            fpdf.image(imagepath, 0, 0, width, height)
        outfilename = output_filename(txtpath)
        fpdf.output(outfilename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("txt", help="The plain text file that contains paths of images.")
    args = parser.parse_args()
    txt = args.txt
    try:
        create_pdf(txt)
    except Exception as e:
        print('Error: ' + str(e))
