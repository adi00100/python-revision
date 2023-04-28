class File:
    def __init__(self,file_name,mode):
        self.file_name=file_name
        self.mode=mode
    
    def __enter__(self):
            self.file=open(self.file_name,self.mode)
            return self.file

    def __exit__(self,exc_type,exc_value,traceback):
            self.file.close()

with File("temp","w") as f:
      f.write("Hello world")