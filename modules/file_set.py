import pandas as pd
from matplotlib import rc, font_manager



class File_set:
    def __init__(self):
        self.columns_list = []
        self.position = 0
        self.number_list = []
        self.letter_list = []
        self.index_list = []
        self.null_list = []
        self.newColumns_list = []
        self.newNumber_list =[]
        self.newLetter_list = []

    # 읽을 파일을 로드하고 파일 데이터를 리턴한다.
    def file_load(self,file_name):
        rc('font', family="NanumGothic")
        data = pd.read_csv(file_name, sep=",", dtype='unicode', engine='python')
        return data

    # 파일 데이터의 columns 리스트를 리턴한다.
    def data_columns(self,data):
        for i in data.columns:
            self.columns_list.append(i)
        return self.columns_list

    # 파일 데이터 속 원하는 columns을 선택하고 그 columns의 데이터가 무엇으로 이루어져있는지 리스트로 반납한다.
    def index_list(self,data,columns):
        for i in data.columns.unique():
            self.index_list.append(i)
        return self.index_list

    # 파일 데이터 속 범주형 데이터와 이산형 데이터를 분류한다.
    def data_classification(self, data):
        self.position = 0
        for i in self.columns_list:
            # if(data[i].unique()[0].isdigit()):
            # if(type(float(data[i][0])) == float):
            if (self.isNumber(data[i][0])):
                self.number_list.append(self.columns_list[self.position])
            else:
                self.letter_list.append(self.columns_list[self.position])

            self.position += 1

        # for i in self.columns_list:
        #     if(type(float(data[i][0])) == float):
        #         self.number_list.append(self.columns_list[self.position])
        #     else:
        #         self.letter_list.append(self.columns_list[self.position])
        #     self.position += 1

    # Null 값을 많이 포함하고 있는 columns은 제거한후 새로운 columns list를 만든다.
    def list_mining(self, data):
        self.position = 0
        for i in self.columns_list:
            if '#NULL!' in data[i].unique():
                self.null_list.append(self.columns_list[self.position])
            else:
                self.newColumns_list.append(self.columns_list[self.position])
            self.position += 1

    # Null값을 제거한 새로운 columns list로  범주형 데이터와 이산형 데이터를 분류하는데... 위와 중복이라 차후에 개선할 여지가 있음.
    def newData_classification(self, data):
        self.position = 0
        for i in self.newColumns_list:
            # if(data[i].unique()[0].isdigit()):
            if(self.isNumber(data[i][0])):
                self.newNumber_list.append(self.newColumns_list[self.position])
            else:
                self.newLetter_list.append(self.newColumns_list[self.position])
            self.position += 1

        # for i in self.newColumns_list:
        #     if(type(float(data[i][0])) == float):
        #         self.newNumber_list.append(self.newColumns_list[self.position])
        #     else:
        #         self.newLetter_list.append(self.newColumns_list[self.position])
        #     self.position += 1

    #다른 엑셀 파일을 읽을것을 대비해서 posterior_weight에 대한 예외 처리 구문을 따로 두었음.
    def set_except(self,Letterlist,Numberlist):
        Letterlist.remove('posterior_weight')
        Numberlist.append('posterior_weight')

    def get_newColumns(self):
        return self.newColumns_list

    def get_newNumber(self):
        return self.newNumber_list

    def get_newLetter(self):
        return self.newLetter_list

    def getNumber(self):
        return self.number_list

    def getLetter(self):
        return self.letter_list

    def isNumber(self,str):
        try:
            tmp = float(str)
            return True
        except:
            return False



if __name__ == "__main__":
    print(3)