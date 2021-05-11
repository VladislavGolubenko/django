function press_dropdown(btn){

    select = document.getElementsByClassName('dropdown_select');
    faSortDown = document.getElementsByClassName('fa-sort-down');
    faSortUp = document.getElementsByClassName('fa-sort-up');


    if(btn.value == 'first'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select')[i].style.display = "none";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('fa-sort-up')[0].style.display = "block";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('fa-sort-down')[0].style.display = "none";
        }

        btn.setAttribute('value', 'second')
    }
    else if(btn.value == 'second'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select')[i].style.display = "flex";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('fa-sort-up')[0].style.display = "none";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('fa-sort-down')[0].style.display = "block";
        }

        btn.setAttribute('value', 'first')
    }
}