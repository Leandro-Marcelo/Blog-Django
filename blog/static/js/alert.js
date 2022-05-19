function deleteConfirmation(id){
    const response = confirm("are you sure?")

    if(response){
        // redirect to /posts/delete/:id
        window.location.href = "/posts/delete/"+id
    }
}


