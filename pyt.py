from abc import ABC, abstractmethod
#unique_id ===> ایدی منحصر به فرد
#contact_info ====> اطلاعات تماس
class Person(ABC):
    def __init__(self, name ,unique_id ,contact_info):
        self.name = name
        #self.age = age
        self.contact_info = contact_info
        self.unique_id = unique_id

    def __str__ (self):
        return f"{self.unique_id} : person_unique_id , {self.name} : name , {self.contact_info} : contact_info " 
    
    # اپدیت اطلاعات تماس
    def update_contact_details (self ,new_contact_info):
        self.contact_info = new_contact_info
        print("updated")

    @abstractmethod
    def show_info(self):
        pass

class Admin(Person):
    def __init__(self, name, age,unique_id ,contact_info):
        super().__init__(name ,unique_id ,contact_info)
        self.age = age
    
    def remove (self, staff_id):
        pass 

#اپدیت نقش کارکنان 
    def update_staff_role(self ,staff_id ,new_role):
        pass

# تایید 
    def approve (self, room_id, maintenance_type):
        pass

    def show_info(self):
        print(f" {self.name} is a admin")

# کارکنان
class Staff(Person):
    def __init__(self, name, age, unique_id , contact_info ):
        super().__init__(name, unique_id ,contact_info)
        #self.role = role
        self.age = age 

    def show_info(self):
        print(f" {self.name} is a staff")

# مهمانان
class Guests(Person):
    def __init__(self, name, unique_id , contact_info):
        super().__init__(name, unique_id ,contact_info)
        #self.age = age
    
    # در خواست اتاق
    def request_room (self, room_type ,dates):
        pass
    # اصلاح رزرو
    def amend_booking (self, booking_id ,new_dates):
        pass
    #کنسل مردن رزرو
    def cancel_booking (self, booking_id):
        pass
    # بازخورد 
    def give_feedback (self, feedback_text):
        pass

    def show_info(self):
        print(f" {self.name} is a guests")

    

class Room:
    def __init__(self, room_id, room_type, status):
        self.room_id = room_id
        self.room_type = room_type
        self.status = status
    
    def __str__ (self):
        return f"{self.room_id} : room ID , {self.room_type} : room_type , {self.status} : status "
    #تنظیم وضعیت اتاق
    def set_room_status(self, new_status):
        self.status = new_status 

    '''def show_info(self):
        print(f" {self.name} is a room")'''

    

class Hotel:
    def __init__(self):
        self.rooms = []
        self.staff = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_staff(self, staff):
        self.staff.append(staff)

    def add_guest(self, guest):
        self.guests.append(guest)

    # لیست اتاق های در دسترس
    def list_available_rooms(self, room_type):
        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.status == 'available']
        return available_rooms
    
    # دریافت اطلاعات مهمان
    def get_guest_details(self, guest_id):
        guest = [guest for guest in self.guests if guest.guest_id == guest_id]
        return guest
    
    # خلاصه عملیات روزانه
    def summarize_daily_operations(self):
        print("Total rooms: ", len(self.rooms))
        print("Total available rooms: ", len([room for room in self.rooms if room.status == 'available']))
        print("Total guests: ", len(self.guests))
        print("Total staff: ", len(self.staff))

if __name__ == "__main__":
    a1 = Admin("ali", 20 , 123, "k55")
    print(vars(a1))
    s1 = Staff("mony", 23 ,"p33" ,233334)
    print(vars(s1))
    r1 = Room("o99" ,"ll" ,"jhccv")
    print(vars(r1))
    h1 = Hotel("de")
    print(h1)