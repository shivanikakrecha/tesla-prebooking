class TeslaPreBooking(object):

    def __init__(self, name, mobile_number, age, city):
        self.name = name
        self.mobile_number = int(mobile_number)
        self.age = int(age)
        self.city = city

    def export_customer_details(self, extension_type='txt', file_name=None):
        if file_name == None:
            file_name = "customer details"

        file_name = file_name + "." + extension_type

        # This file will be store at root folder location, Which place this script is running

        try:
            with open(file_name, "w") as text_file:

                text_file.write("Register Name: {}".format(self.name))
                text_file.write("Register Mobile Number: {}".format(self.mobile_number))
                text_file.write("Register Age: {}".format(self.age))
                text_file.write("Register City: {}".format(self.city))

        except Exception:

            print("Unable to write file!")

    def validate_details(self):
        import pdb; pdb.set_trace()
        if not isinstance(self.name, str):
            raise Exception("Name is not valid format. Please enter a string format.")

        if not isinstance(self.mobile_number, int):
            raise Exception("Mobile number is not valid format. Please enter a integer format.")

        if not isinstance(self.city, str):
            raise Exception("City is not valid format. Please enter a string format.")

        if not isinstance(self.age, int):
            raise Exception("Age is not valid format. Please enter a integer format.")

        return None


class FetchUserDetails(object):
        
    def fetch_user_name(self):
        name = input("Please register your full name: ")
        return name

    def fetch_user_mobile_number(self):
        mobile_number = input("Please register your mobile number: ")
        return mobile_number

    def fetch_user_age(self):
        age = input("Please register your age: ")
        return age

    def fetch_user_city(self):
        city = input("Please register your city: ")
        return city


def main(welcome_message):
    print(welcome_message)

    while True:
        
        # Create user details object 
        obj = FetchUserDetails()
        name = obj.fetch_user_name()
        mobile_number = obj.fetch_user_mobile_number()
        age = obj.fetch_user_age()
        city = obj.fetch_user_city()

        registration_object = TeslaPreBooking(name, mobile_number, age, city)

        registration_object.validate_details()

        # Fetch extension by user choice
        extension_type = input("Please select a type to export registration details: txt/pdf ")

        if extension_type.lower() in ['pdf', 'txt']:
            registration_object.export_customer_details(
                extension_type = extension_type.lower(),
                file_name = name
                )
        else:
            registration_object.export_customer_details(file_name = name)

        user_choice = input("Are you want to add another registration? Yes/No ")

        if user_choice.lower() == 'no':
            break


if __name__ == "__main__":
    welcome_message = "Welcome to tesla pre booking! Please fill below details to book Tesla."

    main(welcome_message)

    print("Tesla will contact you sooner. Enjoy Tesla!")

