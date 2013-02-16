
import gtk


class Canvas:
    def __init__(self, id, title,width,height):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        # Create a Fixed Container
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):
        self.window.show()
        gtk.main()
        return

    def add(self,widget):
        widget_type = type(widget)  
        print widget_type     
        if(widget_type==Button):
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextArea):
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)

        elif(widget_type==CheckBox):
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            widget.controller.set_active(widget.value)
            
        elif(widget_type==RadioGroup):
            widget.controller = []
            radio_controller = gtk.RadioButton(None, widget.labels[0])
            radio_controller.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_controller,widget.position_X[0], widget.position_Y[0])
            radio_controller.show()
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[i])
                radio_controller.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_controller,widget.position_X[i], widget.position_Y[i])
                radio_controller.show()
                widget.controller.append(radio_controller)
            
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].set_active(True)
            
        elif(widget_type==ValueList):
            widget.controller = gtk.OptionMenu()
            widget.controller.set_size_request(widget.width,widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
                print "gis"
            widget.controller.set_menu(menu)
            widget.controller.show()
            self.fixed.put(widget.controller,widget.position_X, widget.position_Y)
            

class Button(gtk.Button):
    controller = None
    callbackMethod = None
    def __init__(self,text,X,Y,width,height):
        self.text = text
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def clickListener(self,method):
        if(self.controller == None):
            self.callbackMethod = method
        else:
            self.controller.connect("clicked", method)
        return True
    
class TextArea(gtk.TextView):
    controller = None
    callbackMethod = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        self.buffer.set_text(text)
        return True

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True


class CheckBox(gtk.CheckButton):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def setValue(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.controller == None):
            self.value = value
        else:
            self.controller.set_active(value)

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.get_active()


class RadioGroup(gtk.RadioButton):
    GroupController = None
    controller = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[i].get_active()):
                return self.labels[i]
        return "None"

    def setButtonTrue(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)

class ValueList(gtk.OptionMenu):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.title = ""
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value
        temp = [value]
        for i in range(len(choices)):
            temp.append(choices[i])
        self.choices = temp

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            IntValue = self.controller.get_history()
            if(IntValue < 0):
                return None
            return self.choices[IntValue]

''' ----------------------------------------------------------------
        This is just demo! 
        IT IS NOT THE PART OF LIB '''
       
class API:
    '''
    Initialize the object using following parameters
    API ( title ="" , height=500, width=500)
    
    
    '''
    def __init__(self,title="", height=500, width=500):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        self.window.show()
       
    def createLabel(self,name="Label"):
        label = gtk.Label(name)
        label.show()
        return label
    
    def createButton(self, name="Button"):
        button = gtk.Button(name)
        button.show()
        return button
    
    def createCheckButton(self, name="CheckButton"):
        checkButton = gtk.CheckButton(name)
        checkButton.show()
        return checkButton
    
    def createRadioButton(self, nameList, widget , func = None):
        ''' 
        Create RadioButton will take as argument a list containing names
        of the radioButton and a widget to which these radio buttons should 
        be attached
        
        createRadioButton( ListOfNames, WidgetToAddButtonsTo, FunctionToCallWhenToggled = None)
        '''
        count = 0
        for a in nameList:
            if(count == 0):
                radioButton = gtk.RadioButton(None, a)
            else:
                radioButton = gtk.RadioButton(radioButton, a)
            widget.add(radioButton)
            radioButton.show()
            count = count + 1
            
    def createBox(self, Vertical = True):
        '''
        When Vertical is set to true, this function will return Vertical Box
        in which widgets are added vertically.
        When set to False, Horizontal Box will be return in which widgets are
        added Horizontally
        '''
        if(Vertical):
            box = gtk.VBox(False,2)
        else:
            box = gtk.HBox(False,2)
        box.show()
        return box
    
    def createTextBox(self, CharLimit = 0):
        textBox = gtk.Entry(CharLimit)
        textBox.show()
        return textBox
        
    def createDropDownList(self, ListNames):
        opt = gtk.OptionMenu()
        menu = gtk.Menu()
        
        for name in ListNames:
            item = gtk.MenuItem(name)
            item.show()
            menu.append(item)
        opt.set_menu(menu)
        opt.show()
        return opt
   


        
    

if __name__ == '__main__':

    #Functions bind to button events
    def SubmitButtonClick(event):
        report = " Your city is "+valuelist.getValue()+"\n"
        if(checkbox1.getValue()):
            report = report + " you have read the code\n"
        else:
            report = report + " you have not read the code\n"

        if(checkbox2.getValue()):
            report = report + " you have read the documentation\n"
        else:
            report = report + " you have not read the documentation\n"

        report = report + " you are "+rb1.getValue()+"\n"
        report = report + " you need "+rb2.getValue()+"\n"

        textarea.appendText("_______________________\n"+report+"\n\n")
        return True 

    def AboutButtonClick(event):
        textarea.setText("Created by wxGUI -v1.0\nAuthor : Arink Verma\n\nhttp://10.1.0.140/trac/wiki/ArinkVerma\n")
        return True



    #Constructor canvas
    canvas = Canvas(1, 'wxGUI -v1.0 | ArinkVerma' ,510,300)

    #Dropdown valuelist
    cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
    valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
    canvas.add(valuelist)

    #checkboxs
    checkbox1 = CheckBox("I have read the code.",10,45,215,15)
    checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
    checkbox1.setValue(True)
    canvas.add(checkbox1)
    canvas.add(checkbox2)

    #radioGroup1
    rb1 = RadioGroup(60,50)
    rb1.addRadioButton("Nice",10,110)
    rb1.addRadioButton("Good",70,110)
    rb1.addRadioButton("Great",140,110)
    rb1.setButtonTrue(2)
    canvas.add(rb1)

    #radioGroup2
    rb2 = RadioGroup(100,50)
    rb2.addRadioButton("Option #1",10,160)
    rb2.addRadioButton("Option #2",110,160)
    rb2.setButtonTrue(0)
    canvas.add(rb2)

    #TextArea
    textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
    canvas.add(textarea)

    #Creating Buttons
    submitBtn = Button("Submit",130,230,120,30)
    aboutBtn = Button("About",260,230,120,30)

    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)

    #Adding buttons to canvas
    canvas.add(aboutBtn)
    canvas.add(submitBtn)

    canvas.show()

    