# version 1.0 2025-09-29 00:12:59
import os
import shutil
import sys
from pathlib import Path

OUTPUT_DIR = 'output'

def remove_bom(file):
    '''
    remove bom from file
    :param file:
    :return:
    '''
    try:
        with open(file, 'rb') as f:
            content = f.read()
            if content.startswith(b'\xef\xbb\xbf'):
                print(f'file {file} with BOM')
                output_file = Path(str(file).replace(str(path), str(output)))
                Path(output_file.parent).mkdir(parents=True, exist_ok=True)
                with open(output_file, 'wb') as nf:
                    nf.write(content[3:])
                print(f'output file: {output_file}')
    except Exception as e:
        print(f'Read {file} error: {e}')


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: python remove_bom.py <path>')
        sys.exit(0)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f'{path} is not exist')
        sys.exit(0)

    output = Path(OUTPUT_DIR + os.sep + path.name)
    if output.exists():
        shutil.rmtree(output)
        print(f'delete {output}')

    for file in path.rglob('*'):
        if file.is_file():
            remove_bom(file)
