# Print the following pattern
# A
# A B
# A B C
# A B C D



class Pattern1:

    def pattern(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j), end=" ")
            print()
    
        


if __name__ == '__main__':
    n = 5
    pattern1 = Pattern1()
    pattern1.pattern(n)