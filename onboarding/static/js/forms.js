var getmat = document.getElementById("id_materialIDS");
console.log(getmat);
getmat.setAttribute("size", getmat.length);
// holt das Element mit der ID "id_materialIDS" und setzt das Attribut "size" auf seine Länge

var getacc = document.getElementById("id_accountIDS");
getacc.setAttribute("size", getacc.length);
// holt das Element mit der ID "id_accountIDS" und setzt das Attribut "size" auf seine Länge

var getothers = document.getElementById("id_otherIDS");
getothers.setAttribute("size", getothers.length);
// holt das Element mit der ID "id_otherIDS" und setzt das Attribut "size" auf seine Länge

var labels = document.getElementsByTagName("label");
labels[0].innerHTML = "New Employee";
labels[1].innerHTML = "Employee";
labels[2].innerHTML = "Materials";
labels[3].innerHTML = "Licenses";
labels[4].innerHTML = "Accounts";
labels[5].innerHTML = "Others";
// ändert den Text der Labels entsprechend der Reihenfolge

$('option').mousedown(function(e) {
    e.preventDefault();
    var originalScrollTop = $(this).parent().scrollTop();
    console.log(originalScrollTop);
    $(this).prop('selected', $(this).prop('selected') ? false : true);
    var self = this;
    $(this).parent().focus();
    setTimeout(function() {
        $(self).parent().scrollTop(originalScrollTop);
    }, 0);

    return false;
});
// verhindert das Standardverhalten beim Klicken auf eine Option,
// speichert die Scroll-Position,
// toggelt die Auswahl der Option,
// stellt die Scroll-Position wieder her
