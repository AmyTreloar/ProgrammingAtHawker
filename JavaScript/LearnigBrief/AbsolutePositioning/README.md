# Learning Brief

Positioning of HTML elements

## Goals: 

HTML/CSS positioning

* Absolute Positioning of HTML elements through CSS

## Theoretical Components: 

[MDN: Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)


**Absolutely Positioned Element**

An absolutely positioned element is an element whose computed position value is absolute or fixed.The top, right, 
bottom, and left properties specify offsets from the edges of the element's containing block. (The containing block is 
the ancestor to which the element is relatively positioned.) If the element has margins, they are added to the offset.

Creating a box that is 50px by 50px that is 20px from the top and 20px from the left of the window. 
```html
<style>
    div .example{
        position: absolute;
        left: 20px;
        top: 20px;
        width: 50px;
        height: 50px; 
    }
</style>
```
## Practical Components: 

Create a div with the id of door and then create another div inside door and give it the id of handle

```html
<div id="door">
    <div id="handle"></div>
</div>
```

Create a style sheet and link to the HTML document. Now create two CSS entries, one for door, and the other for handle

```css
#door {

}

#handle{

}
```

The objective here is to create a series of divs that look a bit like a door. 

To make the door, let's start by giving it some size and give it a border: 

```css
#door {
    height: 200px; /*This div will be 200px high*/
    width: 100px; /*This div will be 100px wide*/
    border: 3px solid black;
}
```

If you open this page in your browser you'll see that it appears in the top left hand corner of the screen
this is it's `static` position. The default order and position as designated by the W3C. 

We want to move it around a bit. Let's move it so it is 80px from the top and 100px from the left border. 

```css
#door {
    position: absolute;
    top: 80px;
    left: 100px;
    height: 200px; /*This div will be 200px high*/
    width: 100px; /*This div will be 100px wide*/
    border: 3px solid black;
}
```


## Investigation:

It is possible to create a small box that will look like a handle. 

1. Using the div with the ID of handle generate a 10px by 10x box roughly half way down and to the left of your door.
2. Using your style sheet give your door a background colour of tan. 
3. Using your style sheet give your handle a backgroudn colour of black 
