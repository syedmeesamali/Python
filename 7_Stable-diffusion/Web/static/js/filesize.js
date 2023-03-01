function filesizeVal(elem)
{
    document.cookie = `filesize=${elem.files[0].size}`;
    console.log("Cookie value!" + document.cookie);
}