

def fileType(string):

    text = string.split('.')
    resualt = text[1:]
    
    print (' '.join(resualt))



str = input("Enter your file :")
fileType(str)