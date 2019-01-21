class UserInputError(Exception):
    def __init__(self):
        self.omni_msg = "ERROR: "
    
    def send_msg(self):
        return self.omni_msg
    pass

class NotNumericError(UserInputError):
    def __init__(self):
        self.msg = self.send_msg + "User supplied a non-numeric value!"
        super()
    pass

class NotAlphabeticError(UserInputError):
    def __init__(self):
        self.msg = self.send_msg + "User supplied a non-alphabetic value!"
        super()
    pass

def main():
    s = input("Write some cool: ")

    for ch in s:
        try:
            
            if str(ch).isalpha() == True:
                raise NotNumericError
            
            elif str(ch).isalnum() == True:
                raise NotAlphabeticError
        
        except NotNumericError as num_err:
            print(num_err.msg)

        except NotAlphabeticError as alph_err:
            print(alph_err.msg)

if __name__ == "__main__":
    main()