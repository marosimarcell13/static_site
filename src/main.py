import os
import shutil
import sys

from copy_static import copy_to_everything
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs = "./docs"
dir_path_template = "./template.html"
dir_path_content = "./content"

basepath = sys.argv[0]
print(basepath)

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    
    copy_to_everything(dir_path_static,dir_path_docs)


    generate_pages_recursive(dir_path_content,dir_path_template,dir_path_docs,basepath)


main()