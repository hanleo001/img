import os

pathlst=[]
filelst=[]

# print(os.listdir())



def get_dir_reclusively(root, basedir, level=1):
    contents = os.listdir(os.path.join(basedir, root))
    res = []
    for dir in contents:
        if os.path.isdir(os.path.join(root, dir)) and dir[0] != ".":
            res.append((level, "dir", dir))
            res.extend(get_dir_reclusively(os.path.join(root, dir), basedir, level+1))
        elif dir[-4:] == ".png" or dir[-4:]==".jpg":
            res.append((level, "file", os.path.join(root, dir)))
    return res



def write_to_md(methods, domain, file_list, basedir):
    with open(os.path.join(basedir, "index2.md"), "wt", encoding="utf-8") as index:
        index.write("# 目录\n")
        for level, ftype, filepath in file_list:
            if ftype == "dir":
                index.write("## " + "  " * (level - 1) + filepath + "\n")
            elif ftype == "file":
                title = os.path.splitext(os.path.basename(filepath))[0]
                path = "/".join(filepath.split("\\"))
                index.write("* " + "  " * (level - 1) + f"[{title}]({methods}://{domain}/{path})\n")


def write_to_md_2(methods, domain, file_list, basedir):
    with open(os.path.join(basedir, "index2.md"), "wt", encoding="utf-8") as index:
        index.write("# 目录\n")
        for level, ftype, filepath in file_list:
            if ftype == "dir":
                index.write("#" * (level+1)+ ' ' + filepath + "\n")
            elif ftype == "file":
                title = os.path.splitext(os.path.basename(filepath))[0]
                path = "/".join(filepath.split("\\"))
                index.write("- " + f"[{title}]({methods}://{domain}/{path})\n")


def write_to_md_3(methods, domain, file_list, basedir):
    with open(os.path.join(basedir, "index3.md"), "wt", encoding="utf-8") as index:
        index.write("# 目录\n")
        for level, ftype, filepath in file_list:
            if ftype == "dir":
                index.write("- " * (level+1)+ ' ' + filepath + "\n")
            elif ftype == "file":
                title = os.path.splitext(os.path.basename(filepath))[0]
                path = "/".join(filepath.split("\\"))
                index.write("- "* (level+1) + f"[{title}]({methods}://{domain}/{path})\n")


def write_to_md(methods, domain, file_list, basedir):
    with open(os.path.join(basedir, "index.md"), "wt", encoding="utf-8") as index:
        index.write("# 目录\n")
        for level, ftype, filepath in file_list:
            if ftype == "dir":
                index.write(">" * (level)+ ' ' + filepath + "\n")
                index.write(">"*level + "\n")
            elif ftype == "file":
                title = os.path.splitext(os.path.basename(filepath))[0]
                path = "/".join(filepath.split("\\"))
                index.write(">"*(level) + "- " + f"[{title}]({methods}://{domain}/{path})\n")
                index.write(">"*level + "\n")



if __name__ == "__main__":
    BASEDIR = r"E:\www\site\img"
    file_list = get_dir_reclusively("", BASEDIR)
    print(file_list)
    write_to_md(
        "https",
        "img.leoh.top",
        file_list,
        BASEDIR
    )


