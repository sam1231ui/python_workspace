# this is used to read write from file

# task to write whole line from console
f = open('Text.txt', "w")

while True:
    data = input("Enter the data: ")
    if data == "exit":
        break
    else:
        f.write(data + "\n")


# logger example
# import logging
# import logging.config
#
# logging.basicConfig(filename="newfile.log", format='%(asctime)s %(name)s %(levelname)s %(message)s', filemode='a', level=logging.DEBUG)
#
# logger = logging.getLogger("file_logger")
# # f = open("Text.txt", "r")
#
# # print(f.read())
# logger.info("reading of file completed")
# logger.debug("Harmless debug Message")


