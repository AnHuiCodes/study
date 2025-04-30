from is_pkg import is_data
from gdt_pkg import gdt_pkg
from kslm_pkg import kslm_data
from bqt_pkg import bqt_data

print(len(set(is_data + gdt_pkg + kslm_data + bqt_data)))
