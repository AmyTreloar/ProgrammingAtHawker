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
            function changeText(id) {
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
