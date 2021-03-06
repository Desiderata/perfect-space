var Gallery = function(element, id) {
    this.element = element;
    this.id = id;

    this.init();
};
Gallery.prototype.init = function() {
    if (!this.element) {
        return false;
    }
    this.initGallery();
    this.initPreview();
};
Gallery.prototype.initGallery = function() {
    var gallery = this.createGallery();
    this.element.parentNode.replaceChild(gallery, this.element);
};
Gallery.prototype.initPreview = function() {
    $('.carousel-inner').lightGallery({
        download: false,
        thumbnail: true,
        selector: '.gallery-link',
        zoom: true
    });
};
Gallery.prototype.createGallery = function() {
    var images = this.element.querySelectorAll('img');
    var indicators = this.createIndicators(images.length);
    var slides = this.createSlides(images);
    var container = this.createContainer();

    container.appendChild(slides);
    if (images.length > 1) {
        container.appendChild(indicators);
        container = this.createControls(container);
    }

    return container;
};
Gallery.prototype.createContainer = function() {
    var container = document.createElement('div');
    container.id = this.getId();
    container.className = 'carousel slide carousel-fit carousel-fade';
    container.setAttribute('data-ride', 'carousel');
    container.setAttribute('data-interval', 'false');

    return container;
};
Gallery.prototype.createIndicators = function(num) {
    var container = document.createElement('ol');
    container.className = 'carousel-indicators small';

    for (var i= 0; i<num; ++i) {
        var li = document.createElement('li');
        li.setAttribute('data-target', '#' + this.getId());
        li.setAttribute('data-slide-to', i);

        if (i == 0) {
            li.className = 'active';
        }

        container.appendChild(li);
    }

    return container;
};
Gallery.prototype.createControls = function(container) {
    var spanLeft = document.createElement('span');
    spanLeft.className = 'glyphicon glyphicon-chevron-left black';

    var left = document.createElement('a');
    left.className = 'left carousel-control';
    left.setAttribute('data-slide', 'prev');
    left.href  = '#' + this.getId();
    left.appendChild(spanLeft);
    container.appendChild(left);

    var spanRight = document.createElement('span');
    spanRight.className = 'glyphicon glyphicon-chevron-right black';

    var right = document.createElement('a');
    right.className = 'right carousel-control';
    right.setAttribute('data-slide', 'next');
    right.href  = '#' + this.getId();
    right.appendChild(spanRight);
    container.appendChild(right);

    return container;
};
Gallery.prototype.createSlides = function(images) {
    var container = document.createElement('div');
    container.className = 'carousel-inner';

    for (var i=-1, l=images.length; ++i<l;) {
        var image = images[i];
        var slide = document.createElement('div');
        var link = this.createSlideLink(image);
        var title = this.createTitle(image);

        link.classList.add('gallery-link');
        slide.className = i == 0 ? 'item active' : 'item';
        slide.appendChild(link);
        slide.appendChild(title);
        container.appendChild(slide);
    }

    return container;
};
Gallery.prototype.createSlideLink = function(image) {
    var container = document.createElement('a');
    container.href = image.src;

    var img = document.createElement('img');
    img.className = 'img-small-slide';
    img.src = image.src;

    container.appendChild(img);

    return container;
};
Gallery.prototype.createTitle = function(image) {
    var div = document.createElement('div');
    div.className = 'gallery-title';
    image.alt.length ? div.innerHTML = image.alt : div.classList.add('no-title');

    return div;
};
Gallery.prototype.getId = function() {
    return 'carousel-' + this.id;
};
