def write(message: str):
    file = open("text.txt", "w")
    try:
        file.write(message)
    except Exception as e:
        print(f"Error while writing message\n  {e}")
    finally:
        file.close()

def write_better(path: str, message: str):
    file = open(path, 'w')
    try:
        file.write(message)
    except Exception as e:
        print(f"Error while writing {message} to {path}")
    finally:
        file.close()

def write_better_l(path: str, message: list):
    file = open(path, 'w')
    try:
        file.writelines(message)
    except Exception as e:
        print(f"Error while writing {message} to {path}")
    finally:
        file.close()
