function checkCartCookie() {
    if (Cookies.get("cart") == null) {
        Cookies.set('cart', { totalProduct: '0' }, { expires: 7 });
        var cartObj = Cookies.getJSON('cart');
        cartObj.totalMoney = '0';
        Cookies.set('cart', cartObj, { expires: 7 });

    }
    changeCartTotal(Cookies.getJSON('cart').totalMoney);
};
/*header fix-top animation*/
$(document).ready(function () {
    var navpos = $('#header-nav').offset();
    console.log(navpos.top);
    $(window).bind('scroll', function () {
        if ($(window).scrollTop() >= navpos.top - 1) {
            //if ($(window).scrollTop() >= navpos.top - 1 && $(document).height() > 800) {
            //console.log("access!");
            //$('#header-nav').addClass('position-fixed-nav');
            $('#header-nav').addClass('navbar-fixed-top');
            $('#header-nav').css("position", "fixed");
            $('#header-nav').css("top", "0");
            $('.body-content').css("padding-top", "60px");
        }
        else {
            //console.log("leave!");
            $('#header-nav').css("position", "relative");
            $('#header-nav').css("top", "0");
            $('.body-content').css("padding-top", "0");
            //$('#header-nav').removeClass('position-fixed-nav');
            $('#header-nav').removeClass('navbar-fixed-top');

        }
    });
});
/* change element when using mobile browser*/
$(document).ready(function () {
    /* Check width on page load*/
    if ($(window).width() < 514) {
        $('#product-list').text("Danh mục").append($('<span></span>').addClass('caret'));
        $('.add-to-cart-text').text("Thêm vào giỏ");
    }
});

$(window).resize(function () {
    /*If browser resized, check width again */
    if ($(window).width() < 514) {
        $('#product-list').text("Danh mục").append($('<span></span>').addClass('caret'));
        $('.add-to-cart-text').text("Thêm vào giỏ");
    }
    else {
        $('#product-list').text("Danh mục sản phẩm").append($('<span></span>').addClass('caret'));
        $('.add-to-cart-text').text("Thêm vào giỏ hàng");
    }
});


/*event when add product to cart*/
$(".add-to-cart").click(function () {
    var product_Info = $(this).closest(".product-info");
    if ($(this).attr("isSelected") != "true") {
        var product_Id = $(product_Info).find(".product-id");
        var cartObj = Cookies.getJSON('cart');
        var checkID = $(product_Id).text();
        var pcx = $((product_Info).find(".money-value")).text();
        var price = parseInt($($(product_Info).find(".money-value")).text().split(".").join(""));
        if (cartObj.totalMoney + price >= 2000000000) {
            alert("Qúy khách được mua tối đa 2 tỷ đồng trên 1 lần đặt hàng!");
        }
        else {
            var position = positionIdInCart(checkID, cartObj);
            if (position == -1) {
                var index = cartObj.totalProduct.toString();
                cartObj[index] = checkID.toString();
                cartObj[index + "no"] = '1';
                cartObj[index + "price"] = price;
                cartObj.totalProduct++;
                cartObj.totalMoney = parseInt(cartObj.totalMoney) + price;
                Cookies.set('cart', cartObj, { expires: 7 });
            } else {
                cartObj[position + "no"] = parseInt(cartObj[position + "no"]) + 1;
                cartObj.totalMoney = parseInt(cartObj.totalMoney) + price;
                Cookies.set('cart', cartObj, { expires: 7 });
            }
            changeCartTotal(Cookies.getJSON('cart').totalMoney);
            var textInfo = $(this).find(".add-to-cart-text");
            textInfo.text("Đã thêm vào giỏ hàng");
            $(this).attr("isSelected", "true");
        }
    }
    
});

function positionIdInCart(id, cartObj) {
    var position = -1;
    for (var i = 0; i < parseInt(cartObj.totalProduct) ; i++) {
        if (id == cartObj[(i).toString()]) {
            position = i;
            break;
        }
    }
    return position;

};

function changeCartTotal(totalMoney) {

    $('.cart-total-money').text(totalMoney.toLocaleString("de-DE"));
}
function setCurrencyFormat() {
    $(".money-value").each(function () {
        var format = parseInt($(this).text()).toLocaleString("de-DE");
        $(this).text(format);
    });
}
setCurrencyFormat();


$("#search-text-box").keyup(function () {

});
searchHub.client.setResult = function (result) {
    $("#search-result-box").empty();
    for (x = 0; x < result.length; x++) {
        console.log(result[x].ProductName);
        var $newResult = $("<div>", { class: "suggest_item" });
        var img = $('<img style ="width:60px; height:60px;">');
        img.attr('src', "/img/product/" + result[x].ImageFileName);

        var info = $('<h2></h2>');
        var link = $('<a></a>');
        link.attr('href', "/product?name=" + (result[x].ProductName + result[x].ProductCode).toString().split(" ").join("-"));
        link.text(result[x].ProductName + "(" + result[x].ProductCode + ")");

        var price = $("<span>", { class: "suggest_price" });
        price.text(parseInt(result[x].Price).toLocaleString("de-DE"));

        $newResult.append(img);

        info.append(link);
        $newResult.append(info);
        $newResult.append(price);
        $("#search-result-box").append($newResult);
    }

}
