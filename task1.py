from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def save_name(self,name):
        self.name = name
        return self.name    

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self._is_valid(value):
            raise ValueError("Номер телефону має = 10 цифрам.")

    def _is_valid(self, value):
        return value.isdigit() and len(value) == 10                   

            
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_1 = Phone(phone)
        self.phones.append(phone_1)
        print(f"Phone {phone} added to contact {self.name}")

    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]
            print(f"Phone {phone} removed from contact {self.name}")
        else:
            print(f"Phone {phone} not found for contact {self.name}")      

    def edit_phone(self, old_phone, new_phone):
        for phones in self.phones:
            if phones.value == old_phone:
                if not Phone(new_phone)._is_valid(new_phone):
                    raise ValueError("Новый номер телефона должен содержать ровно 10 цифр.")
                phones.value = new_phone
                print(f"Phone {old_phone} changed for contact {self.name} to phone {new_phone}")
                return new_phone
            else:
                raise ValueError(f"Телефон {old_phone} не найден в записи.")           
        
           
    def find_phone(self, phone):
        for phones in self.phones:
            if phones.value == phone:
                return phone
        return None       

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Контакт з ім'ям {record.name.value} вже існує.")
        self.data[record.name.value] = record

    def find(self,name):
        return self.data.get(name)

    def delete(self,name):
        if name in self.data:
            self.data.pop(name)
  
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
book.add_record(john_record)

# # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# # Виведення всіх записів у книзі
     
print(book)

# # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
book.delete("Jane")
print(book)

