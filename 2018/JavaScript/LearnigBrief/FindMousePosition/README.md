# Learning Brief

Locate where the mouse is pointing on your screen. 

## Goals

* Locate where your mouse is on the screen
* Move a HTML element on the screen based off your mouse movements 

## Theoretical Components 

[MDN: mousemove](https://developer.mozilla.org/en-US/docs/Web/Events/mousemove)

The mousemove event is fired when a pointing device (usually a mouse) is moved while over an element.

clientX Read only	long	The X coordinate of the mouse pointer in local (DOM content) coordinates.

clientY Read only	long	The Y coordinate of the mouse pointer in local (DOM content) coordinates.

## Practical Components 

Create the following divs in the body of your HTMl document: 

```html
div class="gameWindow" onclick="showCoords(event)">
    <p id="demo"></p>
</div>
```

In your style sheet add the following style: 

```css
.gameWindow {
    width: 500px;
    height: 300px;
    border: 1px solid black;
    text-align: center;
}
```

When mouse events are fired certain information is passed through the event itself. We can use this to cature 
the location of the mouse x and y positions. 

In your script document add the following script. 

```javascript
function showCoords(event){
    var x = event.clientX;
    var y = event.clientY;
    document.getElementById("demo").innerHTML = "x="+x+", y="+y;
}
```

Now click on the screen somewhere. 

That's a nice starting point but what if we want to move elements? 


Create a new HTMl page. In the body section put the following divs into the body section
```html
<div class="gameWindow" onmousemove="showCoords(event)">
    <div id="demo"></div>
</div>
```

Next we will make gamewindow so that is 500px wide and 300px high and then put a border around it. We will also centre
it so it is in the middle of the screen.

We will also define the demo div so it is 10px wide and high. We will also make it absolutely positioned so it appears 
exactly where we want.  

```css
.gameWindow {
    width: 500px;
    height: 300px;
    border: 1px solid black;
    text-align: center;
}

#demo {
    width:10px;
    height:10px;
    position:absolute;
    background-color: black;
    left:0;
    top:0;
}
```

In the following javascript we do two things: 

1. We get the x and y position of the mouse based off of the mousemove event listed above and through that we find the 
x and y position based off of the client space. 

We then find the demo div dynamically and we write the new left top position in relationship to that new x and y position. 

```javascript
function showCoords(event){
    var x = event.clientX;
    var y = event.clientY;
    console.log("x="+x+", y="+y);
    var demo = document.getElementById("demo");
    demo.style.left = x+"px";
    demo.style.top = y+"px";

}
```


## Investigation 

Using the information that you've been shown here try and make a full screen web application that is black. Then create
div that follows the mouse pointer around the screen. 

Extension: How can we turn the box into a circle? 
 