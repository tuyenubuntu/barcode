import sys
# from io import StringIO


# sys.stdin = StringIO('test')


items = {"823409707147":['Al12','123','Al12.png']}



while True:
    print ("show your barcode")
    value = input()
    print (value)
    # if value == "exit":
    #     break 
    for key in items.keys():
        if key==value:
            print (items[key])
            break
    # else:
    #     print ("Item not found")
