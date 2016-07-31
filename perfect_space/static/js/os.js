var OS = function() {
    this.platform = '';
    this.android = false;
    this.ios = false;
    this.iPhone = false;
    this.iPad = false;
    this.iPod = false;

    this.init();
};
OS.prototype.init = function() {
    var userAgent = navigator.userAgent || navigator.vendor || window.opera;

    if (userAgent.match(/iPad/i)) {
        this.ios = true;
        this.iPad = true;
        this.platform = 'ipad';
    }
    else if (userAgent.match(/iPhone/i) || userAgent.match(/iPod/i))
    {
        this.ios = true;
        this.iPhone = true;
        this.platform = 'iphone';
    }
    else if (userAgent.match(/iPod/i))
    {
        this.ios = true;
        this.iPod = true;
        this.platform = 'ipod';
    }
    else if( userAgent.match(/Android/i) )
    {
        this.android = true;
        this.platform = 'android';
    }
};
