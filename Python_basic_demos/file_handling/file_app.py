# this is application to show all demo at once

# logger and logging config
import logging

logging.basicConfig(filename="file_app_logs.log", filemode='a', format='%(levelname)s %(created)f %(name)s  %(message)s %(asctime)s',
                    datefmt='%d %m %y', level=logging.DEBUG)
# logger object with name
logger = logging.getLogger("file_app_logger")


# function to handle reading of file
def read_file():
    try:
        name = str(input("Enter name of file "))
        logger.info("file name entered")
        f = open(name, 'r')
        logger.info("file object opened")
        print(f"This is content of file\n{f.read()}")
        logger.info("file reading complete")
    except Exception as Argument:
        logging.exception(f"file reading error occurred {Argument}")
    finally:
        logger.info("file object closed")
        f.close()


# function to handle writing in file
def write_file():
    try:
        name = str(input("Enter the name of file "))
        logger.info("file name entered")
        f = open(name, 'w')
        logger.info("file object opened")
        f.write(input("write file data\n"))
        logger.info("file writing complete")
    except Exception as Argument:
        logging.exception(Argument)
    finally:
        logger.info("File object closed")
        f.close()


while True:
    print("1. Read file\n2. Write file\n3. exit")
    choice = input("Enter your choice\n")
    match choice:
        case "1":
            logger.info("user select 1")
            read_file()

        case "2":
            logger.info("user select 2")
            write_file()

        case "3":
            logger.info("////End/////\n ")
            break
