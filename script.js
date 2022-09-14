$(document).ready(function (){
    $("form").submit(function (event){
        console.log("Hello");
        event.preventDefault()
        fd = new FormData();

        fd.append( 'bedrooms', '1' );
        fd.append( 'bathrooms', '1' );
        fd.append( 'sqft_living', '1' );
        fd.append( 'sqft_lot', '1' );
        fd.append( 'floors', '1' );
        fd.append( 'yr_built', '1' );
        fd.append( 'condition', '1' );
        fd.append( 'waterfront', '1' );
        fd.append( 'yr_reno', '1' );


        $.ajax({
            type: "POST",
            url: "http://localhost:5000/predict",
            data: fd,
            processData: false,
            contentType: false,
            success:function(data){
                console.log(data);
            alert(data);
            }
        });
    })
})