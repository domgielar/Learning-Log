import personalinfo

def main():
    current_person = personalinfo.Personalinfo("gabriel", "54 tower St",54,"774-214-8436")
    print(current_person.get_name(), current_person.get_address(), current_person.get_age(), current_person.get_phone_number())
    current_person = personalinfo.Personalinfo("thomas", "54 tower St",54, "774-214-8436")
    print(current_person.get_name(), current_person.get_address(), current_person.get_age(), current_person.get_phone_number())
    current_person = personalinfo.Personalinfo("lincoln", "54 tower St",54, "774-214-8436")
    print(current_person.get_name(), current_person.get_address(), current_person.get_age(), current_person.get_phone_number())


if __name__ == "__main__":
    main()
