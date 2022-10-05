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
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "Down":
        z = z-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "Right":
        x = x-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "Left":
        x += 1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.char) == " ":
        y+=1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "w":
        y+=1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "s":
        y = y-1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "d":
        if yrotation-1 < 0:
            yrotation = 359
        yrotation = yrotation - 1
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
    elif (event.keysym) == "a":
        yrotation += 1
        if yrotation == 360:
            yrotation = 0
        Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
x = 0
y = 0
z = 0
fov = 90
xrotation = 0 # From centre
yrotation = 0
zrotation = 0
coords = [[0,0,10],[0,10,10],[10,0,10],[10,10,10],[0,0,20],[0,10,20],[10,0,20],[10,10,20]] # [x,y,z]
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
     
            
def Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov): #Updates canvas
    canvas.delete("all")
    newvertices = []
    for i in range(len(coords)):
        change_matrix = [[((coords[i])[0]-x)],[((coords[i])[1]-y)],[((coords[i])[2]-z)]]
        x_matrix = [[1,0,0],[0,math.cos(math.radians(xrotation)),-1*math.sin(math.radians(xrotation))],[0, math.sin(math.radians(xrotation)),math.cos(math.radians(xrotation))]]
        y_matrix = [[math.cos(math.radians(yrotation)),0,(math.sin(math.radians(yrotation)))],[0,1,0],[-1*math.sin(math.radians(yrotation)),0,math.cos(math.radians(yrotation))]]
        z_matrix = [[math.cos(math.radians(zrotation)),-1*math.sin(math.radians(zrotation)),0],[(math.sin(math.radians(zrotation))),math.cos(math.radians(zrotation)),0],[0,0,1]]
        m1 = matrix_multiply(change_matrix,x_matrix)
        m2 = matrix_multiply(m1,y_matrix)
        m3 = matrix_multiply(m2,z_matrix)
        if int((m3[2])[0]) != 0:
            rendered = True
            x1 = ((m3[0])[0]*width)/(m3[2])[0]
            y1 = ((m3[1])[0]*height)/(m3[2])[0]
            if x1 < -1*(width/2) or x1 > (width/2) :
                rendered = False
            elif y1 < -1*(height/2) or y1 > (height/2):
                rendered = False
            """
            x1 = (((coords[i])[0]-x)/((coords[i])[2]-z))
            y1 = (((coords[i])[1]-y)/((coords[i])[2]-z))
            """
            yrotation1 = 360-yrotation
            if yrotation1 == 360:
                yrotation1 = 0
            if ((coords[i])[0]-x)>0 and ((coords[i])[2]-z)>0 :
                angle = math.degrees(math.atan(((coords[i])[0]-x)/((coords[i])[2]-z)))
            else:
                if ((coords[i])[0]-x)<0 and ((coords[i])[2]-z)<0:
                    angle = math.degrees(math.atan(((coords[i])[0]-x)/((coords[i])[2]-z))) + 180
                elif ((coords[i])[0]-x)>0 and ((coords[i])[2]-z)<0:
                    angle = math.degrees(math.atan(((coords[i])[2]-z)/(-1*((coords[i])[0]-x)))) + 90
                elif ((coords[i])[2]-z)>0 and ((coords[i])[0]-x)<0:
                    angle = math.degrees(math.atan((-1*((coords[i])[2]-z))/((coords[i])[0]-x))) + 270
                else:
                    if ((coords[i])[2]-z)==0 and ((coords[i])[0]-x)==0:
                        angle = -400
                    elif ((coords[i])[0]-x)==0 and ((coords[i])[2]-z)!=0:
                        if ((coords[i])[2]-z)>0:
                            angle = 0
                        else:
                            angle = 180
                    elif ((coords[i])[2]-z)==0 and ((coords[i])[0]-x)!=0:
                        if ((coords[i])[0]-x)>0:
                            angle = 90
                        else:
                            angle = 270
            highy = angle+fov
            lowy = angle-fov
            if highy >= 360:
                highy = highy-360
            if lowy < 0:
                lowy = 360+lowy
            if highy > lowy:
                if (highy > yrotation1) and (lowy <= yrotation1):
                    l = [x1,y1,i,rendered]
                    newvertices.append(l)
            else:
                if (angle>=(360-fov) and angle < 360):
                    if(highy > yrotation1) or (lowy < yrotation1):
                        l = [x1,y1,i,rendered]
                        newvertices.append(l)
                elif (angle>=0 and angle < fov):
                    if (highy > yrotation1) or (lowy < yrotation1):
                        l = [x1,y1,i,rendered]
                        newvertices.append(l)
    for i in range(len(newvertices)):
        if (newvertices[i])[3] == True:
            fx  = (newvertices[i])[0]+2
            fy  = (newvertices[i])[1]+2
            sx  = (newvertices[i])[0]-2
            sy  = (newvertices[i])[1]-2
            canvas.create_oval((fx+(width/2),fy+(height/2),sx+(width/2),sy+(height/2)),fill = "black")
    if len(newvertices) > 0:
        for i in range(len(objects)):
            for n in range(len(objects[i])):
                found = False
                found2 = False
                failed_search = False
                counter = 0
                while ((found == False) or (found2 == False)) and (failed_search == False):
                    if counter == len(newvertices):
                        failed_search = True
                    elif newvertices[counter][2] == ((objects[i])[n])[0]:
                        x1 = (newvertices[counter][0])
                        y1 = (newvertices[counter][1])
                        rendered_1 = (newvertices[counter][2])
                        found = True
                    elif newvertices[counter][2] == ((objects[i])[n])[1]:
                        x2 = (newvertices[counter][0])
                        y2 = (newvertices[counter][1])
                        rendered_2 = (newvertices[counter][2])
                        found2 = True
                    counter += 1
                """
                x1 = ((newvertices[((objects[i])[n])[0]])[0])
                y1 = ((newvertices[((objects[i])[n])[0]])[1])
                x2 = ((newvertices[((objects[i])[n])[1]])[0])
                y2 = ((newvertices[((objects[i])[n])[1]])[1])
                """
                if failed_search == False:
                    canvas.create_line(x1+(width/2),y1+(height/2),x2+(width/2),y2+(height/2),fill="black")
                else:
                    if (found == True) or (found2 == True):
                        ###CALCULATE PLANAR EQUATION
                        perpendicular_x = -(math.sin(math.radians(yrotation)))
                        perpendicular_z = (math.cos(math.radians(yrotation)))
                        result_total = (perpendicular_x*x)+(0*y)+(perpendicular_z*z)
                        coord1_x = (coords[((objects[i])[n])[0]])[0]
                        coord1_y = (coords[((objects[i])[n])[0]])[1]
                        coord1_z = (coords[((objects[i])[n])[0]])[2]
                        coord2_x = (coords[((objects[i])[n])[1]])[0]
                        coord2_y = (coords[((objects[i])[n])[1]])[1]
                        coord2_z = (coords[((objects[i])[n])[1]])[2]
                        vector_x = coord2_x-coord1_x
                        vector_y = coord2_y-coord1_y
                        vector_z = coord2_z-coord1_z
                        result_total = result_total-(perpendicular_x*coord1_x)-(perpendicular_z*coord1_z)
                        constant = result_total/((perpendicular_x*vector_x)+(perpendicular_z*vector_z))
                        if found == True:
                            constant += -0.01
                        else:
                            constant += 0.01
                        newcoord_x = (constant*vector_x)+coord1_x
                        newcoord_y = (constant*vector_y)+coord1_y
                        newcoord_z = (constant*vector_z)+coord1_z
                        change_matrix = [[(newcoord_x-x)],[(newcoord_y-y)],[(newcoord_z-z)]]
                        x_matrix = [[1,0,0],[0,math.cos(math.radians(xrotation)),-1*math.sin(math.radians(xrotation))],[0, math.sin(math.radians(xrotation)),math.cos(math.radians(xrotation))]]
                        y_matrix = [[math.cos(math.radians(yrotation)),0,(math.sin(math.radians(yrotation)))],[0,1,0],[-1*math.sin(math.radians(yrotation)),0,math.cos(math.radians(yrotation))]]
                        z_matrix = [[math.cos(math.radians(zrotation)),-1*math.sin(math.radians(zrotation)),0],[(math.sin(math.radians(zrotation))),math.cos(math.radians(zrotation)),0],[0,0,1]]
                        m1 = matrix_multiply(change_matrix,x_matrix)
                        m2 = matrix_multiply(m1,y_matrix)
                        m3 = matrix_multiply(m2,z_matrix)
                        if found == True:
                            x2 = ((m3[0])[0]*width)/(m3[2])[0]
                            y2 = ((m3[1])[0]*height)/(m3[2])[0]
                        else:
                            x1 = ((m3[0])[0]*width)/(m3[2])[0]
                            y1 = ((m3[1])[0]*height)/(m3[2])[0]
                        canvas.create_line(x1+(width/2),y1+(height/2),x2+(width/2),y2+(height/2),fill="black")
                        
                    
canvas = Canvas(root, background="white", height = str(height), width=str(width))
canvas.pack()

Update_Canvas(coords,x,y,z,canvas,objects,xrotation,yrotation,zrotation,width,height,fov)
root.mainloop()
    
