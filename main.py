from pyscript import display, document

def submit_form(e):
    FirstName = document.getElementById("Fname").value
    LastName = document.getElementById("Lname").value

    grade7 = {"skibidi toilet", "skibidi toilet 2", "skibidi toilet 3"}
    grade8 = {"sigma", "sigma 2", "sigma 3"}
    grade9 = {"example", "example 2", "example 3"}
    grade10 = {"test", "test 2", "test 3"}

    allmembers = grade7|grade8|grade9|grade10 | {FirstName + " " + LastName}

    display(f"Club members: {', '.join(allmembers)}")
    document.getElementById("total-members").innerHTML = f"Total members: {len(allmembers)}"