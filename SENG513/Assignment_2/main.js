$(document).ready(function() {
    let clear = false;
    let ans = "0";
    let calcField = $("#calc-field");
    let prevCalcField = $("#prev-calc-field");

    $("button").click(function(event) {
        let button = $(event.target);
        if(button.attr("id") === "eval")
        {
            clear = true;
            let exp = calcField.text();
            try {
                let val = eval(exp);
                if(val === undefined)
                    exp = "Ans";
                else 
                    ans = val;
                prevCalcField.text(exp + "=" + ans);                
            } catch(error) {
                prevCalcField.text(exp + "=ERROR");
            }
            calcField.text(ans);
            
        } else if(button.attr("id") === "clear-error"){
            calcField.text(calcField.text().slice(0, -1));
        } else {
            if(clear){
                if(button.attr("class") !== "op")
                calcField.text("");
                clear = false;
            }
            calcField.append(button.text());
        }
    });
});


  