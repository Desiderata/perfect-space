var ProjectMenu = function(element) {
    if (!element) {
        return;
    }

    this.element = element;
    this.menuItems = [];
    this.blockItems = [];
    this.scrollTitles = {};
    this.init();
    this.events();
};


// Init
ProjectMenu.prototype.init = function() {
    this.menuItems = this.element.getElementsByClassName('project-menu-item');
    this.blockItems = document.querySelectorAll('.page h4');
    this.projectCover = document.getElementById('project-cover');
    this.projectCover.addEventListener('load', this.onCoverLoad.bind(this));
    if (this.projectCover.complete) {
        this.onCoverLoad();
    }
};
ProjectMenu.prototype.initScrollTitles = function() {
    for (var i=-1, l=this.blockItems.length; ++i<l;) {
        var block = this.blockItems[i];
        var top = $(block).offset().top;
        this.scrollTitles[top] = block.textContent;
    }
};


ProjectMenu.prototype.events = function() {
    this.clickItemEvent();
    this.scrollEvent();
};


// Events
ProjectMenu.prototype.clickItemEvent = function() {
    if (!this.menuItems.length) {
        return;
    }

    for (var i=-1, l=this.menuItems.length; ++i<l;) {
        this.menuItems[i].addEventListener('click', this.onClickMenuItem.bind(this));
    }
};
ProjectMenu.prototype.scrollEvent = function() {
    window.addEventListener('scroll', this.onScroll.bind(this));
};


// Event functions
ProjectMenu.prototype.onCoverLoad = function(event) {
    this.initScrollTitles();
    this.updateMenuItems();
};
ProjectMenu.prototype.onClickMenuItem = function(event) {
    event.preventDefault();
    var target = event.target;

    this.menuInactive();
    target.classList.add('active');
    this.gotoBlock(target.textContent);
};
ProjectMenu.prototype.onScroll = function(event) {
    if (!Object.keys(this.scrollTitles).length){
        return;
    }

    var scrollY = window.scrollY;
    var title = '';
    for (var scroll in this.scrollTitles) {
        var scrollWithPadding = parseFloat(scroll) - 20;
        if (scrollWithPadding <= scrollY) {
            title = this.scrollTitles[scroll];
            continue;
        }
        break;
    }
    this.menuInactive();

    if (scrollY + window.innerHeight >= document.body.parentElement.clientHeight) {
        var titles = Object.keys(this.scrollTitles);
        var lastTitleKey = titles[titles.length - 1];
        var lastTitle = this.scrollTitles[lastTitleKey];
        this.menuActiveTtile(lastTitle);
    }
    else {
        this.menuActiveTtile(title);
    }
};


// Support functions
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
        if (!this.menuFindTitle(block.textContent)) {
            var menu = document.createElement('div');
            menu.className = 'project-menu-item';
            menu.textContent = block.textContent;
            menuItemsParent.appendChild(menu);
        }
    }
};
ProjectMenu.prototype.menuFindTitle = function(title) {
    var finded = false;

    for (var j=-1, k=this.menuItems.length; ++j<k;) {
        var menu = this.menuItems[j];
        if (menu.textContent.toLowerCase() == title.toLowerCase()) {
            finded = menu;
        }
    }

    return finded;
};
ProjectMenu.prototype.menuInactive = function() {
    if (!this.menuItems.length) {
        return;
    }

    for (var i=-1, l=this.menuItems.length; ++i<l;) {
        this.menuItems[i].classList.remove('active');
    }
};
ProjectMenu.prototype.menuActiveTtile = function(title) {
    var titleElement = this.menuFindTitle(title);
    if (!titleElement) {
        return;
    }

    titleElement.classList.add('active');
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
