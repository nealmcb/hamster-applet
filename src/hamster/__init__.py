import os

BUS_NAME = "org.gnome.Hamster" + (".test" if os.getenv("HAMSTER_DB", "") else "")
