$(document).ready(function() {
    $(document.getElementById('add_trade')).click(
        function(){
        console.log("work");
        $('<ul class="media box"><div class="media-body">{{ item_name }}</div><div class="media-right"><a>X</a></div></ul>').insertBefore($(this)).text("");
        return false;
    });
})