/* Name: Coby Zimmerman
     Date: 10/5/20
     Assignment: CS336 Assignment #5b
     Description: JS page including all the JS functions and properties that make the HTML more interactive and
     animated. Includes two functions in particular: potentialErrors() for the registration form and chosenAwardWinner()
     for the poll form. Now also includes methods for cookies and local storage.
     */

function potentialErrors() {
    let workshopB = document.getElementById("bassone");
    let workshopD = document.getElementById("guitartwo");
    let workshopE = document.getElementById("basstwo");
    let workshopF = document.getElementById("drumstwo");
    let workshopH = document.getElementById("bassthree");
    let workshopG = document.getElementById("guitarthree");
    let workshopI = document.getElementById("drumsthree");

    let currLeft = window.screenLeft;
    let currTop = window.screenTop;
    let centerleft = ((window.innerWidth / 2) - (500 / 2)) + currLeft;
    let centertop = ((window.innerHeight / 2) - (400 / 2)) + currTop;

    let errorWindow = window.open("", "_blank", "scrollbars=1, height=400, width=500, " +
        "left="+centerleft+", top="+centertop+"");
    errorWindow.focus();

    let isValid = true;

    if (workshopB.checked===true) {
        if (workshopD.checked===true || workshopE.checked===true || workshopF.checked===true) {
            errorWindow.document.write("<p>You chose: \"Getting to Know the Structure of the Bass, Its Role in Music, and "
                + "the Differences Between Using a Pick and Fingers.\" This workshop covers sessions 1 and 2, therefore, "
                + "you may not select other workshops in session 2.</p>");
            errorWindow.document.body.style.backgroundColor = "lightslategray";
            isValid = false;
        }
        else if (workshopH.checked===true) {
            errorWindow.document.write("<p>You chose: \"Improving your Bass Playing with Flea from the Red Hot Chili" +
                " Peppers!\" which is not a valid option if you chose the second workshop in session 1.</p>")
            errorWindow.document.body.style.backgroundColor = "lightslategray";
            isValid = false;
        }
    }

    if (workshopF.checked===true) {
        if(workshopG.checked===true || workshopI.checked===true) {
            errorWindow.document.write("<p>You chose: \"Simple Drum Parts From Popular Songs to Get You Playing with "
                + "Others as Soon as Possible.\" If you take this workshop, you must also take \"Improving your Bass " +
                "Playing with Flea from the Red Hot Chili Peppers!\" You cannot take the other two workshops in session "
                + "3.</p>")
            errorWindow.document.body.style.backgroundColor = "lightslategray";
            isValid = false;
        }
    }

    if (workshopH.checked===true && workshopB.checked===false) {
        if (workshopF.checked===false) {
            errorWindow.document.write("<p>You chose: \"Improving your Bass Playing with Flea from the Red Hot" +
                " Chili Peppers!\", but you did not choose to take: \"Simple Drum Parts From Popular Songs to Get You " +
                "Playing with Others as Soon as Possible.\" You must sign up for the latter before you can sign up for" +
                " the former.</p>");
            errorWindow.document.body.style.backgroundColor = "lightslategray";
            isValid = false;
        }
    }

    if (isValid === true) {
        storeCookie();
    }
    return isValid;
}

/* Function that includes alert messages based on who the users vote for (if anyone). Supposed to include local storage
* and textcontent / innerHTML, but I couldn't figure it out. */
function chosenAwardWinner() {

    let nomineeOne = document.getElementById("nom1");
    let nomineeTwo = document.getElementById("nom2");
    let nomineeThree = document.getElementById("nom3");
    let kurtCount = parseInt(localStorage.getItem("kurtCount"));
    let jamesCount = parseInt(localStorage.getItem("jamesCount"));
    let chrisCount = parseInt(localStorage.getItem("chrisCount"));
    let nom1 = document.getElementById("nominee1");
    let nom2 = document.getElementById("nominee2");
    let nom3 = document.getElementById("nominee3");

    //localStorage.setItem("kurtCount", kurtCount);
    //localStorage.setItem("jamesCount", jamesCount);
    //localStorage.setItem("chrisCount", chrisCount);

    //console.log(localStorage.getItem("kurtCount"));
    //console.log(localStorage.getItem("jamesCount"));
    //console.log(localStorage.getItem("chrisCount"));

    if (nomineeOne.checked===true) {
        kurtCount += 1;
        localStorage.setItem("kurtCount", kurtCount);
        nom1.textContent = kurtCount;
        console.log(kurtCount);
        alert("Thank you for voting for: " + nomineeOne.value);
    }
    else if (nomineeTwo.checked===true) {
        jamesCount += 1;
        localStorage.setItem("jamesCount", jamesCount);
        nom2.textContent = jamesCount;
        alert("Thank you for voting for: " + nomineeTwo.value);
    }
    else if (nomineeThree.checked===true) {
        chrisCount += 1;
        localStorage.setItem("chrisCount", chrisCount);
        nom3.textContent = chrisCount;
        alert("Thank you for voting for: " + nomineeThree.value);
    }
    else {
        alert("No nominee selected");
    }
}

function displayVoteTotals() {
    let kurtCount = 0;
    let chrisCount = 0;
    let jamesCount = 0;

    // Find the user's choice and update the local storage and alert the user

    if (localStorage.getItem("kurtCount") == null) {
        localStorage.setItem("kurtCount", kurtCount);
    }
    else {
        kurtCount = localStorage.getItem("kurtCount");
    }

    if (localStorage.getItem("jamesCount") == null) {
        localStorage.setItem("jamesCount", jamesCount);
    }
    else {
        jamesCount = localStorage.getItem("jamesCount");
    }

    if (localStorage.getItem("chrisCount") == null) {
        localStorage.setItem("chrisCount", chrisCount);
    }
    else {
        chrisCount = localStorage.getItem("chrisCount");
    }
 }

/* function to store a cookie with the users input in the fields */
function storeCookie() {
    let firstname = "firstname:" + document.getElementById("first_name").value + "^";
    let lastname = "lastname:" + document.getElementById("last_name").value + "^";
    let address = "address:" + document.getElementById("address_one").value + "^";
    let city = "city:" + document.getElementById("city").value + "^";
    let state = "state:" + document.getElementById("state").value + "^";
    let zip = "zip:" + document.getElementById("zip").value + "^";
    let telephone = "telephone:" + document.getElementById("telenumber").value + "^";
    let email = "email:" + document.getElementById("email").value + "^";
    let url = "url:" + document.getElementById("weburl").value + "^";
    let position = "position:" + document.getElementById("companypos").value + "^";
    let companyname = "companyname:" + document.getElementById("companyname").value + "^";

    let confid = document.getElementById("conf_id").value + "=";

    if (document.getElementById("conf_id").value === "123456") {
        document.cookie = confid + firstname + lastname + address + city + state + zip + telephone + email + url +
            position + companyname + ";";

        retrieveCookie("123456");
    }

}
/* function that retrieves the large cookie and parses the strings within */
function retrieveCookie(cookieName) {
        let result = document.cookie;
        console.log("full cookie = " + result);
        let resultArray = result.split(";");
        console.log(resultArray);

        for (var i = 0; i < resultArray.length; i++) {
            var keyvaluepair = resultArray[i].split("=");
            var key = keyvaluepair[0];
            console.log(key);
            var value = keyvaluepair[1];
            console.log(value);
            var valueArray = value.split("^");
            console.log(valueArray);

            var first = valueArray[0].split(":");
            console.log(first);
            var fname = first[1];
            console.log(fname);
            var last = valueArray[1].split(":");
            var lname = last[1];
            console.log(lname);
            var addy = valueArray[2].split(":");
            var addres = addy[1];
            console.log(addres);
            var c = valueArray[3].split(":");
            var cit = c[1];
            var st = valueArray[4].split(":");
            var stat = st[1];
            var z = valueArray[5].split(":");
            var zi = z[1];
            var tel = valueArray[6].split(":");
            var teleph = tel[1];
            var em = valueArray[7].split(":");
            var emai = em[1];
            var compw = valueArray[8].split(":");
            console.log(compw);
            var compweb = compw[1] + compw[2];
            var compp = valueArray[9].split(":");
            var comppos = compp[1];
            var compn = valueArray[10].split(":");
            var compnam = compn[1];
        }

        matchCookie(fname, lname, addres, cit, stat, zi, teleph, emai, compweb, comppos, compnam);
}

/* function that matches the cookies to the fields for autopopulation */
function matchCookie(first, last, address, city, state, zip, telephone, email, companyweb, companypos, companyname) {
    //console.log("page is fully loaded");
    document.getElementById("first_name").value = first;
    document.getElementById("last_name").value = last;
    document.getElementById("address_one").value = address;
    document.getElementById("city").value = city;
    document.getElementById("state").value = state;
    document.getElementById("zip").value = zip;
    document.getElementById("telenumber").value = telephone;
    document.getElementById("email").value = email;
    document.getElementById("weburl").value = companyweb;
    document.getElementById("companypos").value = companypos;
    document.getElementById("companyname").value = companyname;
}


