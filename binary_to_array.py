input_filename = 'received_yuv_data.bin'
output_filename = 'yuv_data_array.h'
array_name = 'yuvData'

with open(input_filename, 'rb') as f_in, open(output_filename, 'w') as f_out:
    data = f_in.read()
    f_out.write("#pragma once\n\n")
    f_out.write(f"const uint8_t {array_name}[] = {{\n")
    for byte in data:
        f_out.write(f" 0x{byte:02X},")
    f_out.write("\n};\n\n")
    f_out.write(f"const size_t {array_name}Size = sizeof({array_name});\n")
