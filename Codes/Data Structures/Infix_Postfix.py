from LinkedList import LinkedList

def InToPost(infix):
    postfix = []
    symbols = LinkedList()
    chars = infix.split(" ")
    for char in chars:
        if char.isnumeric():
            postfix.append(char)
        elif char == "(":
            symbols.push(char)
        elif char == ")":
            symbol = ""
            while symbols.count()>0 and symbol != "(":
                symbol = symbols.pop()
                if symbol != "(" :
                    postfix.append(symbol)
            print(postfix)
        else:
            symbols.push(char)
    while symbols.count()>0:
        postfix.append(symbols.pop())
    return " ".join(postfix)

print(InToPost("3 * ( 8 + 5 + 10 )"))
# nope still wrong output     
# need check for the issue                
                
