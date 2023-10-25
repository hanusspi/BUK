#log band and current symbol
def progress(input_list, index):
    if 0 <= index < len(input_list):
        result = ""
        for i in range(len(input_list)):
            if i == index:
                result += "["
                result += str(input_list[i])
                result += "]"
            else:
                result += str(input_list[i])
        return result
    else:
        print("Index is out of range.")

class TouringMachine:
    #create Touring Machine class
    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                #Read .TM file
                self.states = file.readline().strip('\n')
                self.alphabet = list(file.readline().strip('\n'))
                self.int_alphabet = list(file.readline().strip('\n'))
                self.begin_state = int(file.readline().strip('\n'))
                self.end_state = int(file.readline().strip('\n'))
                self.transitions = {}
                # Read and process each statetransition
                for line in file:
                    # fit the state transition in dictionary entries (tuple of old state and symbol for identifing)
                    # triple for new state, new symbol and next operation
                    tmp = line.strip("\n").split(" ")
                    self.transitions[int(tmp[0]), tmp[1]]=(int(tmp[2]), tmp[3], tmp[4]) 
        except FileNotFoundError:
            print(f"File '{file_path}' not found")
        except Exception as e:
            print(f"An error occurred: {e}")
    #execute the touring machine
    def execute(self, band):
        #init values
        s = self.begin_state
        i = 1
        band.insert(0,"B")
        band.append("B")
        #run until final state is reached
        while(s!=self.end_state):
            #search fitting transition profile from dict
            print(progress(band, i))
            t = self.transitions[(s,band[i])]
            #overwrite band entry
            band[i] = t[1]
            #update state 
            s = t[0]
            #translate movint instructions to index changes and increase buffer to left and right if needed
            if(t[2] == 'R'):
                i += 1
                if(i>=len(band)):
                    band.append('B')
            elif(t[2] == 'L'):
                i-=1
                if(i<=0):
                    band.insert(0,'B')
                    i+=1
        print(progress(band, i))    
        
        return progress(band, i)
        
file_path = input("Enter File Path: ")
band_input = input("Enter Band: ")
band = list(band_input)
tm = TouringMachine(file_path)
output = tm.execute(band)
print(output)