import os

from markdown_blocks import extract_title, markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    file = open(from_path,"r")
    temp_template = file.read()
    file.close()

    file = open(template_path,"r")
    temp_markdown = file.read()
    file.close()

    #print(temp_template)
    #print(temp_markdown)

    title = extract_title(temp_markdown)
    html = markdown_to_html_node(temp_markdown).to_html()

    with_title = temp_template.replace("{{ Title }}",title)
    result = with_title.replace("{{ Content }}", html)
    #print(result)

    with open(dest_path, "w") as file:
        file.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        dir_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(dir_path):    
            file = open(dir_path,"r")
            temp_markdown = file.read()
            file.close()
            file = open(template_path,"r")
            temp_template = file.read()
            file.close()
            title = extract_title(temp_markdown)
            html = markdown_to_html_node(temp_markdown).to_html()

            with_title = temp_template.replace("{{ Title }}",title)
            result = with_title.replace("{{ Content }}", html)
            result_1 = result.replace('href="/', f'href="{basepath}/')
            result_2 = result_1.replace('src="/', f'src="{basepath}/')

            dest_dir_path1 = os.path.dirname(dest_path)
            if dest_dir_path1 != "":
                os.makedirs(dest_dir_path1, exist_ok=True)

            with open(os.path.join(dest_dir_path1,"index.html"), "w") as file:
                file.write(result_2)
        else:
            generate_pages_recursive(dir_path,template_path,dest_path,basepath)