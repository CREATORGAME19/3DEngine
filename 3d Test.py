from tkinter import *
import math
global canvas
root = Tk()
height = 600
width = 600
def onKeyPress(event):
    global x,y,z,objects,coords,xrotation,yrotation,zrotation
    print(event.keysym)
    if (event.keysym) == "Up":
        z+=1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "Down":
        z = z-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "Right":
        x = x-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "Left":
        x += 1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.char) == " ":
        y+=1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "w":
        y+=1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "s":
        y = y-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "a":
        yrotation = yrotation - 10
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
    elif (event.keysym) == "d":
        yrotation += 10
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
x = 0
y = 0
z = 0
xrotation = 0 # From centre
yrotation = 0
zrotation = 0
coords = [[0,0,1],[0,1,1],[1,0,1],[1,1,1],[0,0,2],[0,1,2],[1,0,2],[1,1,2],[0,0,-1],[0,1,-1],[1,0,-1],[1,1,-1],[0,1,-1],[0,1,-1],[1,0,-1],[1,1,-1]] # [x,y,z]
objects = [[[0,1],[0,2],[1,3],[2,3],[0,4],[1,5],[2,6],[3,7],[4,5],[4,6],[6,7],[5,7]],[]]
root.bind('<KeyPress>', onKeyPress)
def matrix_multiply(a,b):
    new_matrix = []
    for t in range(len(b)):
        new_row = []
        for i in range(len(a[0])):
            sum = 0
            for n in range(len(a)):
                sum = sum+((a[n][i])*b[t][n])
            new_row.append(sum)
        new_matrix.append(new_row)
    return new_matrix
        
            
def Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height): #Updates canvas
    canvas.delete("all")
    newvertices = []
    for i in range(len(coords)):
        change_matrix = [[((coords[i])[0]-x)],[((coords[i])[1]-y)],[((coords[i])[2]-z)]]
        x_matrix = [[1,0,0],[0,math.cos(math.radians(xrotation)),math.sin(math.radians(xrotation))],[0, -1*math.sin(math.radians(xrotation)),math.cos(math.radians(xrotation))]]
        y_matrix = [[math.cos(math.radians(yrotation)),0,(-1*math.sin(math.radians(yrotation)))],[0,1,0],[math.sin(math.radians(yrotation)),0,math.cos(math.radians(yrotation))]]
        z_matrix = [[math.cos(math.radians(zrotation)),math.sin(math.radians(zrotation)),0],[(-1*math.sin(math.radians(zrotation))),math.cos(math.radians(zrotation)),0],[0,0,1]]
        m1 = matrix_multiply(change_matrix,x_matrix)
        m2 = matrix_multiply(m1,y_matrix)
        m3 = matrix_multiply(m2,z_matrix)
        if (m3[2])[0] != 0:
            x1 = ((m3[0])[0]*width)/(m3[2])[0]
            y1 = ((m3[1])[0]*height)/(m3[2])[0]
            """
            x1 = (((coords[i])[0]-x)/((coords[i])[2]-z))
            y1 = (((coords[i])[1]-y)/((coords[i])[2]-z))
            """
            l = [x1,y1,i]
            newvertices.append(l)

    for i in range(len(newvertices)):
        fx  = (newvertices[i])[0]+2
        fy  = (newvertices[i])[1]+2
        sx  = (newvertices[i])[0]-2
        sy  = (newvertices[i])[1]-2
        canvas.create_oval((fx,fy,sx,sy),fill = "black")
    if len(newvertices) > 0:
        for i in range(len(objects)):
            for n in range(len(objects[i])):
                found = False
                found2 = False
                counter = 0
                while (found == False) or (found2 == False):
                    if counter == len(newvertices):
                        found = True
                        found2 = True
                    elif newvertices[counter][2] == ((objects[i])[n])[0]:
                        x1 = (newvertices[counter][0])
                        y1 = (newvertices[counter][1])
                        found = True
                    elif newvertices[counter][2] == ((objects[i])[n])[1]:
                        x2 = (newvertices[counter][0])
                        y2 = (newvertices[counter][1])
                        found2 = True
                    counter += 1
                """
                x1 = ((newvertices[((objects[i])[n])[0]])[0])
                y1 = ((newvertices[((objects[i])[n])[0]])[1])
                x2 = ((newvertices[((objects[i])[n])[1]])[0])
                y2 = ((newvertices[((objects[i])[n])[1]])[1])
                """
                if counter <= (len(newvertices)):
                    canvas.create_line(x1,y1,x2,y2,fill="black")
    

canvas = Canvas(root, background="white", height = str(height), width=str(width))
canvas.pack()

Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height)
root.mainloop()
    
