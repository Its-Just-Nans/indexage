"""builder"""

import argparse
import os
from os import makedirs, listdir
from os.path import getmtime, getsize, join
from datetime import datetime

from .assets import FOLDER_ICO, HTML_TEMPLATE, ROW_TEMPLATE, UNKNOWN_ICO, CSS


def size(size_in_bytes):
    """convert"""
    size_kb = size_in_bytes / 1024.0
    size_mb = size_kb / 1024.0

    if size_mb >= 1:
        return f"{size_mb:.2f}M"
    elif size_kb >= 1:
        return f"{size_kb:.2f}K"
    return size_in_bytes


IMAGES_EXTS = ["png", "jpg", "jpeg", "tiff", "svg"]


def create_html_index(path_to_folder, html_template, options):
    """create an index.html"""
    folder_list = sorted(os.listdir(path_to_folder))
    buffer_rows = ""
    current_template = f"{html_template}"
    correct_html = current_template.replace(
        "<title></title>", f"<title>Index of {path_to_folder}</title>"
    )
    folder_name = path_to_folder[2:]
    link_to_add = ""
    if options["link"]:
        link = f"{options['link']}{folder_name}"
        link_to_add = f' - <a href="{link}">{link}</a>'
    correct_html = correct_html.replace(
        "<h1></h1>",
        f"<h1>Index of {path_to_folder}{link_to_add}</h1>",
    )
    for one_element in folder_list:
        if one_element == "index.html" or one_element in options["exclude"]:
            continue
        path_to_element = join(path_to_folder, one_element)
        if path_to_element in options["exclude"]:
            continue
        isdir = os.path.isdir(path_to_element)
        date = datetime.fromtimestamp(getmtime(path_to_element)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        url = FOLDER_ICO if isdir else UNKNOWN_ICO
        preview = options["preview"] and not isdir
        add = 'class="thumbnail"' if preview else ""
        other = ""
        if preview:
            extension = one_element[one_element.rfind(".") + 1 :]
            if extension in IMAGES_EXTS:
                other = f'<span><img src="{one_element}"></span>'
            else:
                other = f'<span><iframe src="{one_element}"></iframe></span>'
        buffer_rows += ROW_TEMPLATE.substitute(
            file=one_element,
            date=date,
            size=size(getsize(path_to_element)),
            url=url,
            add=add,
            other=other,
        )
        if isdir and one_element not in options["exclude"]:
            makedirs(options["output"], exist_ok=True)
            new_output = join(options["output"], one_element)
            new_options = options.copy()
            new_options["output"] = new_output
            if options["verbose"]:
                print(f"making {path_to_element}")
            create_html_index(path_to_element, html_template, new_options)
    file_data = correct_html.replace("<placeholder></placeholder>", buffer_rows)
    output_index = join(options["output"], "index.html")
    if not options["force"] and os.path.exists(output_index):
        raise FileExistsError(f"File {output_index} already exists, aborting")
    with open(output_index, "w", encoding="utf-8") as file:
        file.write(file_data)


def main():
    """main function"""
    parser = argparse.ArgumentParser(
        prog="indexage", description="Create apache2-like html index"
    )
    parser.add_argument("-o", "--output", type=str, help="Output folder", default=".")
    parser.add_argument(
        "-force",
        "--force",
        action=argparse.BooleanOptionalAction,
        type=bool,
        help="Force writing index.html",
        default=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action=argparse.BooleanOptionalAction,
        type=bool,
        help="Add verbosity",
        default=False,
    )
    parser.add_argument(
        "-e", "--exclude", action="append", help="Exclude folder name", default=list()
    )
    parser.add_argument("-r", "--recursive", type=str, help="Recursive", default=True)
    parser.add_argument("-l", "--link", type=str, help="Add repo link", default="")
    parser.add_argument(
        "-p",
        "--preview",
        action=argparse.BooleanOptionalAction,
        type=bool,
        help="Add preview when hovering",
        default=False,
    )
    parser.add_argument("path", type=str, help="Paths to index")
    args = parser.parse_args()
    if args.verbose:
        print(args)
    options = {
        "exclude": args.exclude,
        "verbose": args.verbose,
        "link": args.link,
        "preview": args.preview,
        "force": args.force,
        "output": args.output.strip() == "" and "." or args.output,
    }
    template = HTML_TEMPLATE
    if options["preview"]:
        template = template.replace("<style></style>", f"<style>{CSS}</style>")
    create_html_index(args.path, template, options)
