# Define a class with a generator which can iterate the numbers, which are divisible
# by 7, between a given range 0 and n.
class Generator:
    def __init__(self):
        self.generator =[]

    def iterate(self,n):
        for i in range(n+1):
            if i%7==0:
                self.generator.append(i)
        return self.generator

def main():
    a=int(input("Enter a range: "))
    b=Generator()
    c=b.iterate(a)
    print("Numbers divisible by 7 between 0 and",a,"is:",c)

if __name__ == "__main__":
    main()