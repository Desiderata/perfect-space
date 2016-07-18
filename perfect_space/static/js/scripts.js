var ProjectMenu = function(element) {
    if (!element) {
        return;
    }

    this.element = element;
    this.menuItems = [];
    this.blockItems = [];
    this.init();
    this.events();
};
ProjectMenu.prototype.init = function() {
    this.menuItems = this.element.getElementsByClassName('project-menu-item');
    this.blockItems = document.querySelectorAll('h4.project-menu-item');
};
ProjectMenu.prototype.events = function() {
    this.clickItemEvent();
};
ProjectMenu.prototype.clickItemEvent = function() {
    if (!this.menuItems.length) {
        return;
    }

    for (var i=-1, l=this.menuItems.length; ++i<l;) {
        this.menuItems[i].addEventListener('click', this.onClickMenuItem.bind(this));
    }
};
ProjectMenu.prototype.onClickMenuItem = function(event) {
    event.preventDefault();
    var target = event.target;

    this.inactiveMenu();
    target.classList.add('active');
    this.gotoBlock(target.textContent);
};
ProjectMenu.prototype.inactiveMenu = function() {
    if (!this.menuItems.length) {
        return;
    }

    for (var i=-1, l=this.menuItems.length; ++i<l;) {
        this.menuItems[i].classList.remove('active');
    }
};
ProjectMenu.prototype.gotoBlock = function(text) {
    for (var i=-1, l=this.blockItems.length; ++i<l;) {
        var block = this.blockItems[i];
        var blockText = block.textContent;
        if (blockText == text) {
            $('html, body').animate({scrollTop: $(block).offset().top }, 1000);
        }
    }
};



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

    lightbox.option({
        disableScrolling: true,
        fixedNavigation: true
    });
});
