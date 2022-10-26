window.addEventListener('DOMContentLoaded', function () {
  $('INPUT#language_code').keypress(function (event) {
    const keyCode = event.which;
    if (keyCode === 13) {
      const lang = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
