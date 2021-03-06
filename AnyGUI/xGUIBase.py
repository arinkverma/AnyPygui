#xGUIBase.py
#Generic base class
#Author: ArinkVerma

''' WX_Canvas : On it widget can be added '''
class Canvas(object):
    def __init__(self, id, title,width,height):pass
    def show(self):pass
    def add(self,widget):pass
            

''' WIDGETS: Button '''
class Button(object):
    def __init__(self,title,X,Y,width,height):pass    
    def clickListener(self,method):pass

class TextArea(object):
    def __init__(self,title,X,Y,width,height):pass
    def setText(self,text):pass
    def appendText(self,text):pass
    def clear(self):pass


class CheckBox(object):
    def __init__(self,title,X,Y,width,height):pass
    def setValue(self,value):pass
    def getValue(self):pass


class RadioGroup(object):
    def __init__(self,width,height):pass
    def addRadioButton(self,label,X,Y):pass
    def getValue(self):pass
    def setButtonTrue(self,pos):pass

class ValueList(object):
    def __init__(self,choices,X,Y,width,height,value=""):pass
    def getValue(self):pass

