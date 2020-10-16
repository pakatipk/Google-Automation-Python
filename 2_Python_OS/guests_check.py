#this this how to modify file (read/write/append/delete)
initial_guests = ["Atsushi","Bee","Shingo","Taiki","Daiki","Hana"]

#check if guests.txt file have right names written
def check_guests():
    with open("guests.txt","r") as file:
        for name in file:
            print(name)

#creating empty text file and write names in
file = open("guests.txt","w")
for name in initial_guests:
    file.write(name + "\n")
file.close()
check_guests()

#adding new guests
new_guests = ["Joy","Toru","Tomo"]
with open("guests.txt","a") as file:
    for name in new_guests:
        file.write(name + "\n")
check_guests()

#removing the guests who have checked out
checkout_guests = ["Shingo","Taiki"]
temp_list = []
with open("guests.txt","r") as file:
    for name in file:
        temp_list.append(name.strip())
with open("guests.txt","w") as file:
    for name in temp_list:
        if name not in checkout_guests:
            file.write(name + " ")
check_guests()
