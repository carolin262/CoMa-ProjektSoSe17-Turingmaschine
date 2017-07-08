import visual

class TM(object):
    # Turingmachine class which will be inherited by the more specified one
    #   always starts with state q0, and head_pos =0
    #   input_alphabet gets seperated from ,
    #   table gets seperated from , and > 
    def __init__(self, input_alphabet, blank, description, num_tapes, num_states, gamma, F):
        self.blank = blank
        self.F=F
        self.num_tapes=num_tapes
        self.num_states=num_states
        self.gamma=gamma
        self.state = 'q0'
        head_pos = 0
        self.input_alphabet = input_alphabet.split(',')
        self.table = { tuple(x.strip().split(',')) : y.strip().split(',') for x,y in (l.split('>') for l in description) }

    def exec_TM(inputstring):
        pass # overwritten

    def exec_TMHELP(inputstring):
        pass # overwritten


    def check_input(self, tape):
        """
        checks whether input is based on the input_alphabet and blanks
        input: tape List
        output: tape List
        """
        print('blank',self.blank, 'alphabet',self.input_alphabet)
        return all((i == self.blank or i in self.input_alphabet for i in tape))

    def fix_tape(self, tape, head_pos):
        """
        checks whether the tape is too short
        if so, it appends an blank to the right side
        Input: tape List
               head_pos Int
        Output: 0/1 , tape, head_pos
                
        """
        # did we leave the tape to the left?
        if head_pos < 0:
            return 1, [self.blank] + tape, 0
        # did we leave the tape to the right?
        if head_pos >= len(tape):
            return 0, tape + [self.blank], head_pos
        return 0, tape, head_pos

    def translate_dir(self, direction):
        """
        Input: direction String
        Output: 1/-1/0 Int
        Converts R to 1
        and L to -1
        """
        if direction == "R": return 1
        if direction == "L": return -1
        return 0 # N or other letters

    @staticmethod
    def _parse_file(path):
        """
        Opens file under path, 
        Input: path link to file
        Output: Uebergangstabelle as turingmachine
                conform lines
        """
        print("Reading file",path)
        with open(path, 'r') as f:
            return read_tm(iter(f.readlines()))

class OneTapeTM(TM):
    #   class of One Tape Turingmachine,
    #   inherited of Turingmachine class at the top
    def __init__(self, input_alphabet, blank, description, num_tapes, num_states, gamma, F):
        TM.__init__(self, input_alphabet, blank, description, num_tapes, num_states, gamma,F)

    def exec_TM(self,inputstring):
        #Input: inputstring String
        #Output: List of Uebergangszustaenden for the visualisation
        return list(self.exec_TMHELP(inputstring))

    def exec_TMHELP(self, initial_tape):
        """
        If input is not correct -> Assertion Error
        endless remembers each position, thus infinitloops can be detected
        If combination of state and tape-number exist
            tape, head_position will be overwritten 
            and yield returns them
        Input: initial_tape String
        Output: Tupel for Visualisation
        """
        ok=self.check_input(initial_tape)
        assert  ok
        head_pos = 0
        tape = initial_tape[:]
        shift_count = 0;
        endless=set()
        while True:
            remember = self.state, head_pos, tuple(tape)
            if remember in endless :
                print("Endlosschleife")
                break
            else:
                endless.add(remember)
            shift, tape, head_pos = self.fix_tape(tape, head_pos)
            shift_count += shift

            state_tuple = (self.state, tape[head_pos])
            if not state_tuple in self.table:
                break # no transition left

            #do the transition
            new_state, write, direct = self.table[state_tuple]
            new_pos = head_pos + self.translate_dir(direct)
            
            yield head_pos - shift_count, write, new_state, new_pos - shift_count

            tape[head_pos] = write
            head_pos = new_pos
            self.state = new_state
            #print(["B"]*(3-shift_count)+tape)

class TwoTapeTM(TM):
    #   class of Two Tape Turingmachine,
    #   inherited of Turingmachine class at the top

    def __init__(self, input_alphabet, blank, description, num_tapes, num_states, gamma, F):
        TM.__init__(self, input_alphabet, blank, description, num_tapes, num_states, gamma, F)
        head_pos2 = 0

    
    def exec_TM(self,inputstring):
        #Input: inputstring String
        #Output: List of Uebergangszustaenden for the visualisation
        return list(self.exec_TMHELP(inputstring))

    def exec_TMHELP(self, initial_tape, initial_tape2=[]):
        """
        If input is not correct -> Assertion Error
        endless remembers each position, thus infinitloops can be detected
        If combination of state and tape-number exist
            both: tape, head_position will be overwritten 
            and yield returns them
        Input: initial_tape String
        Output: Tupel for Visualisation
        """
        ok=self.check_input(initial_tape)
        assert ok
        ok2=self.check_input(initial_tape2)
        assert ok2
        head_pos, head_pos2 = 0,0
        tape1 = initial_tape[:]
        tape2 = initial_tape2[:]
        shift_count = 0;
        shift_count2 = 0;
        i=0
        while True:
            shift, tape1, head_pos = self.fix_tape(tape1, head_pos)
            shift2, tape2, head_pos2 = self.fix_tape(tape2, head_pos2)
            shift_count += shift
            shift_count2 += shift2

            state_tuple = (self.state, tape1[head_pos], tape2[head_pos2])
            print("state",state_tuple, head_pos, head_pos2)
            if not state_tuple in self.table:
                break # no transition left

            #do the transition
            new_state, write, write2, direct, direct2 = self.table[state_tuple]
            new_pos = head_pos + self.translate_dir(direct)
            new_pos2 = head_pos2 + self.translate_dir(direct2)
            #print(direct, direct2, new_pos, new_pos2)
            #print(tape1, tape2)
            # this is just for compatibility with the one tape machine.
            # it would probably make more sense to provide more info here.
            # like, the second tape
            yield head_pos, write, new_state, new_pos - shift_count
            tape1[head_pos] = write
            tape2[head_pos2] = write2
            #print(tape1, tape2)
            head_pos = new_pos
            head_pos2 = new_pos2
            self.state = new_state
        pass


# Reads a TM description, returns an appropriate TM object
# description is an iterator over lines
def read_tm(description):
    header = next(description)
    #analyze header fields
    num_tapes, num_states, sigma, gamma, blank, F = header.split('|')
    if num_tapes == "1":
        return OneTapeTM(sigma, blank, description, num_tapes, num_states, gamma, F)
    elif num_tapes == "2":
        return TwoTapeTM(sigma, blank, description, num_tapes, num_states, gamma, F)
    else:
        assert False

"""
inp=["1","1","0","0","1","1","0"]
bsp=TM._parse_file("./bsp2vl.py",inp)
#bsp=TM._parse_file("./CollatzTM.py")
colli=bsp[0]
VTM=bsp[1]
slides=[]
i=0
for x in colli.exec_TM(inp): 
    if i>300:
        break
    i+=1
    print(x)
    slides.append(VTM.draw_frame(*x))
VTM.write_file(VTM.get_grunddokument(slides))
VTM.visualize()




if __name__=="__main__":
    print("one tape")
    description=iter("1|1|A,B|A,B|C|0;\nq0,B>q2,1,R".split('\n'))
    tm=read_tm(description)
    print(tm.table)
    for x in tm.exec_TM(['B']): print(x)

    print("two tape")
    description=iter("2|1|0|0|B|0;\nq0,0,B>q2,1,1,N,R".split('\n'))
    tm=read_tm(description)
    print(tm.table)
    for x in tm.exec_TM(['0']): print(x)
"""
