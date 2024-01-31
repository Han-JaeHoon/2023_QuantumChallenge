import pennylane as qml
import numpy as np

# quantum coin 
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def Q_coin_1():
    qml.Hadamard(0)
    return qml.expval(qml.PauliZ(0))


# Hadamard gate transform qubit 0 into Hafamard state which is distributied 0, 1 
print(Q_coin_1())
# Q_coin_1's output is 0 
# PauliZ's eigenvalue is 1 or -1 so that  qml.expval(qml.PauliZ(0)) means 0 and 1 state is equally distributed 

dev = qml.device("default.qubit", wires=1)


# 4 side Q-coin 
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def Q_coin_2():
    qml.Hadamard(0)
    qml.Hadamard(1)
    return qml.probs()


# print(Q_coin_2())



# task 2 

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def Q_coin_2(num):
    bits = [int(x) for x in np.binary_repr(num, width=4)]
    qml.BasisStatePreparation(bits, wires=[0,1,2,3])
    return qml.probs()

# print(Q_coin_2(10))
# output ( num = 10 )
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.], 1의 index : 10


# task 3
dev = qml.device("default.qubit", wires=6)


@qml.qnode(dev)
def shift():
    # 주사위 (4,5)
    qml.Hadamard(4)
    qml.Hadamard(5)
    
    # 논리 회로들 (0,1,2,3)
    # 1칸
    qml.CNOT([5,3])
    qml.MultiControlledX([3,5],[2],'01')
    qml.MultiControlledX([2,3,5],[1],'001')
    qml.MultiControlledX([1,2,3,5],[0],'0001')

    qml.CNOT([4,2])
    qml.MultiControlledX([2,4],[1],'01')
    qml.MultiControlledX([1,2,4],[0],'001')
    return qml.probs([0,1,2,3])

# one_roll = shift()
# print(shift())


@qml.qnode(dev)
def shift_n(num):
   
        

    for i in range(num):
        qml.Hadamard(4)
        qml.Hadamard(5)

        qml.CNOT([5,3])
        qml.MultiControlledX([3,5],[2],'01')
        qml.MultiControlledX([2,3,5],[1],'001')
        qml.MultiControlledX([1,2,3,5],[0],'0001')

        qml.CNOT([4,2])
        qml.MultiControlledX([2,4],[1],'01')
        qml.MultiControlledX([1,2,4],[0],'001')

    
    return qml.state()


# 위치를 나타내는 4개의 큐비트
# 주사위를 굴리는 추가적인 큐비트 
# 주사위를 돌리고나서 위치 상태 반환 및 주사위 상태 초기화 후 다시 돌리기 



# Task 4
import numpy as np

aa = np.eye(16)
aa[2][2]=0; aa[9][9]=0; aa[8][8]=0; aa[12][12]=0
aa[2][9]=1; aa[9][2]=1; aa[8][12]=1; aa[12][8]=1

@qml.qnode(dev)
def shift_n_T4(num):


    for i in range(num):
        qml.Hadamard(4)
        qml.Hadamard(5)

        qml.CNOT([5,3])
        qml.MultiControlledX([3,5],[2],'01')
        qml.MultiControlledX([2,3,5],[1],'001')
        qml.MultiControlledX([1,2,3,5],[0],'0001')

        qml.CNOT([4,2])
        qml.MultiControlledX([2,4],[1],'01')
        qml.MultiControlledX([1,2,4],[0],'001')
        
        # 사다리
        qml.QubitUnitary(aa,[0,1,2,3])

    return qml.probs([0,1,2,3])





import matplotlib.pyplot as plt

def print_bar(result):
    bits_num = int(np.log2(len(result)))
    bits_list= [i for i in range(1,17)]
    x = np.arange(len(result))

    plt.figure(figsize=(10, 5))
    plt.bar(x, result,width=0.8)
    plt.xticks(x, bits_list) 
    plt.xlabel('place', fontsize=10)
    plt.ylabel('Probability', fontsize=10)
    



@qml.qnode(dev)
def shift_n_T4(num):  

    for i in range(num):
        qml.Hadamard(4)
        qml.Hadamard(5)

        qml.CNOT([5,3])
        qml.MultiControlledX([3,5],[2],'01')
        qml.MultiControlledX([2,3,5],[1],'001')
        qml.MultiControlledX([1,2,3,5],[0],'0001')

        qml.CNOT([4,2])
        qml.MultiControlledX([2,4],[1],'01')
        qml.MultiControlledX([1,2,4],[0],'001')
        
        
        # 사다리
        qml.QubitUnitary(aa,[0,1,2,3])

    return qml.probs([0,1,2,3])

# x =shift_n_T4(5)
# print(x)


# print(n_roll)
n_roll = shift_n(7)
print(n_roll)
print(len(n_roll))
# print_bar(n_roll)
# n_roll = shift_n(4)
# print_bar(n_roll)
# n_roll = shift_n(5)
# print_bar(n_roll)
# print_bar(one_roll)
# print_bar(x)
# plt.show()
# qml.draw_mpl(shift_n_T4, show_all_wires = True)(2)
plt.show()