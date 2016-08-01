var Mobile = function() {
    this.cover = document.getElementById('cover');
    this.desktop = document.getElementById('desktop');
    this.mobileCarousel = document.getElementById('mobile-carousel');
    this.mobileSwitch = document.getElementById('mobile-switch');
    this.disable = Cookies.get('mobile');
    this.init();
    this.events();
};
Mobile.prototype.init = function() {
    var os = new OS();
    if (this.disable) {
        this.initDesktop();
        return;
    }

    if (os.android || os.ios) {
        this.initMobile();
    }
    else {
        this.initDesktop();
    }
};
Mobile.prototype.events = function() {
    this.mobileSwitch.addEventListener('click', this.onClickSwitch.bind(this));
};
Mobile.prototype.onClickSwitch = function(event) {
    event.preventDefault();
    Cookies.set('mobile', false);
    this.initDesktop();
};
Mobile.prototype.initMobile = function() {
    document.body.style.minWidth = '100%';
    document.body.style.width = '100%';
    document.body.style.paddingBottom = 0;
    this.addMeta();
    this.cover.style.display = 'block';
    this.initSlick();
};
Mobile.prototype.initDesktop = function() {
    this.removeMeta();
    this.desktop.style.display = 'block';
    this.cover.style.display = 'none';
};
Mobile.prototype.initSlick = function() {
    $(this.mobileCarousel).slick({
        arrows: false,
        autoplay: true,
        autoplaySpeed: 1500
        //fade: true
    });
};
Mobile.prototype.addMeta = function() {
    var meta = document.createElement('meta');
    meta.setAttribute('name', 'viewport');
    meta.setAttribute('content', 'width=device-width, initial-scale=1');
    document.head.appendChild(meta);
};
Mobile.prototype.removeMeta = function() {
    var meta = document.querySelector('meta[name="viewport"]');
    if (!meta) {
        return;
    }

    meta.parentElement.removeChild(meta);
};
