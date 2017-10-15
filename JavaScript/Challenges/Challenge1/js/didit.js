var isUpvote = true;



function changeVote(id){
    isUpvote = !isUpvote;

    if (isUpvote === true){
        id.src = "img/upvote.png";
    } else {
        id.src = "img/downvote.png";
    }
}

function mouseOverPost(id){
    id.style.backgroundColor = "red";
}

function mouseLeavePost(id){
    id.style.backgroundColor = "white";
}