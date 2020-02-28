class MycustomError(TypeError):
    """
    Error with specific error code
    """

    def __init__(self,message,code):
        super().__init__(f"Error code:{code} :{message}")

raise MycustomError("Ouch error happend!",500)
#error=MycustomError("error happend",450)
#print(error.__doc__)