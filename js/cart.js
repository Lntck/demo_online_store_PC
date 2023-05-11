$(document).ready(function(){
	
	
	var textInput = $('#inputshop').val();
	
	$(".b-popup").hide();
	
	
	if (localStorage.getItem('shoplistlocal')) {
    	$('.list').html(localStorage.getItem('shoplistlocal'));
	}
			
	
    $(".product__btn.btn").on("click",function(e){
		$('.count').css({"display":"grid"});
    	var itemvalue = this.html();
		$('.list').append('<li    class="item">'+ this.html() +'</li>');
		var shoplistlocal = $('.list').html();
		localStorage.setItem('shoplistlocal', shoplistlocal);
		return false;
    });

	  			
	$(".list").on("click", ".item", function () {
    	$(this).remove();
		  $('.count').css({"display":"grid"});
		  var itemlength = $(".app-body li").length;
		  $('.count').text(itemlength);
		  var shoplistlocal = $('.list').html();
    	localStorage.setItem('shoplistlocal', shoplistlocal);
		return false;
    });
	
	    			 
     $(".closepopup").click(function(){
	 $(".b-popup").hide(200);
    });
	

    $(".openpopup").click(function(){
		if ($('.item').is('li')) {
		$(".b-popup").fadeIn(200);}
	else {
		$(".tooltipshop2").animate({marginLeft: "20px",easing: "easeout",opacity:"1"},300);
		$(".tooltipshop2").delay(900).animate({opacity:"0",marginLeft: "-90px"});
	}
	});
    $("#send").click(function(){
		var itemname = $("#inputname").val();
		var itememail = $("#inputemail").val();
		var itemtel = $("#inputtel").val();
		var shopbox = $(".app-body").html();
		$.ajax({
			url: "sendmessege.php",
			type: "post",
			dataType: "json",
			  data: {
				 "itemname": user_name,
				 "itememail": user_email,
				 "itemtel": user_comment,
				 "shopbox": user_money
			  },
			 success: function() {
				 alert("Ваше сообщение отправлено!");
				 
				  }
	});
		});
		
		$('.closewindow').click(function(){
			$('.app').fadeOut(500);
		});	
	    	$('#tray').click(function(){
			$('.app').fadeIn(500);
		});	
		
		
	$('.items').click(function() {
		var itemlength = $(".app-body li").length;
		$('.count').text(itemlength);	
	});
		
		
	$(".openpopup2").click(function() {
   		window.localStorage.clear();
		$('.list').children().remove();
		$('.count').hide();
    	return false;
	});		
});