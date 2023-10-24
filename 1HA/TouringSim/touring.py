class TouringMachine:
    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.states = file.readline().strip('\n')
                self.alphabet = list(file.readline().strip('\n'))
                self.int_alphabet = list(file.readline().strip('\n'))
                self.begin_state = int(file.readline().strip('\n'))
                self.end_state = int(file.readline().strip('\n'))
                self.transitions = {}
                # Read and process each line in the file
                for line in file:
                    # Do something with each line, for example, print it
                    tmp = line.strip("\n").split(" ")
                    self.transitions[int(tmp[0]), tmp[1]]=(int(tmp[2]), tmp[3], tmp[4])  # 'end='' to avoid double spacing (lines already have newline characters)
        except FileNotFoundError:
            print(f"File '{file_path}' not found")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def execute(self, band):
        s = self.begin_state
        i = 1
        band.insert(0,"B")
        band.append("B")
        while(s!=self.end_state):
            t = self.transitions[(s,band[i])]
            band[i] = t[1]
            s = t[0]
            if(t[2] == 'R'):
                i += 1
            elif(t[2] == 'L'):
                i-=1
        band.pop()
        band.pop(0)
        
        return band
    
file_path = input("Enter File Path: ")
band_input = input("Enter Band: ")
band = list(band_input)
tm = TouringMachine(file_path)
output = tm.execute(band)
print(output)