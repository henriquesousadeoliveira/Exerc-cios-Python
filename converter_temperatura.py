esc_orig = input()
temp_orig = float(input())
esc_dest = input()

if esc_orig == "c":
    celsius = temp_orig
elif esc_orig == "f":
    celsius = (temp_orig - 32) / 1.8
elif esc_orig == "k":
    celsius = temp_orig - 273
elif esc_orig == "r":
    celsius = (temp_orig + 273.15) * 1.8

if esc_dest == "c":
    temp_dest = celsius
elif esc_dest == "f":
    temp_dest = 1.8 * celsius + 32
elif esc_dest == "k":
    temp_dest = celsius + 273
elif esc_dest == "r":
    temp_dest = (celsius + 273.15) * 1.8

print(temp_dest)