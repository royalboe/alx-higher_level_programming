window.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
