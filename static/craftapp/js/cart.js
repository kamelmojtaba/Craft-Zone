var updateBtns = document.getElementsByClassName('update-cart')

// (function ($) {

//     /*------------------
//         Preloader
//     --------------------*/
//     $(window).on('load', function () {
//         $(".loader").fadeOut();
//         $("#preloder").delay(200).fadeOut("slow");

//         /*------------------
//             Gallery filter
//         --------------------*/
//         $('.featured__controls li').on('click', function () {
//             $('.featured__controls li').removeClass('active');
//             $(this).addClass('active');
//         });
//         if ($('.featured__filter').length > 0) {
//             var containerEl = document.querySelector('.featured__filter');
//             var mixer = mixitup(containerEl);
//         }
//     });
    
for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('USER:', user)
    if(user == 'AnonymousUser'){
      addCookieItem(productId, action)
    }else{
      updateUserOrder(productId, action)
    }
  })

}

function addCookieItem(productId, action){
  console.log("Not Logged in...")

  if(action == 'add'){
    if(cart[productId] == undefined){
      cart[productId] = {'qunatity': 1}
    }else{
      cart[productId]['qunatity'] += 1 
    }
  }

  if(action == 'remove'){
    cart[productId]['qunatity'] -= 1 

    if(cart[productId]['qunatity'] <= 0){
      console.log("Removed item")
      delete cart[productId]  
    }
  }
  console.log('cart:', cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
  location.reload()
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
