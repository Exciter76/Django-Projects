
function main(){
    alert("hello contact");
}

function validate(){
    
    //let strEmail = document.forms["contact_detail"]["id_email"].value;
    
    let strEmail = document.getElementById("id_email").value;
    alert(strEmail);
    if(strEmail.search("@") == false){
        alert("Email must have an @");
        return false;
    }

    if(strEmail.search(".") == false){
        alert("Email must have an .")
        return false;
    }

    
}