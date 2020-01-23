import subprocess
# file and directory listing
returned_text = subprocess.check_output("ls -ltr", shell=True, universal_newlines=True)
texto_buscado = subprocess.check_output("ls -ltr | awk \'{print($8,$NF)}\'", shell=True, universal_newlines=True)
print(texto_buscado)
