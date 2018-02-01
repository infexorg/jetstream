function calcOM() {
    var om1 = document.getElementById("om1").value;
    var om2 = document.getElementById("om2").value;
    var om3 = document.getElementById("om3").value;
    var omd = document.getElementById("omd").value;

    var leg1 = (om1*om1 + omd*omd - om2*om2) / (2*omd);
    var mid = Math.sqrt(omd*omd + leg1*leg1 - omd*leg1);
    var leg2 = (omd*omd - omd*leg1 + om1*om1 - om3*om3) / (2*mid);

    var leg1r = omd - leg1;
    var leg2r = mid - leg2;

    document.getElementById("leg1").value = leg1.toFixed(1);
    document.getElementById("leg1r").value = leg1r.toFixed(1);
    document.getElementById("leg2").value = leg2.toFixed(1);
    document.getElementById("leg2r").value = leg2r.toFixed(1);
}