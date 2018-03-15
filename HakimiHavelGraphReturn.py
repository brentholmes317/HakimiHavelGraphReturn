from sys import exit

def convert_integer(s):
  try:
      return int(s)
  except ValueError:
      return None

def HakimiHavelGraphReturn(sequence):

    words = sequence.split()

    #a variable that indicates the splitting by spaces failed.  We will use this
    #to see if splitting by commas also fails at which point we give up
    strike = 0

    #checks if splitting by spaces worked if not we assign a strike
    for word in words:
        if(convert_integer(word) == None):
            strike = 1

    if strike == 1:
        words = sequence.split(',')

        #checks if splitting by commas works.  Either will do but we demand consistency
        for word in words:
            if(convert_integer(word) == None):
                print("Your input is improperly formatted.")
                return False

    #our entry is all integers if we are still around at this point

    int_seq =  []
    #counts vertices in the graph
    counter = 1
    for word in words:
        int_seq.append((convert_integer(word),counter))
        counter = counter + 1

    #checks for negative numbers
    for word in int_seq:
        if(word[0] < 0):
            print("You gave me a negative number.")
            return False

    if(sum(int_seq[0]) % 2 == 1):
        print("Your sequence sums to an odd value and is therefore not graphical.")
        return False

    #At ths point we have either terminated the program or
    #we have an acceptable sequence that does not sum to an odd number

    #we sort our sequence largest to smallest
    int_seq = sorted(int_seq, key=lambda x: x[0], reverse=True)
    length = int_seq.__len__()
    #we create a matrix to keep track of our edges.
    answer_matrix = [[0 for x in range(length)] for y in range(length)]

    #now we run the actual HH algorithm
    for i in range(0, length):
        #we check if we have enough vertices left to attain our desired degree
        if int_seq[i][0] > length-(i+1):
            print("This sequence is not graphical.")
            return False
        else:
            for j in range(0, int_seq[i][0]):
                #this checks to make sure we don't subtract down to a negative
                if int_seq[j+i+1][0] > 0:
                    int_seq[j+i+1] = (int_seq[j+i+1][0]-1,int_seq[j+i+1][1])
                    #and we need to add an edge to our answer_matrix
                    #we need an edge between int_seq[i][1] and int_seq[i+j+1][1]
                    answer_matrix[int_seq[i][1]-1][int_seq[i+j+1][1]-1] = 1
                    answer_matrix[int_seq[i+j+1][1]-1][int_seq[i][1]-1] = 1
                else:
                    print("This sequence is not graphical.")
                    return False
            int_seq = sorted(int_seq, key=lambda x: x[0], reverse=True)
    #If we are still running at this point, then the sequence must be graphical
    print("This sequence is graphical.")
    print(answer_matrix)
    return answer_matrix

print("Please input a sequence of non-negative integers")
source = input("> ")
HakimiHavelGraphReturn(source)
