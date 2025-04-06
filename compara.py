import filecmp
import os

def compare_projects(dir1, dir2):
    diff = filecmp.dircmp(dir1, dir2)
    print("Arquivos diferentes:", diff.diff_files)
    print("Arquivos apenas em", dir1 + ":", diff.left_only)
    print("Arquivos apenas em", dir2 + ":", diff.right_only)

compare_projects("Producao", "saips")
