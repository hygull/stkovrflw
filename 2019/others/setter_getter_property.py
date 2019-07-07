class A:
    def __init__(self, o):
        self.o = o


    # It should be before o.setter
    @property
    def o(self):
        return self.__o

    @o.setter
    def o(self, o):
        print("SET", o)
        self.__o = o



# class P:

#     def __init__(self,x):
#         self.x = x

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x