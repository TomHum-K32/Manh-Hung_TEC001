import re

def hex_color(color):
    color_check = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(color_check, color))

print(hex_color("#FFA90A"))  
print(hex_color("#1245Z")) 
print(hex_color("#ff77cc"))  
