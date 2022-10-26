// Javascript script that fetches and displays the value of hello with jQuery API

$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
