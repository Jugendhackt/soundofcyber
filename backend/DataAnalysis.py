import request_data as rq
import random

FrequencyList = [16.35,17.32,18.35,19.45,20.60,21.83,23.12,24.50,25.96,27.50,29.14,30.87, 32.70,34.65,36.71,38.89,41.20,43.65,46.25,49.00,51.91,55.00,58.27,61.74,
                 65.41,69.30,73.42,77.78,82.41,87.31,92.50,98.00,103.8,110.0,116.5,123.5, 130.8,138.6,146.8,155.6,164.8,174.6,185.0,196.0,207.7,220.0,233.1,246.9,
                 261.6,277.2,293.7,311.1,329.6,349.2,370.0,392.0,415.3,440.0,466.2,493.9, 523.3,554.4,587.3,622.3,659.3,698.5,740.0,784.0,830.6,880.0,932.3,987.8,
                 1047,1109,1175,1245,1319,1397,1480,1568,1661,1760,1865,1976, 2093,2217,2349,2489,2637,2794,2960,3136,3322,3520,3729,3951,
                 4186,4435,4699,4978,5274,5588,5920,6272,6645,7040,7459,7902]
ResultsTable = {}
NoteLength = [0.2,0.4,0.6,0.8]

def Interpret():
    Return = []
    Data = str(rq.get_data(0))
    Data = int(Data.split(" ")[1].replace(">","").replace("[","").replace("]",""))
    for i in range(0,10):
        Note = {"freq" : Analysis().RoundToNearest(Data), "lenght": NoteLength[random.randint(0,4)]}
        Return.append(Note)
    return Return

class Analysis:
    def Decode(self,Data,APIs):
        Outputs = []
        Inputs = []
        Normal = []
        Sounds = []
        AllNodes = Data.split(";")
        for n in AllNodes:
            # Separate Input Into Nodes and Sort by Category
            if(n.startswith("O")):
                Outputs.append(n)
            elif(n.startswith("I")):
                Inputs.append(n)
                Num = n.split("_")[0]
                APIResult = APIs[int(n.split("_")[1])]
                ResultsTable[Num] = APIResult
            else:
                Normal.append(n)

            # Solve All N-Nodes
            for Node in Normal:
                if(Node.split("_")[0] in ResultsTable):
                    pass
                else:
                    Analysis.Solve(Node,AllNodes)

            #Solve Outputs
            for Node in Outputs:
                Dependencies = Node.split("_")[1].split(",")
                DataDict = {}
                DataDict["freq"] = Analysis.RoundToNearest(int(ResultsTable.get(Dependencies[0])))
                DataDict["length"] = ResultsTable.get(Dependencies[1])
                Sounds.append(DataDict)
        return Sounds

    def Solve(self,Node,AllNodes):
        Dependencies = Node.split("_")[1].split(",")
        Dependend_Nodes = Dependencies[1],Dependencies[2]
        Data = []
        Type = Dependencies[0]
        for N in Dependend_Nodes:
            if(N in ResultsTable):
                Data.append(ResultsTable.get(N))
            else:
                Analysis.Solve(N)
        Result = 0
        Data[0] = int(Data[0])
        Data[1] = int(Data[1])

        if(Type == "A"):
            Result = Data[0]+Data[1]
        elif(Type == "S"):
            Result = Data[0]-Data[1]
        elif(Type=="D"):
            Result = Data[0]/Data[1]
        elif(Type=="M"):
            Result = Data[0]/Data[1]
        ResultsTable[Node.split("_")[0]] = Result


    def RoundToNearest(self,Number):
        Smallest = 100000
        Target = Number
        for i in FrequencyList:
            Error = abs(Number-i)
            if(Error < Smallest):
                Smallest = abs(Number-i)
                Target = i
        return Target


MyNetwork = "I1_1;I2_3;I3_8;N1_A,I1,I2;O1_I3,N1"
print(Interpret());
#Sounds = Analysis.Decode(MyNetwork)
#print(Sounds)



