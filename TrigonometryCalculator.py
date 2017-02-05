import time
import sys
import random
import math
"""Uncomment the below for colours to work in windows, don't
know how to get them to work in Linux atm, 
maybe a feature to be implemented?"""
#VVVV Doesn't work in linux VVVV
#from subprocess import call
#call(["color","0A"], shell=True)
#call(["cls"], shell=True)
#===============================
run=True
def typing(string):
        for c in string:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.05)
        print
def spdtyping(string):
        for c in string:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.01)
        print
while run==True:
        typing("Don't forget SOH|CAH|TOA!")
        typing("TRIGONOMETRY CALCULATOR")
        angleorside=raw_input("Are you working out a side or an angle? ").lower()
        if angleorside == "side":
                typing("SIDE SELECTED")
                whichside=raw_input("Which side are you working out? [H/O/A] ").lower()
                if whichside == "h":
                        typing("H (HYPOTENUSE) SELECTED")
                        o=raw_input("What is the value of O (side opposite to angle)? [input 'empty' for unknown value] ").lower()
                        a=raw_input("What is the value of A (side adjacent to angle)? [input 'empty' for unknown value] ").lower()
                        angle=raw_input("What is the value of the angle? ")
                        if o=="empty":
                                typing("COS SELECTED")
                                a=float(a)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.cos(rangle)
                                print float(nangle)
                                typing("That is the result of cos()")
                                hyp=a/nangle
                                typing("The answer is:")
                                print hyp
                                typing("To get this we did a/cos(angle)")
                        elif a=="empty":
                                typing("SIN SELECTED")
                                o=float(o)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.sin(rangle)
                                print float(nangle)
                                typing("That is the result of sin(o)")
                                hyp=o/nangle
                                typing("The answer is:")
                                print hyp
                                typing("To get this we did a/sin(angle)")
                                again=raw_input("Would you like to do another one? [Y/N").lower()
                        if again == "y":
                                run=False
                                time.sleep(5)
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                run=True
                        else:
                                run=False
                elif whichside=="o":
                        typing("O (OPPOSITE) SELECTED")
                        h=raw_input("What is the value of H (side opposite right-angle)? [input 'empty' for unknown value] ").lower()
                        a=raw_input("What is the value of A (side adjacent to angle)? [input 'empty' for unknown value] ").lower()
                        angle=raw_input("What is the value of the angle? ")
                        if h=="empty":
                                typing("TAN SELECTED")
                                a=float(a)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.tan(rangle)
                                print float(nangle)
                                typing("That is the result of tan()")
                                opp=a/nangle
                                typing("The answer is:")
                                print opp
                                typing("To get this we did a*tan(angle)")
                        elif a=="empty":
                                typing("COS SELECTED")
                                h=float(h)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.cos(rangle)
                                print float(nangle)
                                typing("That is the result of cos(h)")
                                opp=h/nangle
                                typing("The answer is:")
                                print opp
                                typing("To get this we did h/cos(angle)")
                                again=raw_input("Would you like to do another one? [Y/N").lower()
                        if again == "y":
                                run=False
                                time.sleep(5)
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                run=True
                        else:
                                run=False
                if whichside == "a":
                        typing("A (ADJACENT) SELECTED")
                        o=raw_input("What is the value of O (side opposite to angle)? [input 'empty' for unknown value] ").lower()
                        h=raw_input("What is the value of H (side adjacent to angle)? [input 'empty' for unknown value] ").lower()
                        angle=raw_input("What is the value of the angle? ")
                        if o=="empty":
                                typing("COS SELECTED")
                                h=float(h)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.cos(rangle)
                                print float(nangle)
                                typing("That is the result of cos()")
                                adj=h*nangle
                                typing("The answer is:")
                                print adj
                                typing("To get this we did h*cos(angle)")
                        elif a=="empty":
                                typing("TAN SELECTED")
                                o=float(o)
                                angle=float(angle)
                                rangle=angle/360*(2*math.pi)
                                nangle = math.tan(rangle)
                                print float(nangle)
                                typing("That is the result of tan(o)")
                                adj=o*nangle
                                typing("The answer is:")
                                print adj
                                typing("To get this we did o*sin(angle)")
                                again=raw_input("Would you like to do another one? [Y/N").lower()
                        if again == "y":
                                run=False
                                time.sleep(5)
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                print" "
                                run=True
                        else:
                                run=False
        elif angleorside =="angle":
                o=raw_input("What is the value of o (Opposite)? [input 'empty' for unknown value ").lower()
                h=raw_input("What is the value of h (Hypotenuse)? [input 'empty' for unknown value ").lower()
                a=raw_input("What is the value of a (Adjacent)? [input 'empty' for unknown value ").lower()
                if o == "empty":
                        typing("SIN SELECTED")
                        h=float(h)
                        a=float(a)
                        h=h/360*(2*math.pi)
                        a=a/360*(2*math.pi)
                        angle = math.asin(a/h)
                        typing("The angle is:")
                        print angle
                elif h=="empty":
                        typing("TAN SELECTED")
                        o=float(o)
                        a=float(a)
                        o=o/360*(2*math.pi)
                        a=a/360*(2*math.pi)
                        angle=math.atan(o/a)
                        typing("The angle is:")
                        print angle
                elif a=="empty":
                        typing("COS SELECTED")
                        o=float(o)
                        h=float(h)
                        o=o/360*(2*math.pi)
                        h=h/360*(2*math.pi)
                        angle=math.acos(o/h)
                        typing("The angle is:")
                        print angle
                        again=raw_input("Would you like to do another one? [Y/N").lower()
                        if again == "y":
                                run=False
                        time.sleep(5)
                        print" "
                        print" "
                        print" "
                        print" "
                        print" "
                        print" "
                        run=True
                else:
                        run=False

# Created by Finlay Haggar MMXVII
