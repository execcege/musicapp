import random
import string
import wsHandlerHost

lastPassword = None
currentPassword = ""


def generate_new_password():
    global currentPassword, lastPassword
    lastPassword = currentPassword
    currentPassword = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    broadcast_password_to_hosts()


def broadcast_password_to_hosts():
    global currentPassword
    wsHandlerHost.HostWebSocket.broadcast(currentPassword)


def password_ok_p(password):
    return True if password in [currentPassword, lastPassword] else False

generate_new_password()

if __name__ == "__main__":
    print password_ok_p("not_ok")
    print password_ok_p("IMAPASSWORD")
    generate_new_password()
    print password_ok_p("IMAPASSWORD")
    print password_ok_p(currentPassword)
    print password_ok_p("NOT_OK")
    generate_new_password()
    print password_ok_p("IMAPASSWORD")