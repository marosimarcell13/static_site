import os
import shutil

from copy_static import copy_to_everything
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_template = "./template.html"
dir_path_content = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    copy_to_everything(dir_path_static,dir_path_public)


    generate_pages_recursive(dir_path_content,dir_path_template,dir_path_public)


main()