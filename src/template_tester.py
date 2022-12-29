import json

class Simulator():
    data = None
    page = 0
    
    def __init__(self):
        f = open('templates/tennis.json')
        self.data = json.load(f)
        f.close()
        
    def show_score(self):
        print("    Punteggio")
        print("       TEAM A: 0")
        print("       TEAM B: 0")
        
    def show_button(self, index, buttons_left, buttons_right):
        if index < len(buttons_left):
            left =  buttons_left[index]['text']
        else:
            left = ""
        if index < len(buttons_right):
            right =  buttons_right[index]['text']
        else:
            right = ""

        print(f"{index}. {left.ljust(25)} {index+len(buttons_left)}. {right.ljust(25)}")
        
    def show_buttons(self, buttons):
        columns = max(len(buttons[0]), len(buttons[1]))
        for i in range(0, columns):
            self.show_button(i, buttons[0], buttons[1])
            
    def show_page(self, page_number):
        page = self.data['interface']['pages'][page_number]
        print(f"*** {page['title'].upper()} ***")
        print(page['description'])
        self.show_buttons(page['buttons'])
        
    def execute_action(self, button):
        action = button["action"]
        if "goto page" in action:
            self.page = int(action.split(":")[1])
        
        
    def run(self):
            print("Running simulator...")
            while True:
                self.show_score()
                
                # Mostro la pagina
                self.show_page(self.page)
                
                # Aspetto che l'utente faccia la scelta
                choosed = int(input())
                
                if choosed < len(self.data['interface']['pages'][self.page]['buttons']):
                    button = self.data['interface']['pages'][self.page]['buttons'][choosed]
                
                    # Elaboro la scelta
                    self.execute_action(button)               
          
# print(data['interface']['pages'])
  
# # Iterating through the json
# # list
  
# Closing file

if  __name__ =='__main__':
    simulator = Simulator()
    simulator.run()
