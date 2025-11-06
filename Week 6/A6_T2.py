def writeFile(FileName, Content) -> None: 
    Filehandle = open(FileName, 'w', encoding="UTF-8")
    Filehandle.write(Content)
    Filehandle.close()
    return None 

def main() -> None: 
    print("Program starting.")
    FirstName = input ("Insert first name: ")
    LastName = input ("Insert last name: ")
    FileName = input ("Insert filename: ")
    Content = "{}\n{}\n".format(FirstName, LastName)
    writeFile(FileName, Content) #Jump to writeFile Function and send
                                # the file name and content as a parameter
    print("Program ending.")
    return None 

if __name__ == "__main__":
    main()