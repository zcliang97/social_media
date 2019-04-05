class Client:

    def __init__(self):
        # directory is an array with each element being a new folder
        self.currentDir = []

    def ls(self, isArg):
        #print all results from table

    # results must be in ls -l format
    def find(self):

    def cd(self, folder):
        if folder == '..':
            # already at root folder
            if not self.currentDir:
                return
            # go back one folder
            else:
                self.currentDir.pop()
        elif folder == ".":
            return
        else:
            # do check to see if folder exists later
            self.currentDir.append(folder)

    def pwd(self):
        print "/" + "/".join(self.currentDir)