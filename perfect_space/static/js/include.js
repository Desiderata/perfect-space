$(document).ready(function () {
	$('*').each(function (i, elem) {
		if ($(elem).attr('data-page')) {
			$.get("templates/"+ $(elem).attr('data-page') +".html", function (data) {
				$(elem).append(data);
			});
		}
		if ($(elem).attr('data-about-page')) {
			$.get("about/"+ $(elem).attr('data-about-page') +".html", function (data) {
				$(elem).append(data);
			});
		}
    });
	lightbox.option({
      'disableScrolling': true,
	  'fixedNavigation': true
    })
});