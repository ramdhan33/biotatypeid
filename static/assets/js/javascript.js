const parentContainer = document.querySelector('.read-more-container');

parentContainer.addEventListener('click',event=>{
    
    const current = event.target;
    
    const isReadMoreBtn = current.className.includes('read-more-btn');
    
    if(!isReadMoreBtn) return;
    
    const currentText = event.target.parentNode.querySelector('.read-more-text');
    
    currentText.classList.toggle('read-more-text--show');
    
    current.textcontent = current.textcontent.includes('Read More') ?
    "Read Less..." : "Read More...";
})
//efek scroll 
$(document).ready(function () {
    var scroll_pos = 0;
    $(document).scroll(function () {
        scroll_pos = $(this).scrollTop();
        if (scroll_pos > 0) {
            $("nav").addClass("putih");
            $("nav img.hitam").show();
            $("nav img.putih").hide();
        } else {
            $("nav").removeClass("putih");
            $("nav img.hitam").hide();
            $("nav img.putih").show();
        }
    })
});