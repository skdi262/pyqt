from pywinsparkle import pywinsparkle

import os
import time
def no_update_found():
    """ when no update has been found, close the updater"""
    print("No update found")
    print("Setting flag to shutdown PassagesUpdater")


def found_update():
    """ log that an update was found """
    print("New Update Available")


def encountered_error():
    print("An error occurred")


def update_cancelled():
    """ when the update was cancelled, close the updater"""
    print("Update was cancelled")
    print("Setting flag to shutdown PassagesUpdater")


def shutdown():
    """ The installer is being launched signal the updater to shutdown """

    # actually shutdown the app here
    print("Safe to shutdown before installing")


def main():

    # register callbacks
    pywinsparkle.win_sparkle_set_did_find_update_callback(found_update)
    pywinsparkle.win_sparkle_set_error_callback(encountered_error)
    pywinsparkle.win_sparkle_set_update_cancelled_callback(update_cancelled)
    pywinsparkle.win_sparkle_set_did_not_find_update_callback(no_update_found)
    pywinsparkle.win_sparkle_set_shutdown_request_callback(shutdown)

    # set application details
    update_url = "https://winsparkle.org/example/appcast.xml"
    pywinsparkle.win_sparkle_set_appcast_url(update_url)
    pywinsparkle.win_sparkle_set_app_details("VendorName", "TestApp1", "1.0.0")

    if os.path.isfile('dsa_pub.pem'):
        with open('dsa_pub.pem', 'r') as file:
            pub_key = file.read()
        pywinsparkle.win_sparkle_set_dsa_pub_pem(pub_key)

    # initialize
    pywinsparkle.win_sparkle_init()

    # check for updates
    pywinsparkle.win_sparkle_check_update_with_ui()

    # alternatively you could check for updates in the
    # background silently
    pywinsparkle.win_sparkle_check_update_without_ui()

    # dont do it this way, just an example to keep the thread running
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()