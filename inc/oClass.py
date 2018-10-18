import sys
import fileinput


class hostOptions:
    def __init__(self):
        print("Hosts App Started!")
        self.switcher = {
            "list" : "list",
            "add" : "add",
            "disable" : "disable",
            "remove" : "remove",
            "enable" : "enable",
            "listArgs" : "listArgs"
        }

    def listArgs(self):
        print("\n\nAvailable commands:")
        for cmd_txt in self.switcher:
            print(cmd_txt)

    def serveArgs(self):
        switcher = self.switcher
        getattr(self, switcher.get(sys.argv[1],"invalid"))()

    def invalid(self):
        print("Invalid arg!")

    def list(self):
        file = open("/etc/hosts", "r")
        count = 0;
        for line in file.readlines():
            print("("+str(count)+")   " + line)
            count = count + 1

        file.close()


    def add(self):
        if len(sys.argv) <= 2:
            print("You need to add a host!")
            return

        file = open("/etc/hosts", "a+")

        if 3 in sys.argv:
            file.write(sys.argv[3]+"       "+sys.argv[2]+"\n")
        else:
            file.write("127.0.0.1       " + sys.argv[2]+"\n")

        print("Host added!")

    def enable(self):

        if len(sys.argv) <= 2:
            print("Add number")
            return

        lineSelected = self.getString(sys.argv[2])
        all_lines = lineSelected[1]
        lineSelected = lineSelected[0]
        if self.check_if_commented(lineSelected) != -1:
            print("Already enabled")
            return

        file_write = open("/etc/hosts", "w+")

        for line in all_lines:
            if (line == lineSelected):
                file_write.write("#"+line)
            else:
                file_write.write(line)

        file_write.close()

    def getString(self, line_number):
        file = open("/etc/hosts", "r")
        count = 0
        selected = int(line_number)
        lineSelected = ""
        all_lines = file.readlines();
        for line in all_lines:
            if selected == count:
                lineSelected = line
                break
            count = count + 1

        file.close()

        return [lineSelected, all_lines]

    def check_if_commented(self, line):
        return line.find("#")

    def disable(self):
        if len(sys.argv) <= 2:
            print("Add number")
            return

        lineSelected = self.getString(sys.argv[2])
        all_lines = lineSelected[1]
        lineSelected = lineSelected[0]
        if self.check_if_commented(lineSelected) == -1:
            print("Already disabled")
            return

        temp_line = lineSelected.replace('#', '');

        file_write = open("/etc/hosts", "w+")

        for line in all_lines:
            if (line == lineSelected):
                file_write.write(temp_line)
            else:
                file_write.write(line)

        file_write.close()

    def remove(self):
        if len(sys.argv) <= 2:
            print("Add number")
            return

        lineSelected = self.getString(sys.argv[2])
        all_lines = lineSelected[1]
        lineSelected = lineSelected[0]

        file_write = open("/etc/hosts", "w+")

        for line in all_lines:
            if (line != lineSelected):
                file_write.write(line)

        file_write.close()
