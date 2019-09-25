# User interactivity

## Problem
You want a field to change based on a mouse clicking a html element

## Solution

Use in built events such as onclick

## discussion

Javascript can be executed when events occur. Some of these events we can build ourselves
and others are pre built for us.

One of those events is onClick which makes javascript listen if people click on divs.

**Example:**

```HTML
<!DOCTYPE html>
<html>
    <body>
         <h1 onclick="changeOnClickt(this)">Click me!</h1>
        <script>
            function changeOnClickt(id) {
                id.innerHTML = "YES!";
            }
        </script>
    </body>
</html>
```

We can also add this functionality through the Document Object Model

```html
<!DOCTYPE html>
<html>
    <body>
         <h1 id="date">Click me!</h1>
        <script>
            document.getElementById("date");
            function changeText(id) {
                id.innerHTML = "YES!";
            }
        </script>
    </body>
</html>
```
---

But we don't always want to actually click on events, right? 

There are other events such as onmouseover and onmouseout

**Example:**

Let's say we want to change the colour of a HTML element when the 
mouse rolls over the element and then when the mouse rolls out it 
changes back to black? 

```html
<!DOCTYPE html>
<html>
	<body>

	<h1 onmouseover="style.color='green'"
	onmouseout="style.color='black'">
	Mouse over me!</h1>

	</body>
</html>
```

Just like in other examples we can bind other things to the event. 

Let's make two new functions rollOver and rollOut. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mouse Over and Out with Functions!</title>
</head>
    <body>
        <h1 onmouseover="rollOver(this)" onmouseout="rollOut(this)">
            Mouse over me!
        </h1>
    <script>
        function rollOver(obj){
            obj.innerHTML = "WOOHOHO!";
        }
        
        function rollOut(obj){
            obj.innerHTML = "Roll the mouse over me."
        }
    </script>
    </body>
</html>

```

# Problem

You want to know if an element has user focus and if so do something. 
 
# Solution 

Use onfocus 

# Pattern

Imagine that we have a bunch of fields that users can enter details. 
To help them identify what they are doing you decided that you will make it that the
active field turns yellow. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Changing  Fields on Focus</title>
</head>
    <body>
        Username: <input type="text" onfocus="focusDetected(this)"/>
        Not Username: <input type="text" onfocus="focusDetected(this)"/>
        <script>
            function focusDetected(obj){
                object.style.backgruond = 'yellow';
            }
        </script>
    </body>
</html>
```



