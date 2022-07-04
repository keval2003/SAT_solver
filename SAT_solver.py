from copy import deepcopy
from numpy import empty

model = set()
model_wrong = set()


def solve(cnf, literals):
    # print('\nCNF = ', end='')
    # print(cnf)
    
    new_true = []
    new_false = []
    global model, model_wrong
    model = set(model)
    model_wrong = set(model_wrong)
    
    units=[]
    for clause in cnf:
        if(len(clause)==1):
            units.append(clause[0])
    
   
    # print("Units to check",units)
    if(len(units)>=2):
        # print(len(units))
        i=0
        j=1
        while True:
            
            # print(i,j)
            # print(units[i],units[j])
            # print(len(units))
            if(units[i]=="-"+units[j] or units[j]=="-"+units[i]):
                return False
            if units[i]==units[j]:
                units.remove(units[i])
                j=j-1
                i=i-1
            i=i+1
            j=j+1
            if i>len(units)-2 or j>len(units)-1:
                break
                    
        
                    


    # print("CNF",cnf)
    
   
    if len(units):
        for unit in units:
            if '-' in unit:
                    model_wrong.add(int(unit))
                    # print(model_wrong)
                    new_false.append(int(unit))
                    i = 0
                    while True:
                        if not cnf[i]:
                            # print("CNF",cnf)
                            return False
                        if(cnf[i]==None):
                            # print("CNF",cnf)
                            return False
                        
                        if unit in cnf[i]:
                            cnf.remove(cnf[i])
                            i -= 1
                        elif str(abs(int(unit))) in cnf[i]:
                            # print("hahahhhhh",unit[-1])
                            cnf[i].remove(str(abs(int(unit))))
                        i += 1
                        # print("cnf",cnf)
                        if i >= len(cnf):
                            break
            else:
                    model.add(unit)
                    new_true.append(unit)
                    i = 0
                    while True:
                        if not cnf:
                            # print("CNF",cnf)
                            return False
                        if(cnf[i]==None):
                            # print("CNF",cnf)
                            return False
                        
                        if '-'+unit in cnf[i]:
                            cnf[i].remove('-'+unit)
                            
                            if "  " in cnf[i]:
                                cnf[i] = cnf[i].replace("  ",)
                        elif unit in cnf[i]:
                            cnf.remove(cnf[i])
                            i -= 1
                        i += 1
                        if i >= len(cnf):
                            break
    # print('Units =', units)
    # print("CNF=",cnf)
    
    

    if not cnf:
        return True
    
    for clause in cnf :
        if clause==None:
            # print("CNF",cnf)
            for i in new_true:
                model.remove(i)
            for i in new_false:
                model_wrong.remove(i)
            # print('Null clause found, backtracking...')
            return False
    temp=[]
    for clause in cnf:
        for k in clause:
            if k!='' and k!=' ' and k!="-":
                if  abs(int(k)) in temp:
                    1

                else:
                    temp.append(abs(int(k)))

    literals=deepcopy(temp)
    # print(cnf)

    # print("UNIT=",units)
    
    # print(literals)
    if not literals:
        return True
    x = literals[0]
    if solve(deepcopy(cnf)+[[str(x)]], deepcopy(literals)):
        return True
    elif solve(deepcopy(cnf)+[['-'+str(x)]], deepcopy(literals)):
        return True
    else:
        # print("not solved at" + str(x) +'\n')
        for i in new_true:
            if i in model:
                model.remove(i)
        for i in new_false:
            if i in model_wrong:
                model_wrong.remove(i)
        return False


def SAT_solver():
    global model, model_wrong
    max_literal=int(input("total literas are=="))
    f=input("file_name is==")
    test_data=open(f)
    cnf = []
    for line in test_data:
        line=line.strip()
        temp = []
        if len(line)==0:
            continue
   
        if (line[0].isdigit()) or (line[0].startswith("-")):
            line = line.split()
            for lit in line:
                if(lit!='0'):
                    temp.append(lit)
    
        cnf.append(temp)
    
    # remove all empty clauses
    lol=len(cnf)-1
    while(lol>=0):
        if(len(cnf[lol])==0):
            cnf.remove(cnf[lol])
        lol=lol-1
    
    for clause in cnf:
        if(len(clause)>=2):
            for i in range(len(clause)-1):
                for j in range(i+1,len(clause)):
                    if(clause[i]=="-"+clause[j] or clause[j]=="-"+clause[i]):
                        print("UNSATISFIABLE")
                        return 
                    if clause[i]==clause[j]:
                        clause.remove(clause[j])

    literals = [i for i in range(1,max_literal+1)]
    if solve(cnf,literals):
        print('\nResult: SATISFIABLE')
        print('Solution:')
        for i in range(1,max_literal+1):
            if -i in model_wrong:
                print(-i)
            elif i in model:
                print(i)
            else:
                print(i)

    

    else:
      print('UNSATISFIABLE')
    print()


SAT_solver()
