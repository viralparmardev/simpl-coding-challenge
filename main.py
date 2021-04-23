from operations import transactions, participants, reports, updates
from responses import exceptions

while True:
    command = input()
    arguments = command.split(" ")

    try:
        if arguments[0] == "new":
            if arguments[1] == "user":
                participants.new_user(arguments)
            elif arguments[1] == "merchant":
                participants.new_merchant(arguments)
            elif arguments[1] == "txn":
                transactions.new_purchase(arguments)
            else:
                exceptions.invalid_command()

        elif arguments[0] == "update":
            if arguments[1] == "merchant":
                updates.update_merchant_discount_percentage(arguments)
            else:
                exceptions.invalid_command()

        elif arguments[0] == "payback":
            transactions.payback_dues(arguments)

        elif arguments[0] == "report":
            report_type = arguments[1]

            if report_type == "discount":
                reports.get_discount_received(arguments)
            elif report_type == "dues":
                reports.get_dues_for_user(arguments)
            elif report_type == "users-at-credit-limit":
                reports.get_users_at_credit_limit()
            elif report_type == "total-dues":
                reports.get_total_dues()
            else:
                exceptions.invalid_command()

        elif arguments[0] == "exit":
            break

        else:
            exceptions.invalid_command()

    except exceptions.InvalidCommandException as e:
        print(e)

    except exceptions.InvalidArgumentException as e:
        print(e)

    except Exception as e:
        print(e)
        print("please enter a correct command")
