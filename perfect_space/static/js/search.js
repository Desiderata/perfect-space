var Search = function() {
    this.searchButton = document.getElementById('search-button');
    this.searchInput = document.getElementById('search-input');
    this.searchText = this.searchInput.textContent;
    this.minWidth = parseInt(window.getComputedStyle(this.searchInput).getPropertyValue('min-width'));
    this.width = this.minWidth;
    this.init();
    this.events();
};
Search.prototype.init = function() {

};
Search.prototype.events = function() {
    this.searchButton.addEventListener('click', this.onClickSearchButton.bind(this));
    this.searchInput.addEventListener('keydown', this.onKeyInputSearch.bind(this));
    this.searchInput.addEventListener('focus', this.onFocusInputSearch.bind(this));
    this.searchInput.addEventListener('blur', this.onBlurInputSearch.bind(this));
};


Search.prototype.onClickSearchButton = function(event) {
    event.preventDefault();
    var query = this.searchInput.textContent;
    var searchUrl = this.searchButton.getAttribute('data-url');
    document.location = searchUrl + '?q=' + query;
};
Search.prototype.onKeyInputSearch = function(event) {
    var target = event.target;
    if (event.code == 'Enter') {
        event.preventDefault();
    }
    if (target.style.width) {
        target.removeAttribute('style');
    }

};
Search.prototype.onFocusInputSearch = function(event) {
    var target = event.target;
    if (target.textContent == this.searchText) {
        target.textContent = ' ';
    }
    else {
        target.style.width = Math.max(this.minWidth, this.width);
    }

    var range = document.createRange();
    var sel = window.getSelection();
    range.setStart(target.childNodes[0], 0);
    range.collapse(true);
    sel.removeAllRanges();
    sel.addRange(range);
};
Search.prototype.onBlurInputSearch = function(event) {
    var target = event.target;
    if (target.textContent == '') {
        target.textContent = this.searchText;
    }

    target.style.width = target.clientWidth;
    target.style.display = 'none';
    target.offsetHeight;
    target.style.display = 'block';

    this.width = target.clientWidth;
    target.style.width = this.minWidth;
};
