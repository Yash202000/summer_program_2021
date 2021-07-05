
const myForm = document.getElementById('myForm');
const inpFile = document.getElementById('inpFile');

myForm.addEventListener("submit",e => {
    e.preventDefault();
    const endpoint = '/cred';
    const formData = new FormData();

    formData.append("inpFile",inpFile.files[0]);
    console.log(formData);
    fetch(endpoint,{
        method: "post",
        body: formData
    }).catch(console.error);

});