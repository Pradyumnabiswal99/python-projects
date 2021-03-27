from tkinter import *
import tkinter.filedialog
def btnConvert_Click():
    convertStringIntoHexCode(varFileSource.get(),varFileDest.get())
def btnSelectSource_Click():
    res=tkinter.filedialog.askopenfilename()
    varFileSource.set(res)
def btnSelectDest_Click():
    res=tkinter.filedialog.asksaveasfilename()
    varFileDest.set(res)
def convertStringIntoHexCode(fileSource,fileDest):
    strNew=""
    fsS=open(fileSource,'r')
    strData=fsS.read()
    for e in strData:
        code=ord(e)
        strNew+=hex(code)+" "
    fs=open(fileDest,'w')
    fs.write(strNew)
    fs.close()
root=Tk()
root.minsize(400,400)
varFileSource=StringVar()
txtFileSourceName=Entry(root,textvariable=varFileSource)
txtFileSourceName.pack(fill='x')
btnSelectSource=Button(root,text="Select Source File",command=btnSelectSource_Click)
btnSelectSource.pack(fill='x')

varFileDest=StringVar()
txtFileDestName=Entry(root,textvariable=varFileDest)
txtFileDestName.pack(fill='x')
btnSelectDest=Button(root,text="Select Dest File",command=btnSelectDest_Click)
btnSelectDest.pack(fill='x')
btnConvert=Button(root,text="Convert Into Hex",command=btnConvert_Click)
btnConvert.pack(fill='x')

root.mainloop()
