import json

class TAComment:
    def __init__(self, filedata) -> None:

        self.filedata = filedata
        self.__requried = ["comment","lines"]
        self.__start = 0
        self.__end = 0
        self.__startstate = False
        self.__string_container = ""
        self.__lines_container = []
        self.__lines_num = 0
        self.__status = True
        self.__out = ""

    @property
    def out(self):
        return self.__out

    def run(self):
        for line in self.filedata:
            self.__lines_num += 1
            self.__condition_state(line)
        return self.__lines_container

    def __condition_state(self,line):
        if "#>>> :end:" in line and self.__startstate:
            self.__have_end(line)
        elif self.__startstate:
            self.__add_line(line)
        elif "#>>> :end:" in line and not self.__startstate:
            self.__can_not_find_start(line)
        if "#>>> :start:" in line and self.__startstate:
            self.__did_not_have_end_point()
        if "#>>> :start:" in line:    
            self.__have_start()

    def __check_comment_syntax(self,data):
        return self.__requried != list(data.keys())


    def __did_not_have_end_point(self):
        self.__out += f"syntax error line:{self.__lines_num-1}\n     <not have end point>\n"
        self.__status = False
        self.__have_start()

    def __have_end(self,line):
        self.__end = self.__lines_num
        self.__startstate = False
        data = self.__org_info(self.__split_line_data(line))
        if self.__check_comment_syntax(data):
            self.__not_follow_req(line)
            return
        data["lines"] = {f"{self.__start}-{self.__end}":self.__string_container}
        self.__lines_container.append(data)

    def __not_follow_req(self,line):
        self.__out += f"syntax error line:{self.__lines_num}\n"
        self.__out += f"     <This comment not follow the requriement : {self.__requried}>\n"
        self.__out += f"     {line}\n"
        self.__status = False

    def __have_start(self):
        self.__start = self.__lines_num
        self.__string_container = ""
        self.__startstate = True

    def __add_line(self,line):
        self.__string_container += line

    def __can_not_find_start(self,line):
        self.__out += f"syntax error line:{self.__lines_num}\n     <not found starting point>\n     {line}"
        self.__status = False

    def __org_info(self,element):
        data = {}
        for i in element:
            pre_data = i.split("=")
            data[pre_data[0].strip()] = pre_data[1].strip()
            data[f"lines"] = {f"{self.__start}-{self.__end}":self.__lines_container}
        return data

    def __split_line_data(self,line):
        elementline = line[11:]
        element = elementline.split(",")
        return element

