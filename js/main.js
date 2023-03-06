$(function(){
    $('.main-menu-btn').on('click', function(e){
        e.preventDefault();
        $('.main-menu-content').addClass('active');
    });
    $('.main-menu-close-btn').on('click', function(e){
        e.preventDefault();
        $('.main-menu-content').removeClass('active');
    })
});
    
    
    
    