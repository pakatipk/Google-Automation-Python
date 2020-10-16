#this this how to modify file (read/write/append/delete)

#check if guests.txt file have right names written
def print_guests():
    with open("guests.txt","r") as file:
        print("Guest: ")
        for name in file:
            print(name.strip())
        print(" ")

#creating file from input
def new_guests(initial_guests):
    file = open("guests.txt","w")
    for name in initial_guests:
        file.write(name + "\n")
    file.close()

new_guests(["Atsushi","Bee","Shingo","Taiki","Daiki","Hana"])
print_guests()

#adding new guests from input
def add_guests(more_guests):
    with open("guests.txt","a") as file:
        for name in more_guests:
            file.write(name + "\n")

add_guests(["Joy","Toru","Tomo"])
print_guests()

#removing the guests that have checked out
def check_out(out_guests):
    temp_list = []
    with open("guests.txt","r") as file:
        for name in file:
            temp_list.append(name.strip())
    with open("guests.txt","w") as file:
        for name in temp_list:
            if name not in out_guests:
                file.write(name + "\n")

check_out(["Shingo","Taiki"])
print_guests()


def check_guests(guests_to_check):
    temp_list = []
    with open("guests.txt","r") as file:
        for name in file:
            temp_list.append(name.strip())
        for name in guests_to_check:
            if name in temp_list:
                print("Guest: {} is checked in".format(name))
            else:
                print("Guest: {} is checked out".format(name))

check_guests(["Atsushi","Joy","Shingo"])
