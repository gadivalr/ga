tiny.init({
    selector: "txtContenido",
    Plugins:[
        "advlist", "autolink", "link", "image", "lists" , "charmap" , "preview", "anchor", "pagebreak",
        "searchreplace", "wordcount", "visualblocks", "visualchars", "code", "fullscreen", "insertdatetime",
        "media", "nonbreaking", "save", "table", "directionality", "emoticons", "template", "paste", "textcolor",
        "imageupload", "fileupload", "codesample", "imagetools", "mediaembed", "linkchecker", "spellchecker",
    ],

    toolbar1: "undo redo | styles | bold italic underline| alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | codesample" +
        " | imageupload fileupload | spellchecker linkchecker | preview fullscreen | forecolor backcolor emoticons",
        menu: {
            favs: {title: 'Menu', items: 'code visualaid | searchreplace | spellchecker | emoticons'}
        },
    menubar: 'file edit view insert format tools table help favs',
    content_style: "body {font-family: Hevelica, Arial, sans-serif; font-size: 16px;}",
    
});