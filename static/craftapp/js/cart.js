var updateBtns = document.getElementsByClassName('update-cart')

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            Gallery filter
        --------------------*/
        $('.featured__controls li').on('click', function () {
            $('.featured__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.featured__filter').length > 0) {
            var containerEl = document.querySelector('.featured__filter');
            var mixer = mixitup(containerEl);
        }
    });
    
for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('USER:', user)
    if(user == 'AnonymousUser'){
      console.log('Not loged in')
    }else{
      updateUserOrder(productId, action)
    }
  })

}


function updateUserOrder(productId, action){
  console.log('User is loged in')

  var url = '/update_item/'

  fetch(url, {
    method : 'POST',
    headers : {
      'Content-Type' : 'application/json',
      'X-CSRFToken' : csrftoken, 
    },
    body: JSON.stringify({'productId': productId, 'action': action})
  })

  .then((response) =>{
    return response.json()
  })
  .then((data) =>{
    console.log('data', data)
    location.reload()
  })
}
