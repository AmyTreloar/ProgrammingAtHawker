var isUpvote = true;
var deg = 180;


function changeVote(id){
    console.log(deg);
    if (isUpvote){
        deg = 0;
    } else {
        deg = 180;
    }
    isUpvote = !isUpvote;
    deg = 0 - deg;
    if (id.innerHTML === "O"){
        id.innherHTML = "^";
    }
    id.style.webkitTransform = 'rotate('+deg+'deg)';
    id.style.mozTransform    = 'rotate('+deg+'deg)';
    id.style.msTransform     = 'rotate('+deg+'deg)';
    id.style.oTransform      = 'rotate('+deg+'deg)';
    id.style.transform       = 'rotate('+deg+'deg)';
    if (isUpvote === true){
        id.style.color = 'red';
    } else {
        id.style.color = 'blue';
    }
}

function mouseOverPost(id){
    id.style.backgroundColor = "red";
}

function mouseLeavePost(id){
    id.style.backgroundColor = "white";
}