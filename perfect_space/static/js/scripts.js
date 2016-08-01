$(document).ready(function () {
    // Mobile
    new Mobile();

    var galleries = document.getElementsByClassName('gallery');
    var j = 0;
    while (galleries.length > 0) {
        new Gallery(galleries[0], j++);
    }

    var projectMenu = document.getElementsByClassName('project-menu');
    if (projectMenu.length) {
        new ProjectMenu(projectMenu[0])
    }

    // Stickyfill
    $('.sticky').Stickyfill();

    var publicationImages = document.getElementsByClassName('publication-image');
    for (var r=-1, p=publicationImages.length; ++r<p;) {
        var publicationImage = publicationImages[r];
        publicationImage.addEventListener('click', function(event) {
            event.preventDefault();
            var target = event.target;
            var $gallery = $(target).next('.publication-gallery');
            $gallery.find('.item a').click();
        });
    }

    // fix menu li width
    fixMenuWidth();
});

function fixMenuWidth() {
    var menuItems = document.getElementById('menu').querySelectorAll('li');
    for (var i=-1, l=menuItems.length; ++i<l;) {
        var item = menuItems[i];
        item.style.width = item.clientWidth + 2 + 'px';
        item.style.height = item.clientHeight + 'px';
    }
}
