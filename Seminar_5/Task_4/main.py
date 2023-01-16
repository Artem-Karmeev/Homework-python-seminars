from data_function import read_file, record_file
from head import packing, inpack
from input_function import console_input
from config import link_inp, link_out

console_input(link_inp)
original_data = read_file(link_inp)

if original_data[0].isdigit():
    result = inpack(original_data)
    record_file(result, link_out)
else:
    result = packing(original_data)
    record_file(result, link_out)    












