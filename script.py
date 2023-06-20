import os
import polib

# Obtener todos los archivos .po en el directorio actual
po_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.po')]

# Comprueba si hay exactamente un archivo .po
if len(po_files) == 1:
    filename = po_files[0]
elif len(po_files) > 1:
    filename = input("There are multiple .po files in the current directory 🤔. Please enter the name of the file you want to sort:")
else:
    print("No .po files found in current directory. 😭")
    exit(1)

# Cargar el archivo .po
po = polib.pofile(f"{filename}.po")

# Ordenar los términos alfabéticamente
po.sort(key=lambda t: t.msgid)

# Guardar el resultado, lo que también envolverá las líneas
po.save()

print(f"Sorted {filename}.po! 🎉")
