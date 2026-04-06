#Cho một biến dictionary như sau:
# layers = {
# "layer-11": {
#"layer-21": 90
#"layer-22": {
#"layer-31": 43
#}
# },
# "layer-12": 35
#}
#In giá trị của layer-12 và layer-31
layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}

print("Giá trị của layer-12:", layers["layer-12"])
print("Giá trị của layer-31:", layers["layer-11"]["layer-22"]["layer-31"])