#!C:\Users\Peter.W\PycharmProjects\violin\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'truth-table-generator==1.1.2','console_scripts','ttg_cli.py'
__requires__ = 'truth-table-generator==1.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('truth-table-generator==1.1.2', 'console_scripts', 'ttg_cli.py')()
    )
