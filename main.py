import os
import dbOOPS

if __name__ == "__main__":

    cobj = dbOOPS.DBConnection()
    cobj.connect()

    os.system("cls")
    print("Vaccination Center Management System")
    print("------------------------------------")
    input("Press Enter to continue...")

    os.system("cls")
    print("Login")

    username = input("Username: ")
    password = input("Password: ")

    cobj.cursor.execute(
        "SELECT * FROM tbLogin WHERE Username=? AND Password=?",
        (username, password)
    )
    rows = cobj.cursor.fetchall()

    if rows:
        print("Login Successful")
        input("Press Enter...")

        while True:
            os.system("cls")
            print("Main Menu")
            print("1. Manage Centers")
            print("2. Manage Medicines")
            print("3. Manage Citizens")
            print("4. Vaccination Records")
            print("5. Certificates")
            print("6. Feedback")
            print("7. Exit")

            choice = input("Enter choice: ")

            # ---------------- CENTER MENU ----------------
            if choice == "1":
                centerObj = dbOOPS.Center()

                while True:
                    os.system("cls")
                    print("Center Menu")
                    print("1. Add Center")
                    print("2. View Centers")
                    print("3. Update Center")
                    print("4. Delete Center")
                    print("5. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        name = input("Center Name: ")
                        address = input("Address: ")
                        phone = input("Phone: ")
                        email = input("Email: ")
                        incharge = input("Incharge Name: ")
                        timings = input("Timings: ")

                        centerObj.insert_center(
                            name, address, phone, email, incharge, timings
                        )
                        input("Press Enter...")

                    elif ch == "2":
                        centerObj.view_centers()
                        input("Press Enter...")

                    elif ch == "5":
                        break

            # ---------------- MEDICINE MENU ----------------
            elif choice == "2":
                medObj = dbOOPS.Medicine()

                while True:
                    os.system("cls")
                    print("Medicine Menu")
                    print("1. Add Medicine")
                    print("2. View Medicines")
                    print("3. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        company = input("Company Name: ")
                        name = input("Medicine Name: ")
                        doi = input("Date of Issue (YYYY-MM-DD): ")
                        doe = input("Date of Expiry (YYYY-MM-DD): ")
                        qty = int(input("Quantity: "))

                        medObj.insert_medicine(
                            company, name, doi, doe, qty
                        )
                        input("Press Enter...")

                    elif ch == "2":
                        medObj.view_medicines()
                        input("Press Enter...")

                    elif ch == "3":
                        break

            # ---------------- CITIZEN MENU ----------------
            elif choice == "3":
                citizenObj = dbOOPS.Citizen()

                while True:
                    os.system("cls")
                    print("Citizen Menu")
                    print("1. Add Citizen")
                    print("2. View Citizens")
                    print("3. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        name = input("Name: ")
                        cnic = input("CNIC: ")
                        phone = input("Phone: ")
                        address = input("Address: ")

                        citizenObj.insert_citizen(name, cnic, phone, address)
                        input("Press Enter...")

                    elif ch == "2":
                        citizenObj.view_citizens()
                        input("Press Enter...")

                    elif ch == "3":
                        break

            # ---------------- RECORD MENU ----------------
            elif choice == "4":
                recordObj = dbOOPS.Record()

                while True:
                    os.system("cls")
                    print("Vaccination Record Menu")
                    print("1. Add Record")
                    print("2. View Records")
                    print("3. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        cid = int(input("Citizen ID: "))
                        center_id = int(input("Center ID: "))
                        med_id = int(input("Medicine ID: "))
                        dose = int(input("Dose Number: "))
                        date = input("Vaccination Date (YYYY-MM-DD): ")

                        recordObj.insert_record(cid, center_id, med_id, dose, date)
                        input("Press Enter...")

                    elif ch == "2":
                        recordObj.view_records()
                        input("Press Enter...")

                    elif ch == "3":
                        break

            # ---------------- CERTIFICATE MENU ----------------
            elif choice == "5":
                certObj = dbOOPS.Certificate()

                while True:
                    os.system("cls")
                    print("Certificate Menu")
                    print("1. Issue Certificate")
                    print("2. View Certificates")
                    print("3. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        cid = int(input("Citizen ID: "))
                        date = input("Issue Date (YYYY-MM-DD): ")
                        status = input("Status: ")

                        certObj.insert_certificate(cid, date, status)
                        input("Press Enter...")

                    elif ch == "2":
                        certObj.view_certificates()
                        input("Press Enter...")

                    elif ch == "3":
                        break

            # ---------------- FEEDBACK MENU ----------------
            elif choice == "6":
                feedObj = dbOOPS.Feedback()

                while True:
                    os.system("cls")
                    print("Feedback Menu")
                    print("1. Add Feedback")
                    print("2. View Feedback")
                    print("3. Back")

                    ch = input("Enter choice: ")

                    if ch == "1":
                        cid = int(input("Citizen ID: "))
                        message = input("Message: ")
                        rating = int(input("Rating (1-5): "))

                        feedObj.insert_feedback(cid, message, rating)
                        input("Press Enter...")

                    elif ch == "2":
                        feedObj.view_feedback()
                        input("Press Enter...")

                    elif ch == "3":
                        break

            elif choice == "7":
                print("Exiting System...")
                break

    else:
        print("Login Failed")
        input("Press Enter...")

    cobj.disconnect()
