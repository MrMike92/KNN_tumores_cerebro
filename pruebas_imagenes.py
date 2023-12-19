"""MIT License
Copyright (c) 2023 MrMike92
Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricciones, incluyendo, sin limitación, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software a hacerlo, sujeto a las siguientes condiciones:
El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o porciones sustanciales del Software.
EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR CUALQUIER RECLAMO, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE."""

import os
import shutil

def copy_files(source_folder, destination_folder, prefix):
    count = 1
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpeg'):  # Cambiar si la extensión de las imágenes tienen una diferente
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, f'{prefix}{count:03}.jpeg')
            shutil.copyfile(source_path, destination_path)
            count += 1

# Directorios de origen y destino
yes_folder = r'yes'
no_folder = r'no'
test_folder = r'test'

# Copiar imágenes de la carpeta YES a la carpeta TEST
copy_files(yes_folder, test_folder, 'b')

# Copiar imágenes de la carpeta NO a la carpeta TEST
copy_files(no_folder, test_folder, 'p')