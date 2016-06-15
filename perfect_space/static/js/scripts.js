$(document).ready(function () {
    // fix menu li width
    var menuItems = document.getElementById('menu').querySelectorAll('li');
    for (var i=-1, l=menuItems.length; ++i<l;) {
        var item = menuItems[i];
        item.style.width = item.clientWidth + 'px';
        item.style.height = item.clientHeight + 'px';
    }

    var galleries = document.getElementsByClassName('gallery');
    var j = 0;
    while (galleries.length > 0) {
        new Gallery(galleries[0], j++);
    }

    lightbox.option({
        disableScrolling: true,
        fixedNavigation: true
    });
});
