

var viewsize = view.size;

var atoms = [];

var rand;
var rad;

for (i = 0; i < 6; i++) {
    rand = new Point.random();
    rand.x *= viewsize.width;
    rand.y *= viewsize.height;
    rad = 5 + Math.random() * 10; // radius
    
    circle = new Path.Circle(rand, rad);
    circle.fillColor = 'black';
    console.log(circle);
    atoms.push(circle);
}


function onFrame(event) {
    
}


function onMouseUp(event) {
    for (var i=0; i < atoms.length; i++) {
        atoms[i].fillColor = 'red';
    }
}
