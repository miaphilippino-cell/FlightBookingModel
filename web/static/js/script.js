// Prevent choosing the same airport

document.addEventListener(
    "DOMContentLoaded",
    function () {


        let origin = document.querySelector(
            'select[name="origin"]'
        );


        let destination = document.querySelector(
            'select[name="destination"]'
        );


        if(origin && destination){


            destination.addEventListener(
                "change",
                function(){


                    if(
                        origin.value === destination.value
                    ){

                        alert(
                            "Departure and destination cannot be the same."
                        );


                        destination.value = "";

                    }


                }
            );


        }


    }
);