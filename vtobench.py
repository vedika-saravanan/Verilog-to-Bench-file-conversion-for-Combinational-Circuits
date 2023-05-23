import os
import re
def main():
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.v'):
            invar = []
            outvar = []
            instructions =[]
            wire = []
            gate_count = []
            with open(filename) as myfile:
                for myline in myfile:
                    if myline.startswith('input'):
                        str = myline[6:][:-1][:-1]
                        invar = list(str.split(", "))
                        invar = ["INPUT"+" "+"("+suit+")"+"\n" for suit in invar] 
                    if myline.startswith('output'):
                        str = myline[7:][:-1][:-1]
                        outvar = list(str.split(", "))
                        outvar = ["OUTPUT"+" "+"("+suit+")"+"\n" for suit in outvar]
                    if myline.startswith('wire'):
                        str = myline[4:][:-1][:-1]
                        wire = list(str.split(", "))
                        wire = ["OUTPUT"+" "+"("+suit+")"+"\n" for suit in wire]
                    if myline.startswith('AND') or myline.startswith('and') or myline.startswith('and2s1') or myline.startswith('and2s2') or myline.startswith('and2s3') or myline.startswith('and3s1') or myline.startswith('and3s2') or myline.startswith('and3s3') or myline.startswith('and4s1') or myline.startswith('and4s2')or myline.startswith('and4s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1] 
                        out_gate = str2.split(",")[0] 
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        instructions.append(out_gate+" "+"="+" "+"AND"+"("+gates_in.rstrip()+")"+"\n")
                        
                    if myline.startswith('NAND') or myline.startswith('nand') or myline.startswith('nnd2s1') or myline.startswith('nnd2s2') or myline.startswith('nnd2s3') or myline.startswith('nnd3s1') or myline.startswith('nnd3s2') or myline.startswith('nnd3s3') or myline.startswith('nnd4s1') or myline.startswith('nnd4s2') or myline.startswith('nnd4s3') or myline.startswith('nnd5s3') or myline.startswith('nnd6s3') or myline.startswith('nnd7s3') or myline.startswith('nnd8s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        # print(type(gates_in))
                        
                        instructions.append(out_gate+" "+"="+" "+"NAND"+"("+gates_in.rstrip()+")"+"\n")
                        # import pdb;pdb.set_trace()
                    if myline.startswith('OR') or myline.startswith('or') or myline.startswith('or2s1') or myline.startswith('or2s2')  or myline.startswith('or2s3')  or myline.startswith('or3s1')  or myline.startswith('or3s2')  or myline.startswith('or3s3')  or myline.startswith('or4s1')  or myline.startswith('or4s2')  or myline.startswith('or4s3')  or myline.startswith('or5s1')  or myline.startswith('or5s2')  or myline.startswith('or5s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        
                        instructions.append(out_gate+" "+"="+" "+"OR"+"("+gates_in.rstrip()+")"+"\n")
                    if myline.startswith('NOR') or myline.startswith('nor') or myline.startswith('nor2s1') or myline.startswith('nor2s2') or myline.startswith('nor2s3') or myline.startswith('nor3s1') or myline.startswith('nor3s2') or myline.startswith('nor3s3') or myline.startswith('nor4s1') or myline.startswith('nor4s2') or myline.startswith('nor4s3') or myline.startswith('nor5s1') or myline.startswith('nor5s2')or myline.startswith('nor5s3')or myline.startswith('nor6s1')or myline.startswith('nor6s2')or myline.startswith('nor6s3')or myline.startswith('nor7s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        
                        instructions.append(out_gate+" "+"="+" "+"NOR"+"("+gates_in.rstrip()+")"+"\n")
                    if myline.startswith('BUFF') or myline.startswith('buff') or myline.startswith('hnb1s1') or myline.startswith('nb1s1') or myline.startswith('nb1s10') or myline.startswith('nb1s11') or myline.startswith('nb1s12') or myline.startswith('nb1s2') or myline.startswith('nb1s3') or myline.startswith('nb1s4') or myline.startswith('nb1s5') or myline.startswith('nb1s6') or myline.startswith('nb1s7') or myline.startswith('nb1s8') or myline.startswith('nb1s9') :
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        instructions.append(out_gate+" "+"="+" "+"BUFF"+"("+gates_in.rstrip()+")"+"\n")
                    if myline.startswith('NOT') or myline.startswith('not') or myline.startswith('hi1s1') or myline.startswith('hib1s1') or myline.startswith('i1s1') or myline.startswith('i1s10') or myline.startswith('i1s11') or myline.startswith('i1s12') or myline.startswith('i1s2') or myline.startswith('i1s3') or myline.startswith('i1s4') or myline.startswith('i1s5') or myline.startswith('i1s6') or myline.startswith('i1s7') or myline.startswith('i1s8') or myline.startswith('i1s9') or myline.startswith('ib1s1') or myline.startswith('ib1s10') or myline.startswith('ib1s11') or myline.startswith('ib1s12') or myline.startswith('ib1s2') or myline.startswith('ib1s3') or myline.startswith('ib1s4') or myline.startswith('ib1s5') or myline.startswith('ib1s6') or myline.startswith('ib1s7') or myline.startswith('ib1s8') or myline.startswith('ib1s9'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        
                        instructions.append(out_gate+" "+"="+" "+"NOT"+"("+gates_in.rstrip()+")"+"\n")
                    if myline.startswith('XOR') or myline.startswith('xor')  or myline.startswith('xor2s1') or myline.startswith('xor2s2') or myline.startswith('xor2s3')  or myline.startswith('xor3s1') or myline.startswith('xor3s2') or myline.startswith('xor3s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        print(type(gates_in))
                        
                        instructions.append(out_gate+" "+"="+" "+"XOR"+"("+gates_in.rstrip()+")"+"\n")
                        
                    if myline.startswith('XNOR') or myline.startswith('xnor') or myline.startswith('xnr2s1') or myline.startswith('xnr2s2') or myline.startswith('xnr2s3') or myline.startswith('xnr3s1') or myline.startswith('xnr3s2') or myline.startswith('xnr3s3'):
                        myline = myline[:-1][:-1]
                        str1 = myline.split("(")[0].split(" ")[0]
                        str2 = myline.split("(")[1][:-1]
                        out_gate = str2.split(",")[0]
                        gates_in = str2.split(",")[1:]
                        gates_in = ','.join(gates_in)
                        print(type(gates_in))
                        
                        instructions.append(out_gate+" "+"="+" "+"XNOR"+"("+gates_in.rstrip()+")"+"\n")
            FileWrite(filename,invar,outvar,instructions)

def FileWrite(filename, invar, outvar, instructions):

    inputs =''
    outputs=''

    ins=''


  
    for out in outvar:
        outputs = outputs+out

    for inp in invar:
        inputs = inputs+inp
    for inst in instructions:
        ins = ins+inst
        # import pdb;pdb.set_trace()
        
    
    
    vname = filename.split(".")[0] + ".bench"
    fff= open(vname,"w+")

    fff.write("#"+" "+filename.split(".")[0])
    fff.write('\n')
    fff.write('\n')
    fff.write(inputs)
    fff.write('\n')
    fff.write(outputs)
    fff.write('\n')
    fff.write(ins)
    fff.close()
    print("converted "+filename+" to "+vname)

if __name__=="__main__":
    main()
