class Patterns:

    # Print the following pattern
    # A
    # A B
    # A B C
    # A B C D
    def pattern1(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j), end=" ")
            print()

    # Print the following pattern
    # A B C D
    # A B C
    # A B
    # A
    def pattern2(self, n):
        for i in range(n):
            for j in range(n-i):
                print(chr(65+j), end="")
            print()

    # A
    # BB
    # CCC
    # DDDD
    def pattern3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i), end="")
            print()

    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    def pattern4(self, n):
        for i in range(n*2):
            if i < n:
                # First part of stars
                for j in range(n-i):
                    print("*", end="")
                # Spaces in between
                for j in range(i*2):
                    print(" ", end="")
                # Last part of stars
                for j in range(n-i):
                    print("*", end="")
            else:
                # First part of stars
                for j in range((i%n)+1):
                    print("*", end="")
                # Spaces in between
                for j in range((2*n-i-1)*2):
                    print(" ", end="")
                # Last part of stars
                for j in range((i%n)+1):
                    print("*", end="")
            print()

    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
    def pattern5(self, n):
        for i in range(2*n-1):
            if i<n:
                # First set of stars
                for j in range(i+1):
                    print("*", end="")
                # Spaces
                for j in range(2*(n-i-1)):
                    print(" ", end="")
                # Next set of stars
                for j in range(i+1):
                    print("*", end="")
            else:
                # First set of stars
                for j in range(n-((i+1)%n)):
                    print("*", end="")
                # Spaces
                for j in range(2*((i+1)%n)):
                    print(" ", end="")
                # Next set of stars
                for j in range(n-((i+1)%n)):
                    print("*", end="")
            print()

    # *****
    # *   *
    # *   *
    # *   *
    # *****
    def pattern6(self, n):
        for i in range(n):
            if i==0 or i==n-1:
                for j in range(n):
                    print("*", end="")
            else:
                for j in range(n):
                    if j==0 or j==n-1:
                        print("*", end="")
                    else:
                        print(" ", end="")
            print()

    # 5 5 5 5 5 5 5 5 5 
    # 5 4 4 4 4 4 4 4 5 
    # 5 4 3 3 3 3 3 4 5 
    # 5 4 3 2 2 2 3 4 5 
    # 5 4 3 2 1 2 3 4 5 
    # 5 4 3 2 2 2 3 4 5 
    # 5 4 3 3 3 3 3 4 5 
    # 5 4 4 4 4 4 4 4 5 
    # 5 5 5 5 5 5 5 5 5
    def pattern7(self, n):
        for i in range(2*n-1):
            to_print = n
            if i<n:
                for j in range(2*n-1):
                    if j<i:
                        print(to_print, end=" ")
                        to_print -= 1
                    elif j>=i and j<2*n-1-i:
                        print(to_print, end=" ")
                    else:
                        to_print += 1
                        print(to_print, end=" ")
            else:
                for j in range(2*n-1):
                    if j<2*n-1-i:
                        print(to_print, end=" ")
                        to_print -= 1
                    elif j>=2*n-1-i and j<i+1:
                        print(to_print, end=" ")
                    else:
                        to_print += 1
                        print(to_print, end=" ")
            print()                    


if __name__ == '__main__':
    n = 5
    patterns = Patterns()
    patterns.pattern7(n)