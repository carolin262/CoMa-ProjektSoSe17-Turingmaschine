import visual

class TM(object):
    def __init__(self, input_alphabet, blank, description):
        self.blank = blank
        self.state = 'q0'
        head_pos = 0
        self.input_alphabet = input_alphabet.split(',')
        self.table = { tuple(x.strip().split(',')) : y.strip().split(',') for x,y in (l.split('>') for l in description) }

    def exec_TM(inputstring):
        pass # overwritten

    def check_input(self, tape):
        print('blank',self.blank, 'alphabet',self.input_alphabet)
        return all((i == self.blank or i in self.input_alphabet for i in tape))

    def fix_tape(self, tape, head_pos):
        # did we leave the tape to the left?
        if head_pos < 0:
            return 1, [self.blank] + tape, 0
        # did we leave the tape to the right?
        if head_pos >= len(tape):
            return 0, tape + [self.blank], head_pos
        return 0, tape, head_pos

    def translate_dir(self, direction):
        if direction == "R": return 1
        if direction == "L": return -1
        return 0 # N or other letters

    @staticmethod
    def _parse_file(path,tape):
        with open(path, 'r') as f:
            return read_tm(iter(f.readlines()),tape)

class OneTapeTM(TM):
    def __init__(self, blank,description, F): #ToDo umbennenen
        self.slides=[] 
        TM.__init__(self, blank, description, F)

    def exec_TM(self, initial_tape):
        assert self.check_input(initial_tape)
        head_pos = 0
        tape = initial_tape[:]
        shift_count = 0;
        while True:
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
            print(["B"]*(3-shift_count)+tape)

class TwoTapeTM(TM):
    def __init__(self, blank, F, description):
        TM.__init__(self, blank, F, description)
        head_pos2 = 0

    def exec_TM(self, initial_tape, initial_tape2=[]):
        assert self.check_input(initial_tape)
        assert self.check_input(initial_tape2)
        head_pos, head2_pos = 0,0
        tape1 = initial_tape[:]
        tape2 = initial_tape2[:]
        shift_count = 0;
        shift_count2 = 0;
        while True:
            shift, tape1, head_pos = self.fix_tape(tape1, head_pos)
            shift2, tape2, head_pos2 = self.fix_tape(tape2, head_pos)
            shift_count += shift
            shift_count2 += shift2

            state_tuple = (self.state, tape1[head_pos], tape2[head_pos2])
            print(state_tuple)
            if not state_tuple in self.table:
                break # no transition left

            #do the transition
            new_state, write, write2, direct, direct2 = self.table[state_tuple]
            new_pos = head_pos + self.translate_dir(direct)
            new_pos2 = head_pos2 + self.translate_dir(direct2)
            
            # this is just for compatibility with the one tape machine.
            # it would probably make more sense to provide more info here.
            # like, the second tape
            yield head_pos, write, new_state, new_pos - shift_count

            tape1[head_pos] = write
            tape2[head_pos2] = write2
            head_pos = new_pos
            head_pos2 = new_pos2
            self.state = new_state
        pass


# Reads a TM description, returns an appropriate TM object
# description is an iterator over lines
def read_tm(description,tape):
    header = next(description)
    #analyze header fields
    print(header.split('|'))
    num_tapes, num_states, sigma, gamma, blank, F = header.split('|')
    if num_tapes == "1":
        VTM=visual.VisualTM(tape,sigma,gamma,num_states,F,blank)
        return OneTapeTM(sigma, blank, description),VTM
    elif num_tapes == "2":
        return TwoTapeTM(sigma, blank, description),0
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
