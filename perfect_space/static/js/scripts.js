$(document).ready(function () {
    // fix menu li width
    var menuItems = document.getElementById('menu').querySelectorAll('li');
    for (var i=-1, l=menuItems.length; ++i<l;) {
        var item = menuItems[i];
        item.style.width = item.clientWidth + 'px';
        item.style.height = item.clientHeight + 'px';
    }

    var galleries = document.getElementsByClassName('gallery');
    for (var j=-1, k=galleries.length; ++j<k;) {
        var gallery = galleries[j];
        new Gallery(gallery, j);
    }

    lightbox.option({
        'disableScrolling': true,
        'fixedNavigation': true
    });
});
