# Problem
You want to have some sort of event without using the default
methods available in JavaScript or the event that you want to 
use may change depending on use or other events. 

# Solution 

Create your own event! 

**Example:**

```html
document.getElementById('foo').addEventListener('click', displayDate);
```

# Discussion

The addEventListener() method attaches an event handler to the 
specified element without overwriting existing event handlers. 

# Patterns

Emulate an onclick event to a div with an id of foo

```html

<script>
    document.getElementByID('foo').addEventListener('click', quickAlert());
    function quickAlert(){
        alert("Hello world");
    }
</script>
```

Add multiple events to the same element: 

```html
<script>
    document.getElementById('foo').addEventListener('mouseover', rollOver());
    document.getElementById('foo').addEventListener('click', clickTime();
    
    function rollOver(){
        // some instructions
    }
    
    function clickTime(){
        // some instructions
    }
</script>
```

Pass a variable to a function that requires arguments. 

```html
<script>
    document.getElementById('foo').addEventListener('click', spamOnClick("HEY HEY HEY"));
    
    function spamOnClick(data){
        console.log(data);
    }
</script>
```

Remove an event function from an element. 

```html
<script>
    document.getElementById('foo').removeEventListener('click', someFunction)
</script>
```
