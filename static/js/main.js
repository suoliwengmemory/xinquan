var mySwiper = new Swiper('.banner1', {
    direction: 'horizontal',
    loop: true,
    autoplay: 3000,
    nextButton: '.next',
    prevButton: '.prev',
});

var mySwiper1 = new Swiper('.store-banner', {
direction: 'horizontal',
loop: true,
autoplay: 3000,
nextButton: '.s-right',
prevButton: '.s-left',
onSlideChangeStart: function(swiper) {
$(".col-banner .img-box:eq(" + swiper.activeIndex + ")").addClass("active").siblings(".img-box").removeClass("active");
}
});

var mySwiper2 = new Swiper('.md-banner', {
    direction: 'horizontal',
    loop: true,
    autoplay: 3000,
});
var mySwiper3 = new Swiper('.news-banner', {
    direction: 'horizontal',
    loop: true,
    autoplay: 3000,
    slidesPerView: 3,
    // 如果需要前进后退按钮
    nextButton: '.pn .lb',
    prevButton: '.pn .rb',
    spaceBetween: 60,
});

$('.col-banner .img-box:eq(0)').click(function() {
    mySwiper1.slideTo(0, 1000, false); //切换到第一个slide，速度为1秒
});
$('.col-banner .img-box:eq(1)').click(function() {
    mySwiper1.slideTo(1, 1000, false); //切换到第一个slide，速度为1秒
});
$('.col-banner .img-box:eq(2)').click(function() {
    mySwiper1.slideTo(2, 1000, false); //切换到第一个slide，速度为1秒
});
$('.col-banner .img-box:eq(3)').click(function() {
    mySwiper1.slideTo(3, 1000, false); //切换到第一个slide，速度为1秒
});
$('.col-banner .img-box:eq(4)').click(function() {
    mySwiper1.slideTo(4, 1000, false); //切换到第一个slide，速度为1秒
});
$(".col-banner .img-box").on('click', function() {
    $(this).addClass("active");
    $(this).siblings(".img-box").removeClass("active")
})

// browser window scroll (in pixels) after which the "back to top" link is shown
var offset = 300,
    //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
    offset_opacity = 1200,
    //duration of the top scrolling animation (in ms)
    scroll_top_duration = 700,
    //grab the "back to top" link
    $back_to_top = $('.cd-top');

//hide or show the "back to top" link
$(window).scroll(function() {
    ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
    if ($(this).scrollTop() > offset_opacity) {
        $back_to_top.addClass('cd-fade-out');
    }
});

//smooth scroll to top
$back_to_top.on('click', function(event) {
    event.preventDefault();
    $('body,html').animate({
        scrollTop: 0,
    }, scroll_top_duration);
});
$(".f1 .c").on('click', function() {
    $(location).attr('href', 'product.html');
});
$(".gdp .probox .ltubox .ltu").on('click', function() {
    $(location).attr('href', 'goods-det.html');
});
$(".str .probox .ltubox .ltu").on('click', function() {
    $(location).attr('href', 'store-det.html');
});

document.write("<a href=\'#0\' class=\'cd-top\'>Top</a>");

// 导航二级鼠标滑过下拉
$(".top .nav .yiji").on('mouseenter', function() {
    $(this).children(".erjibox").show();
});
$(".top .nav .yiji").on('mouseleave', function() {
    $(this).children(".erjibox").hide();
});

//左侧导航二级下拉
// $(".page .zuo .m-nav li.yiji").on('mouseenter', function() {
//     $(this).children(".erjibox").slideDown();
// });
// $(".page .zuo .m-nav li.yiji").on('mouseleave', function() {
//     $(this).children(".erjibox").slideUp();
// });
$(".page .zuo .m-nav li.erji").on('click', function() {
    $(this).addClass("active").siblings("li").removeClass("active");
    $(this).parent(".erjibox").show();
    var yiji = $(this).parent(".erjibox").parent(".yiji");
    $(yiji).addClass("active").siblings(".yiji").removeClass("active")
});
//左侧一级导航点击active
$(".zuo .m-nav .yiji").on("click",function(){
    $(this).addClass("actvie").siblings(".yiji").removeClass("active")
})
//分页
$(".k-page li").on('click',function(){
    $(this).addClass("active").siblings("li").removeClass("active")
})

