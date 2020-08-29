
class SemCalendar: 

    def __init__(self, start_date, end_date, break_start, break_end):
        self.start_date = start_date
        self.end_date = end_date
        self.break_start = break_start
        self.break_end = break_end
        self.__generate_weeks() 
    
    def __generate_weeks(self): 
        pass

    

class Week:

    def __init__(self, start_date, is_break): 
        self.start_date = start_date
        self.is_break = is_break
        self.items = [] 
        self.item_count = 0 
    
    def add_item(self, description): 
        self.items.append(ThingsDue(description))
        self.item_count += 1 
    
    def delete_item(self, index): 
        self.items.pop(index) 
        self.item_count -= 1

    def edit_item(self, new_description, index): 
        self.items[index].change_description(new_description)


class ThingsDue:

    def __init__(self, description): 
        self.description = description

    def change_description(self, new_description): 
        self.description = new_description



    




        