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

    // Mobile
    var cover = document.getElementById('cover');
    var desktop = document.getElementById('desktop');
    var os = new OS();
    if (os.android || os.ios) {
        document.body.style.minWidth = 'auto';
        document.body.style.width = '100%';
        document.body.style.paddingBottom = 0;
        cover.style.display = 'block';
    }
    else {
        desktop.style.display = 'block';
    }
    var mobileSwitch = document.getElementById('mobile-switch');
    mobileSwitch.addEventListener('click', function(event) {
        event.preventDefault();
        if (desktop.style.display = 'none') {
            cover.style.display = 'none';
            desktop.style.display = 'block';
        }
    });
});
