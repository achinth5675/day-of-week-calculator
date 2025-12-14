from datetime import datetime

def get_day_from_date(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%A")


def show_today_day():
    today = datetime.today()
    print("\n📅 TODAY")
    print("-" * 30)
    print("Date :", today.strftime("%d-%m-%Y"))
    print("Day  :", today.strftime("%A"))


def print_menu():
    print("\n" + "=" * 45)
    print("        DAY OF THE WEEK CALCULATOR")
    print("=" * 45)
    print("[ 1 ]  Find day for a given date")
    print("[ 2 ]  Find today's day")
    print("[ 3 ]  Exit")
    print("-" * 45)


def wait_for_user():
    input("\n👉 Press Enter to continue...")


def main():
    while True:
        print_menu()
        choice = input("👉 Select an option (1/2/3): ").strip()

        if choice == "1":
            try:
                date_input = input("\n📥 Enter date (DD-MM-YYYY): ")
                day = get_day_from_date(date_input)

                print("\n✅ RESULT")
                print("-" * 30)
                print("Day of the week:", day)

            except ValueError:
                print("\n❌ ERROR: Invalid date format. Use DD-MM-YYYY.")

            wait_for_user()

        elif choice == "2":
            show_today_day()
            wait_for_user()

        elif choice == "3":
            print("\n👋 Exiting program. Thank you!")
            break

        else:
            print("\n⚠️ Invalid selection. Please choose 1, 2, or 3.")
            wait_for_user()


if __name__ == "__main__":
    main()
