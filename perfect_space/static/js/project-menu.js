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
    this.blockItems = document.querySelectorAll('.page h4');
    this.updateMenuItems();
};
ProjectMenu.prototype.events = function() {
    this.clickItemEvent();
};
ProjectMenu.prototype.updateMenuItems = function() {
    if (!this.menuItems.length) {
        return;
    }

    if (this.menuItems.length == this.blockItems.length) {
        return;
    }

    var menuItemsParent = this.menuItems[0].parentElement;
    for (var i=-1, l=this.blockItems.length; ++i<l;) {
        var block = this.blockItems[i];
        if (!this.findMenu(block.textContent)) {
            var menu = document.createElement('div');
            menu.className = 'project-menu-item';
            menu.textContent = block.textContent;
            menuItemsParent.appendChild(menu);
        }
    }
};
ProjectMenu.prototype.findMenu = function(title) {
    var finded = false;

    for (var j=-1, k=this.menuItems.length; ++j<k;) {
        var menu = this.menuItems[j];
        if (menu.textContent.toLowerCase() == title.toLowerCase()) {
            finded = true;
        }
    }

    return finded;
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
