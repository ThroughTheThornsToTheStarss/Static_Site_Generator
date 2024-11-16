
from copystatic import  clear_directory, copy_recursive
from extract_title import generate_pages_recursive
path_copy = "./static"
path_base = "./public"
path_dest = "./content"


def main():
    
    print("Deleting public directory...")
    clear_directory(path_base)

    print("Copying static files to public directory...")
    copy_recursive(path_copy, path_base)

    generate_pages_recursive( path_dest,"./template.html", path_base)


if __name__ == "__main__":
    main()