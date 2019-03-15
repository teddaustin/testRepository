"""
Initialize
    and import
"""
import sys
import csv
import os
import glob

class FileClass:

    def __init__ (self):
        name = 'nada'
        ext = 'dada'

    def is_filetype_supported(self, FileName, SupportedFiles):
        #for f in os.listdir():
        #self.name, self.ext = os.path.splitext(f)
        self.name, self.ext = os.path.splitext(FileName)
        self.ext = self.ext.lstrip('.')
        print('0:', self.name, self.ext)

        if self.ext in SupportedFiles:
            print(FileName,'supported')
            return 0
        else:
            print(FileName, self.name, self.ext,'2')
            return 1

    def find_ext_(self,root_dir):
        #find txt in directory running from. Haven't passed parameters yet
        self.path = os.getcwd()
        self.path = root_dir
        print('current directory: ', self.path)
        self.counter = 0
        self.list_ext_files = {}
        for f in os.listdir(self.path):
            if f.endswith(".txt"):
                self.list_ext_files [self.counter] = os.path.join(self.path, f)
                self.counter += 1
        if self.counter == 0:
            print('No files found')
        self.counter = 0
        for f in self.list_ext_files:
            #print(self.list_ext_files[self.counter])
            self.counter += 1

class MyDataPlot:

    def MakeArray(var1):
        ArrayL = []
        for i in range(var1): # This creates a list with index of 0 to var1-1
            ArrayL.append(i)
            return ArrayL

            def Plot2DATASets (DataSetA,DataSetB,xAxis,yAxis,xLabel,yLabel):
                plt.xlabel(xLabel)
                plt.ylabel(yLabel)
                #t = np.arange(0., 5., 0.2)
                # plt.plot(DataSetA, 'r--', DataSetB, 'b--')

                # s= defines size.  c= defines color
                # plt.scatter(DataSetA,DataSetB,s=,c='r')
                # print (plt.style.available)
                # plt.style.use('seaborn-ticks')
                # fig, ax = plt.subplots(figsize=(8, 8))
                # print(fig.canvas.get_supported_filetypes())
                # fig.savefig('myfirstplot.pdf', transparent=False, dpi=80, bbox_inches="tight")

                """
                red dashes 'r--', blue squares 'bs', green triangles'g^', red circle 'ro'

                """
                plt.plot(xAxis, DataSetA,'r--',xAxis, DataSetB, 'g--')
                #    plt.plot(DataSet1, yAxis,'ro',DataSet2, yAxis, 'g--')
                plt.show()

                """
                # Plot example for two data sets
                DataSet1 = [1,2,3,4,5,6]
                DataSet2 = [1,4,8,16,32,64]
                xAx = [0,0.1,0.2,0.3,0.4,0.5]
                yAx = [5,20,40,60,80,100]
                xL = 'X-Axis Label'
                yL = 'Y-axis Label'
                Plot2DATASets (DataSet1,DataSet2,xAx,yAx,xL,yL)
                Plot2DATASets ([0,1,2],[12,13,14],[0,0.4,0.8],[0,0.1,0.2],'fun','try')

                if len(sys.argv) < 4:
                    print('ERROR: Not enough arguments')
                    exit()
                else:
                    in1 = sys.argv[1]
                    in2 = sys.argv[2]
                    in3 = sys.argv[3]
                    in4 = sys.argv[4]
                    # you call the function by using the function name and pass a parameter
                    print('You entered:',in1,in2,in3,in4)

                    Logic:
                    find all files with name FindFile in all subriredctories
                    Store the list in a file StoreFilePaths
                    Look for an attribute FileClass in the path of each file.
                    Find those files from StoreFilePath and extract FindString from those files
                    Parse IOAttribute from those files
                    Plot them


                    All_max_ONtimes  = MakeArray(int(in1))
                    All_max_OFFtimes = MakeArray(int(in1))

                    x = 0
                    while  x < int(in1):
                        All_max_OFFtimes [x] = random.randint(int(in4),int(in3))
                        All_max_ONtimes [x] = random.randint(int(in4),int(in2))
                        x+=1
                    # print(All_max_ONtimes)
                    # print(All_max_OFFtimes)

                    for z in range(len(All_max_ONtimes)):
                        print ('Timer',z+1,' (ON=',All_max_ONtimes[z],'\tOFF=',All_max_OFFtimes[z],')')
                        hon, mon = tConvert(All_max_ONtimes[z],'m')
                        hoff, moff  = tConvert(All_max_OFFtimes[z],'m')
                        print ('Timer',z+1,' (ON=',"%d:%02d" % (hon, mon),'\tOFF=', "%d:%02d)\n" % (hoff, moff))
                """
