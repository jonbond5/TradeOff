$(document).ready(function() {
    $(document.getElementById('add_trade_give')).click(
        function(){
        	var addedItem = $(document.getElementById('give_new_item')).val();
        	if(addedItem != ''){
        		console.log(addedItem);
        		$(document.getElementById('give_container')).append('<ul class="media box"><div class="media-body">'+addedItem+'</div><div class="media-right"><a onclick="$(this).closest(\'ul\').remove();">X</a></div></ul>')
        		$(document.getElementById('give_new_item')).val('');
        	}
        	return false;
    });

    $(document.getElementById('add_trade_get')).click(
        function(){
        	var addedItem = $(document.getElementById('request_new_item')).val();
        	if(addedItem != ''){
        		console.log(addedItem);
        		$(document.getElementById('get_container')).append('<ul class="media box"><div class="media-body">'+addedItem+'</div><div class="media-right"><a onclick="$(this).closest(\'ul\').remove();">X</a></div></ul>')
        		$(document.getElementById('request_new_item')).val('');
        	}
        	return false;
    });
})