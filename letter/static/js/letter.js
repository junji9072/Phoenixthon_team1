
window.myFunction = function(id) {
                    if(document.getElementById("title" + id) != null){
                        var title = document.getElementById("title" + id).textContent;
                    }

                    if(document.getElementById("image" + id) != null){
                        var image = document.getElementById("image" + id).src;
                        document.getElementById("img").src = image;
                    }else{
                        document.getElementById("img").src = "../static/image/army.jpg";
                    }
                    if(document.getElementById("comment" + id) != null){
                        var comment = document.getElementById("comment" + id).textContent;
                        comment = comment.replace(/(?:\r\n|\r|\n)/g, '<br />');
                    }

                    if(document.getElementById("created-at" + id) != null){
                        var create = document.getElementById("created-at" + id).textContent;
                    }
                    if(title != null){
                        document.getElementById("demo-title").innerHTML = title;
                    }else{
                        document.getElementById("demo-title").innerHTML = "";
                    }

                    if(comment != null){
                        document.getElementById("demo-comment").innerHTML = comment
                    }else{
                        document.getElementById("demo-comment").innerHTML = "";
                    }


                    if(create != null){
                        document.getElementById("demo-create-at").innerHTML = create;
                    }else{
                        document.getElementById("demo-create-at").innerHTML = "";
                    }
                }


function getConfirmation()
    {
        var retVal = confirm("Do you want to continue ?");
        if (retVal == true)
            {
                return true;
            }
        else
        {
            return false;
        }
    }



$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    dots:false,
    nav:true,
    autoplay:true,
    smartSpeed: 3000,
    autoplayTimeout:7000,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})
