import matplotlib.pyplot as plt
import math

with open('../data/AddedAttributesMerged.csv', 'r') as data:
    dataList = list(data)
    headingRow = True
    lowIndex = []
    highIndex = []
    sc = []
    st = []
    scst = []
    gen = []
    
    sc_state = [[0 for i in range(0)] for j in range(31)]
    st_state = [[0 for i in range(0)] for j in range(31)]
    scst_state = [[0 for i in range(0)] for j in range(31)]
    low_index_state = [[0 for i in range(0)] for j in range(31)]
    high_index_state = [[0 for i in range(0)] for j in range(31)]
    #for row in sc_state:
        #print (row)
    
    for row in dataList:
        if headingRow:
            headingRow = False
            continue
        rowList = row.split(",")
        
        sc_val = float(rowList[11]) if rowList[11]!='NA' else 0
        st_val = float(rowList[13]) if rowList[13]!='NA' else 0
        
        lowIndex.append(float(rowList[9]))
        highIndex.append(float(rowList[10]))
        sc.append(sc_val)
        st.append(st_val)
        gen.append(float(rowList[15]) if rowList[15]!='NA' else 0)
        
        
        
        state_index = int(rowList[17])
        
        sc_state[state_index].append(sc_val)
        st_state[state_index].append(st_val)
        low_index_state[state_index].append(float(rowList[9]))
        high_index_state[state_index].append(float(rowList[10]))
        scst_state[state_index].append(sc_val+st_val)
        
    a = int(len(lowIndex)/4)
    b = int(len(highIndex)/4)
   
    for i in range(31):
        print(i)
        plt.scatter(scst_state[i], low_index_state[i])
        plt.show()
        print()
        
    
    
    