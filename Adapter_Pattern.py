# str
# int

class OldInterface: # str
    def get(self):
        return '123'

class NewInterface: # int
    def get_weird(self):
        return 456

class Adapter(OldInterface):
    def __init__(self, new_interface):
        self.new_interface = new_interface

    def get(self):
        return str(self.new_interface.get_weird())

def main(obj):
    print(f'The result is: {obj.get()}')

if __name__ == '__main__':
    new_obj = NewInterface()
    adapter_obj = Adapter(new_obj)
    main(adapter_obj)