// Javascript script that adds a li element to UL.mylist after clicking

$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
});
